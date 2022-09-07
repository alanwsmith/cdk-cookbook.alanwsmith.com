from constructs import Construct
from aws_cdk import Stack
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_cloudfront as cloudfront
from aws_cdk import aws_cloudfront_origins as origins
from aws_cdk import aws_s3_deployment as s3deploy
from os import path

class ServerTimingHeadersStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        target_bucket = s3.Bucket(
            self, 
            "cdkServerTimingHeaderBucket"
        )

        s3deploy.BucketDeployment(
            self, 
            "cdkServerTimingHeaderDeployment",
            sources=[s3deploy.Source.asset(path.join("assets", "s3-files"))],
            destination_bucket=target_bucket
        )

        custom_response_headers_policy = cloudfront.ResponseHeadersPolicy(
            self, 
            "cdkServerTimingHeaderPolicy",
            response_headers_policy_name="cdkServerTimingHeaderPolicy",
            comment="CDK Example of enabling ServerTiming Headers",
        )

        custom_response_headers_policy.node.default_child.add_override('Properties.ResponseHeadersPolicyConfig.ServerTimingHeadersConfig.Enabled', True)
        custom_response_headers_policy.node.default_child.add_override('Properties.ResponseHeadersPolicyConfig.ServerTimingHeadersConfig.SamplingRate', 100)

        cloudfront.Distribution(
            self, 
            'cdkServerTimingHeaderPolicyDistribution',
            default_behavior=cloudfront.BehaviorOptions(
                response_headers_policy=custom_response_headers_policy,
                origin=origins.S3Origin(target_bucket)
            ),
            default_root_object="index.html"
        )

