from constructs import Construct
from aws_cdk import Stack
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_cloudfront as cloudfront
from aws_cdk import aws_cloudfront_origins as origins
from aws_cdk import aws_s3_deployment as s3deploy
from os import path


class SendAllTrafficToOnePlaceStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        target_bucket = s3.Bucket(
            self, 
            'cdkSendAllTrafficToOnePlaceBucket'
        )

        s3deploy.BucketDeployment(
            self, 
            "cdkSendAllTrafficToOnePlaceDeployment",
            sources=[s3deploy.Source.asset(path.join("assets", "s3-files"))],
            destination_bucket=target_bucket
        )

        cf_function = cloudfront.Function(
            self, 
            'cdkSendAllTrafficToOnePlaceFunction',
            code=cloudfront.FunctionCode.from_inline("""
function handler(event) {
	var request = event.request;
	request.uri = '/target.html';
	return request;
}
            """)
        )

        cloudfront.Distribution(self, 'cdkSendAllTrafficToOnePlaceDistribution',
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.S3Origin(target_bucket),
                function_associations=[cloudfront.FunctionAssociation(
                    function=cf_function,
                    event_type=cloudfront.FunctionEventType.VIEWER_REQUEST
                )]
            )
        )

