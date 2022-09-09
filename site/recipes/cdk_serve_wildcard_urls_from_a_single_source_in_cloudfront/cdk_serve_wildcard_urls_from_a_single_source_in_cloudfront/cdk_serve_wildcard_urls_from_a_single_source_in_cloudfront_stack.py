from constructs import Construct
from aws_cdk import Stack
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_s3_deployment as s3deploy
from aws_cdk import aws_cloudfront as cloudfront
from aws_cdk import aws_cloudfront_origins as origins
from os import path

class CdkServeWildcardUrlsFromASingleSourceInCloudfrontStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        target_bucket = s3.Bucket(
            self, 
            'cdkServeWildcardURLsFromASingleSourceInCloudfrontBucket'
        )

        s3deploy.BucketDeployment(
            self, 
            'cdkServeWildcardURLsFromASingleSourceInCloudfrontBucketDeployment',
            sources=[s3deploy.Source.asset(path.join("assets", "s3-files"))],
            destination_bucket=target_bucket
        )

        rewrite_function = cloudfront.Function(
            self, 
            'cdkServeWildcardURLsFromASingleSourceInCloudfrontFunction',
            code=cloudfront.FunctionCode.from_inline("""
function handler(event) {
	var request = event.request;
	if (request.uri.indexOf('/collector/') === 0) {
	    request.uri = '/collector/index.html';
    }
	return request;
}
            """)
        )

        cloudfront.Distribution(
            self, 
            'cdkServeWildcardURLsFromASingleSourceInCloudfrontDistribution',
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.S3Origin(target_bucket),
                function_associations=[cloudfront.FunctionAssociation(
                    function=rewrite_function,
                    event_type=cloudfront.FunctionEventType.VIEWER_REQUEST
                )]
            )
        )

