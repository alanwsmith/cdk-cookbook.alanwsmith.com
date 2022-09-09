import aws_cdk as core
import aws_cdk.assertions as assertions

from serve_one_s3_file_to_multiple_urls_in_cloudfront_with_lambda_edge_functions.serve_one_s3_file_to_multiple_urls_in_cloudfront_with_lambda_edge_functions_stack import ServeOneS3FileToMultipleUrlsInCloudfrontWithLambdaEdgeFunctionsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in serve_one_s3_file_to_multiple_urls_in_cloudfront_with_lambda_edge_functions/serve_one_s3_file_to_multiple_urls_in_cloudfront_with_lambda_edge_functions_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ServeOneS3FileToMultipleUrlsInCloudfrontWithLambdaEdgeFunctionsStack(app, "serve-one-s3-file-to-multiple-urls-in-cloudfront-with-lambda-edge-functions")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
