import aws_cdk as core
import aws_cdk.assertions as assertions

from api_gateway_websockets_cloudfront_s3_chat_prototype.api_gateway_websockets_cloudfront_s3_chat_prototype_stack import ApiGatewayWebsocketsCloudfrontS3ChatPrototypeStack

# example tests. To run these tests, uncomment this file along with the example
# resource in api_gateway_websockets_cloudfront_s3_chat_prototype/api_gateway_websockets_cloudfront_s3_chat_prototype_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ApiGatewayWebsocketsCloudfrontS3ChatPrototypeStack(app, "api-gateway-websockets-cloudfront-s3-chat-prototype")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
