from constructs import Construct
from aws_cdk import Stack
from aws_cdk import aws_apigatewayv2_alpha as apiv2a
from aws_cdk import aws_apigatewayv2_integrations_alpha as apiv2ai
from aws_cdk import aws_lambda as lambda_
from aws_cdk import aws_dynamodb as dynamodb
from os import path

class ApiGatewayWebsocketChatAppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        web_socket_api = apiv2a.WebSocketApi(
            self, 
            "CDK_EXAMPLE_CHAT_APP_WEBSOCKET_API"
        )

        apiv2a.WebSocketStage(
            self, 
            "CDK_EXAMPLE_CHAT_APP_WEBSOCKET_STAGE",
            web_socket_api=web_socket_api,
            stage_name="dev",
            auto_deploy=True
        )

        message_handler = lambda_.Function(
            self, 
            "CDK_EXAMPLE_CHAT_APP_MESSAGE_FUNCTION",
            runtime=lambda_.Runtime.NODEJS_16_X,
            handler="index.handler",
            code=lambda_.Code.from_asset(
                path.join(
                    'assets', 'lambda-functions', 'message_handler'
                )
            )
        )

        web_socket_api.add_route(
            "message",
            integration=apiv2ai.WebSocketLambdaIntegration(
                "CDK_EXAMPLE_CHAT_APP_MESSAGE_ROUTE",
                message_handler
            )
        )

        connect_handler = lambda_.Function(
            self, 
            "cdkApiGatewayWebsocketsCloudfrontS3ChatPrototypeConnectFunciton",
            runtime=lambda_.Runtime.NODEJS_16_X,
            handler="index.handler",
            code=lambda_.Code.from_asset(
                path.join(
                    'assets', 'lambda-functions', 'connect_handler'
                )
            )
        )

        web_socket_api.add_route(
            "$connect",
            integration=apiv2ai.WebSocketLambdaIntegration(
                "cdkApiGatewayWebsocketsCloudfrontS3ChatPrototypeConnectIntegration",
                connect_handler
            )
        )

        disconnect_handler = lambda_.Function(
            self, 
            "cdkApiGatewayWebsocketsCloudfrontS3ChatPrototypeDisconnectFunciton",
            runtime=lambda_.Runtime.NODEJS_16_X,
            handler="index.handler",
            code=lambda_.Code.from_asset(
                path.join(
                    'assets', 'lambda-functions', 'disconnect_handler'
                )
            )
        )

        web_socket_api.add_route(
            "$disconnect",
            integration=apiv2ai.WebSocketLambdaIntegration(
                "cdkApiGatewayWebsocketsCloudfrontS3ChatPrototypeDisconnectIntegration",
                disconnect_handler
            )
        )

        default_handler = lambda_.Function(
            self, 
            "cdkApiGatewayWebsocketsCloudfrontS3ChatPrototypeDefaultFunciton",
            runtime=lambda_.Runtime.NODEJS_16_X,
            handler="index.handler",
            code=lambda_.Code.from_asset(
                path.join(
                    'assets', 'lambda-functions', 'default_handler'
                )
            )
        )

        web_socket_api.add_route(
            "$default",
            integration=apiv2ai.WebSocketLambdaIntegration(
                "cdkApiGatewayWebsocketsCloudfrontS3ChatPrototypeDefaultIntegration",
                default_handler
            )
        )

        global_table = dynamodb.Table(
            self, 
            "cdkApiGatewayWebsocketsChatPrototypeTable",
            partition_key=dynamodb.Attribute(
                name="connectionId", 
                type=dynamodb.AttributeType.STRING
            ),
        )

        global_table.grant_read_write_data(connect_handler)
        global_table.grant_read_write_data(default_handler)
        global_table.grant_read_write_data(message_handler)
        global_table.grant_read_write_data(disconnect_handler)

        http_api = apiv2a.HttpApi(
            self, 
            "cdkApiGatewayWebsocketsCloudfrontS3ChatPrototypeHTTPAPI"
        )

        web_page = lambda_.Function(
            self, 
            "cdkApiGatewayWebsocketsCloudfrontS3ChatPrototypeWebPage",
            runtime=lambda_.Runtime.NODEJS_16_X,
            handler="index.handler",
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
                "cdkApiGatewayWebsocketsCloudfrontS3ChatPrototypeWebPageIntegration",
                web_page
            )
        )

        

