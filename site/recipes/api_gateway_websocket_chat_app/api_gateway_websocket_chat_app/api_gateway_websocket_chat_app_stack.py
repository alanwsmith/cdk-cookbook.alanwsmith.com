from constructs import Construct
from aws_cdk import Stack
from aws_cdk import aws_apigatewayv2_alpha as apiv2a
from aws_cdk import aws_apigatewayv2_integrations_alpha as apiv2ai
from aws_cdk import aws_lambda as lambda_
from aws_cdk import aws_dynamodb as dynamodb
from aws_cdk import aws_iam as iam
from aws_cdk import Aws 
# from aws_cdk import CfnMapping
from os import path

class ApiGatewayWebsocketChatAppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        global_table = dynamodb.Table(
            self, 
            "CDK_TABLE_FOR_WEBSOCKET_EXAMPLE_APP",
            partition_key=dynamodb.Attribute(
                name="connectionId", 
                type=dynamodb.AttributeType.STRING
            ),
        )

        web_socket_api = apiv2a.WebSocketApi(
            self, 
            "CDK_WEBSOCKET_API_FOR_WEBSOCKET_EXAMPLE_APP"
        )

        web_socket_stage = apiv2a.WebSocketStage(
            self, 
            "CDK_STAGE_FOR_WEBSOCKET_EXAMPLE_APP",
            web_socket_api=web_socket_api,
            stage_name="dev",
            auto_deploy=True,
        )

        # lambda_policy_statement = iam.PolicyStatement(
        #     principals= [
        #         iam.ServicePrincipal("apigateway.amazonaws.com")
        #     ],
        #     actions=[
        #         "execute-api:ManageConnections"
        #     ],
        #     resources=[
        #         f"arn:aws:execute-api:us-east-1:{Aws.ACCOUNT_ID}:*/*/POST/@connections/*"
        #     ]
        # )


        lambda_role = iam.Role(
            self, 
            "cdkExampleWebsocketChatApp",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            inline_policies={
                "cdkExampleWebsocketChatAppPolicy": iam.PolicyDocument(
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


            # inline_policies=CfnMapping(self, "RegionTable",
                # iam.PolicyDocument(
                #     statements=[
                #         iam.PolicyStatement(
                #             principals= [
                #                 iam.ServicePrincipal("apigateway.amazonaws.com")
                #             ],
                #             actions=[
                #                 "execute-api:ManageConnections"
                #             ],
                #             resources=[
                #                 f"arn:aws:execute-api:us-east-1:{Aws.ACCOUNT_ID}:*/*/POST/@connections/*"
                #             ]
                #         )
                #     ]
                # )    
             #                          ),


        # lambda_permissions = lambda_.Permission(
        #     principal=iam.ServicePrincipal("apigateway.amazonaws.com"),
        #     action="execute-api:ManageConnections",
        # )

        send_message_handler = lambda_.Function(
            self, 
            "CDK_MESSAGE_HANDLER_FOR_WEBSOCKET_EXAMPLE_APP",
            runtime=lambda_.Runtime.NODEJS_16_X,
            handler="index.handler",
            environment={
                "table":global_table.table_name
            },
            role=lambda_role,
            # initial_policy=[lambda_policy_statement],
            code=lambda_.Code.from_asset(
                path.join(
                    'assets', 'lambda-functions', 'send_message_handler'
                )
            )
        )

        # send_message_handler.add_permission(
        #     "CDK_MESSAGE_HANDLER_PERMISSIONS_FOR_WEBSOCKET_EXAMPLE_APP",
        #     # principal=iam.ServicePrincipal("apigateway.amazonaws.com")
        # )


        # send_message_handler.add_permission(
        #     "CDK_MESSAGE_HANDLER_PERMISSIONS_FOR_WEBSOCKET_EXAMPLE_APP",
        #     principal=iam.ServicePrincipal("apigateway.amazonaws.com")
        # )

        # send_message_handler.add_to_role_policy(
        #     lambda_policy_statement
        # )




        web_socket_api.add_route(
            "send_message",
            integration=apiv2ai.WebSocketLambdaIntegration(
                "CDK_MESSAGE_HANDLER_ROUTE_FOR_WEBSOCKET_EXAMPLE_APP",
                send_message_handler
            )
        )

        connect_handler = lambda_.Function(
            self, 
            "CDK_CONNECT_HANDLER_FOR_WEBSOCKET_EXAMPLE_APP",
            runtime=lambda_.Runtime.NODEJS_16_X,
            handler="index.handler",
            role=lambda_role,
            environment={
                "table":global_table.table_name
            },
            # initial_policy=[lambda_policy_statement],
            code=lambda_.Code.from_asset(
                path.join(
                    'assets', 'lambda-functions', 'connect_handler'
                )
            )
        )

        # connect_handler.add_permission(
        #     "CDK_CONNECT_HANDLER_PERMISSION_FOR_WEBSOCKET_EXAMPLE_APP",
        #     principal=iam.ServicePrincipal("apigateway.amazonaws.com")
        # )

        # connect_handler.add_to_role_policy(
        #     lambda_policy_statement
        # )


        web_socket_api.add_route(
            "$connect",
            integration=apiv2ai.WebSocketLambdaIntegration(
                "CDK_CONNECT_HANDLER_ROUTE_FOR_WEBSOCKET_EXAMPLE_APP",
                connect_handler
            )
        )

        disconnect_handler = lambda_.Function(
            self, 
            "CDK_DISCONNECT_HANDLER_FOR_WEBSOCKET_EXAMPLE_APP",
            runtime=lambda_.Runtime.NODEJS_16_X,
            handler="index.handler",
            role=lambda_role,
            environment={
                "table":global_table.table_name
            },
            # initial_policy=[lambda_policy_statement],
            code=lambda_.Code.from_asset(
                path.join(
                    'assets', 'lambda-functions', 'disconnect_handler'
                )
            )
        )

        # disconnect_handler.add_permission(
        #     "CDK_DISCONNECT_HANDLER_PERMISSION_FOR_WEBSOCKET_EXAMPLE_APP",
        #     principal=iam.ServicePrincipal("apigateway.amazonaws.com")
        # )

        # disconnect_handler.add_to_role_policy(
        #     lambda_policy_statement
        # )

        web_socket_api.add_route(
            "$disconnect",
            integration=apiv2ai.WebSocketLambdaIntegration(
                "CDK_DISCONNECT_HANDLER_ROUTE_FOR_WEBSOCKET_EXAMPLE_APP",
                disconnect_handler
            )
        )

        default_handler = lambda_.Function(
            self, 
            "CDK_DEFAULT_HANDLER_FOR_WEBSOCKET_EXAMPLE_APP",
            runtime=lambda_.Runtime.NODEJS_16_X,
            handler="index.handler",
            role=lambda_role,
            environment={
                "table":global_table.table_name
            },
            # initial_policy=[lambda_policy_statement],
            code=lambda_.Code.from_asset(
                path.join(
                    'assets', 'lambda-functions', 'default_handler'
                )
            )
        )

        # default_handler.add_permission(
        #     "CDK_DEFAULT_HANDLER_PERMISSION_FOR_WEBSOCKET_EXAMPLE_APP",
        #     principal=iam.ServicePrincipal("apigateway.amazonaws.com")
        # )

        # default_handler.add_to_role_policy(
        #     lambda_policy_statement
        # )

        web_socket_api.add_route(
            "$default",
            integration=apiv2ai.WebSocketLambdaIntegration(
                "CDK_DEFAULT_HANDLER_ROUTE_FOR_WEBSOCKET_EXAMPLE_APP",
                default_handler
            )
        )

        global_table.grant_read_write_data(connect_handler)
        global_table.grant_read_write_data(default_handler)
        global_table.grant_read_write_data(send_message_handler)
        global_table.grant_read_write_data(disconnect_handler)

        http_api = apiv2a.HttpApi(
            self, 
            "CDK_HTTP_API_FOR_WEBSOCKET_EXAMPLE_APP"
        )

        web_page = lambda_.Function(
            self, 
            "CDK_WEB_PAGE_FOR_WEBSOCKET_EXAMPLE_APP",
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
                "CDK_WEB_PAGE_ROUTE_FOR_WEBSOCKET_EXAMPLE_APP",
                web_page
            )
        )

        

