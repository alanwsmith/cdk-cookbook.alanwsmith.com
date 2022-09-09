import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_cloudfront_server_timing_response_headers.cdk_cloudfront_server_timing_response_headers_stack import CdkCloudfrontServerTimingResponseHeadersStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_cloudfront_server_timing_response_headers/cdk_cloudfront_server_timing_response_headers_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkCloudfrontServerTimingResponseHeadersStack(app, "cdk-cloudfront-server-timing-response-headers")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
