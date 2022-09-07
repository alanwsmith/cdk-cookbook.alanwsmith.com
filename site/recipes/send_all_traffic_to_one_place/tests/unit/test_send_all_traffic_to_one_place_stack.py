import aws_cdk as core
import aws_cdk.assertions as assertions

from send_all_traffic_to_one_place.send_all_traffic_to_one_place_stack import SendAllTrafficToOnePlaceStack

# example tests. To run these tests, uncomment this file along with the example
# resource in send_all_traffic_to_one_place/send_all_traffic_to_one_place_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SendAllTrafficToOnePlaceStack(app, "send-all-traffic-to-one-place")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
