from constructs import Construct
from aws_cdk import Stack
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_cloudfront as cloudfront
from aws_cdk import aws_cloudfront_origins as origins
from aws_cdk import aws_s3_deployment as s3deploy
from os import path

class CloudfrontServerTimingResponseHeadersStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        target_bucket = s3.Bucket(
            self, 
            "cdkExampleCloudFrontServerTimingResponseHeadersBucket"
        )

        s3deploy.BucketDeployment(
            self, 
            "cdkExampleCloudFrontServerTimingResponseHeadersDeployment",
            sources=[s3deploy.Source.asset(path.join("assets", "s3-files"))],
            destination_bucket=target_bucket
        )

        custom_response_headers_policy = cloudfront.ResponseHeadersPolicy(
            self, 
            "cdkExampleCloudFrontServerTimingResponseHeadersPolicy",
            response_headers_policy_name="cdkExampleCloudFrontServerTimingResponseHeadersPolicy",
            comment="CDK Example - Cloudfront Server Timing Response Headers",
            cors_behavior=cloudfront.ResponseHeadersCorsBehavior(
                access_control_allow_credentials=False,
                access_control_allow_headers=["*"],
                access_control_allow_methods=["GET", "POST"],
                access_control_allow_origins=["*"],
                access_control_expose_headers=["*"],
                origin_override=True
            ),
        )

        # There isn't a native way to add these headers so they
        # have to be added via this add_override() method
        custom_response_headers_policy.node.default_child.add_override('Properties.ResponseHeadersPolicyConfig.ServerTimingHeadersConfig.Enabled', True)
        custom_response_headers_policy.node.default_child.add_override('Properties.ResponseHeadersPolicyConfig.ServerTimingHeadersConfig.SamplingRate', 100)

        cloudfront.Distribution(
            self, 
            "cdkExampleCloudFrontServerTimingResponseHeadersDistribution",
            default_behavior=cloudfront.BehaviorOptions(
                response_headers_policy=custom_response_headers_policy,
                origin=origins.S3Origin(target_bucket)
            ),
            default_root_object="index.html"
        )

