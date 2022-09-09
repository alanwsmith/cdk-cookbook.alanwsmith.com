import aws_cdk as core
import aws_cdk.assertions as assertions

from api_gateway_websocket_chat_app.api_gateway_websocket_chat_app_stack import ApiGatewayWebsocketChatAppStack

# example tests. To run these tests, uncomment this file along with the example
# resource in api_gateway_websocket_chat_app/api_gateway_websocket_chat_app_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ApiGatewayWebsocketChatAppStack(app, "api-gateway-websocket-chat-app")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
