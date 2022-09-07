import aws_cdk as core
import aws_cdk.assertions as assertions

from server_timing_headers.server_timing_headers_stack import ServerTimingHeadersStack

# example tests. To run these tests, uncomment this file along with the example
# resource in server_timing_headers/server_timing_headers_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ServerTimingHeadersStack(app, "server-timing-headers")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
