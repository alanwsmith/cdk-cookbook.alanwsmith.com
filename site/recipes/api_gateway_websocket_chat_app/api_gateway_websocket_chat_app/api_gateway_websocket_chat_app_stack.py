from constructs import Construct
from aws_cdk import Stack
from aws_cdk import aws_apigatewayv2_alpha as apiv2a
from aws_cdk import aws_apigatewayv2_integrations_alpha as apiv2ai
from aws_cdk import aws_lambda as lambda_
from aws_cdk import aws_dynamodb as dynamodb
from aws_cdk import aws_iam as iam
from aws_cdk import Aws 
from os import path

class ApiGatewayWebsocketChatAppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        dynamo_table = dynamodb.Table(
            self, 
            "cdk_ChatApp_Table",
            partition_key=dynamodb.Attribute(
                name="connectionId", 
                type=dynamodb.AttributeType.STRING
            ),
        )

        web_socket_api = apiv2a.WebSocketApi(
            self, 
            "cdk_ChatApp_Websocket_API"
        )

        web_socket_stage = apiv2a.WebSocketStage(
            self, 
            "cdk_ChatApp_Dev_Websocket_Stage",
            web_socket_api=web_socket_api,
            stage_name="dev",
            auto_deploy=True,
        )

        lambda_role = iam.Role(
            self, 
            "cdk_ChatApp_Lambda_Role",
            assumed_by=iam.ServicePrincipal(
                "lambda.amazonaws.com"
            ),
            inline_policies={
                "cdk_ChatApp_Lambda_Policy_Document": iam.PolicyDocument(
                    statements=[
                        iam.PolicyStatement(
                            actions=[
                                "execute-api:ManageConnections",
                                "service-role:AWSLambdaBasicExecutionRole",
                                "service-role:AWSLambdaVPCAccessExecutionRole"
                            ],
                            resources=[
                                f"arn:aws:execute-api:us-east-1:{Aws.ACCOUNT_ID}:*/*/POST/@connections/*"
                            ]
                        )
                    ]
                )
             }
        )
        connect_handler = lambda_.Function(
            self, 
            "cdk_ChatApp_Connect_Handler",
            runtime=lambda_.Runtime.NODEJS_16_X,
            handler="index.handler",
            role=lambda_role,
            environment={
                "table":dynamo_table.table_name
            },
            code=lambda_.Code.from_asset(
                path.join(
                    'assets', 'lambda-functions', 'connect_handler'
                )
            )
        )

        web_socket_api.add_route(
            "$connect",
            integration=apiv2ai.WebSocketLambdaIntegration(
                "cdk_ChatApp_Connect_Integration",
                connect_handler
            )
        )

        default_handler = lambda_.Function(
            self, 
            "cdk_ChatApp_Default_Handler",
            runtime=lambda_.Runtime.NODEJS_16_X,
            handler="index.handler",
            role=lambda_role,
            environment={
                "table":dynamo_table.table_name
            },
            code=lambda_.Code.from_asset(
                path.join(
                    'assets', 'lambda-functions', 'default_handler'
                )
            )
        )

        web_socket_api.add_route(
            "$default",
            integration=apiv2ai.WebSocketLambdaIntegration(
                "cdk_ChatApp_Default_Integration",
                default_handler
            )
        )


        disconnect_handler = lambda_.Function(
            self, 
            "cdk_ChatApp_Disconnect_Handler",
            runtime=lambda_.Runtime.NODEJS_16_X,
            handler="index.handler",
            role=lambda_role,
            environment={
                "table":dynamo_table.table_name
            },
            code=lambda_.Code.from_asset(
                path.join(
                    'assets', 'lambda-functions', 'disconnect_handler'
                )
            )
        )

        web_socket_api.add_route(
            "$disconnect",
            integration=apiv2ai.WebSocketLambdaIntegration(
                "cdk_ChatApp_Disconnect_Integration",
                disconnect_handler
            )
        )

        send_message_handler = lambda_.Function(
            self, 
            "cdk_ChatApp_Send_Message_Handler",
            runtime=lambda_.Runtime.NODEJS_16_X,
            handler="index.handler",
            environment={
                "table":dynamo_table.table_name
            },
            role=lambda_role,
            code=lambda_.Code.from_asset(
                path.join(
                    'assets', 'lambda-functions', 'send_message_handler'
                )
            )
        )

        web_socket_api.add_route(
            "send_message",
            integration=apiv2ai.WebSocketLambdaIntegration(
                "cdk_ChatApp_Send_Message_Integration",
                send_message_handler
            )
        )



        dynamo_table.grant_read_write_data(connect_handler)
        dynamo_table.grant_read_write_data(default_handler)
        dynamo_table.grant_read_write_data(send_message_handler)
        dynamo_table.grant_read_write_data(disconnect_handler)

        http_api = apiv2a.HttpApi(
            self, 
            "cdk_ChatApp_HTTP_API"
        )

        web_page = lambda_.Function(
            self, 
            "cdk_ChatApp_Web_Page",
            runtime=lambda_.Runtime.NODEJS_16_X,
            handler="index.handler",
            environment={
                "websocket_endpoint": web_socket_stage.url
            },
            code=lambda_.Code.from_asset(
                path.join(
                    'assets', 'lambda-functions', 'web_page'
                )
            )
        )

        http_api.add_routes(
            path="/",
            methods=[apiv2a.HttpMethod.GET],
            integration=apiv2ai.HttpLambdaIntegration(
                "cdk_ChatApp_Web_Page_Integration",
                web_page
            )
        )

