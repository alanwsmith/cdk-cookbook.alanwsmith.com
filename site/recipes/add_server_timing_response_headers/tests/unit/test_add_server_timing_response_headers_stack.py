import aws_cdk as core
import aws_cdk.assertions as assertions

from add_server_timing_response_headers.add_server_timing_response_headers_stack import AddServerTimingResponseHeadersStack

# example tests. To run these tests, uncomment this file along with the example
# resource in add_server_timing_response_headers/add_server_timing_response_headers_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AddServerTimingResponseHeadersStack(app, "add-server-timing-response-headers")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
