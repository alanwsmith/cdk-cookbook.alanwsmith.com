import aws_cdk as core
import aws_cdk.assertions as assertions

from make_cloudfront_request_and_response_lambda_functions.make_cloudfront_request_and_response_lambda_functions_stack import MakeCloudfrontRequestAndResponseLambdaFunctionsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in make_cloudfront_request_and_response_lambda_functions/make_cloudfront_request_and_response_lambda_functions_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = MakeCloudfrontRequestAndResponseLambdaFunctionsStack(app, "make-cloudfront-request-and-response-lambda-functions")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
