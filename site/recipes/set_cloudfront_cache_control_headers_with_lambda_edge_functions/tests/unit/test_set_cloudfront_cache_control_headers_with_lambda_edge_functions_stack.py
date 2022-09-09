import aws_cdk as core
import aws_cdk.assertions as assertions

from set_cloudfront_cache_control_headers_with_lambda_edge_functions.set_cloudfront_cache_control_headers_with_lambda_edge_functions_stack import SetCloudfrontCacheControlHeadersWithLambdaEdgeFunctionsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in set_cloudfront_cache_control_headers_with_lambda_edge_functions/set_cloudfront_cache_control_headers_with_lambda_edge_functions_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SetCloudfrontCacheControlHeadersWithLambdaEdgeFunctionsStack(app, "set-cloudfront-cache-control-headers-with-lambda-edge-functions")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
