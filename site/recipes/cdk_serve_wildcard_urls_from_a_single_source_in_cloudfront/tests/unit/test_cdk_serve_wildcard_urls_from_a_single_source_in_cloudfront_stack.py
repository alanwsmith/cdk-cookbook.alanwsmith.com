import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_serve_wildcard_urls_from_a_single_source_in_cloudfront.cdk_serve_wildcard_urls_from_a_single_source_in_cloudfront_stack import CdkServeWildcardUrlsFromASingleSourceInCloudfrontStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_serve_wildcard_urls_from_a_single_source_in_cloudfront/cdk_serve_wildcard_urls_from_a_single_source_in_cloudfront_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkServeWildcardUrlsFromASingleSourceInCloudfrontStack(app, "cdk-serve-wildcard-urls-from-a-single-source-in-cloudfront")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
