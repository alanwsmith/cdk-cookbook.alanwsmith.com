from constructs import Construct
from aws_cdk import Duration 
from aws_cdk import Stack
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_cloudfront as cloudfront
from aws_cdk import aws_cloudfront_origins as origins
from aws_cdk import aws_lambda as lambda_ 
from aws_cdk import aws_s3_deployment as s3deploy
from os import path

class SetCloudfrontCacheControlHeadersWithLambdaEdgeFunctionsStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        target_bucket = s3.Bucket(
            self, 
            'cdkSetCloudfrontCacheControlHeadersWithLambdaEdgeFunctionsBucket'
        )

        s3deploy.BucketDeployment(
            self, 
            'cdkSetCloudfrontCacheControlHeadersWithLambdaEdgeFunctionsBucketDeployment',
            sources=[s3deploy.Source.asset(
                path.join("assets", "s3-files")
            )],
            destination_bucket=target_bucket
        )

        origin_response_lambda = cloudfront.experimental.EdgeFunction(
            self, 
            'cdkSetCloudfrontCacheControlHeadersWithLambdaEdgeFunctionsOriginResponseFunction',
            runtime=lambda_.Runtime.NODEJS_16_X,
            handler="index.handler",
            code=lambda_.Code.from_asset(
                path.join('assets', 'lambda-functions', 'origin-response-lambda')
            )
        )

        viewer_response_lambda = cloudfront.experimental.EdgeFunction(
            self, 
            'cdkSetCloudfrontCacheControlHeadersWithLambdaEdgeFunctionsViewerResponseFunction',
            runtime=lambda_.Runtime.NODEJS_16_X,
            handler="index.handler",
            code=lambda_.Code.from_asset(
                path.join('assets', 'lambda-functions', 'viewer-response-lambda')
            )
        )

        custom_response_headers_policy = cloudfront.ResponseHeadersPolicy(
            self, 
            'cdkSetCloudfrontCacheControlHeadersWithLambdaEdgeFunctionsPolicy',
            response_headers_policy_name="cdkSetCloudfrontCacheControlHeadersWithLambdaEdgeFunctionsPolicy",
            comment="CDK Example - Setting Orign and Viewer Cache Control Headers",
            cors_behavior=cloudfront.ResponseHeadersCorsBehavior(
                access_control_allow_credentials=False,
                access_control_allow_headers=["*"],
                access_control_allow_methods=["GET", "POST"],
                access_control_allow_origins=["*"],
                access_control_expose_headers=["*"],
                origin_override=True
            ),
        )

        cloudfront.Distribution(
            self, 
            'cdkSetCloudfrontCacheControlHeadersWithLambdaEdgeFunctionsDistribution',
            default_root_object="index.html",
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.S3Origin(target_bucket),
                response_headers_policy=custom_response_headers_policy,
                edge_lambdas=[
                    cloudfront.EdgeLambda(
                        function_version=origin_response_lambda.current_version,
                        event_type=cloudfront.LambdaEdgeEventType.ORIGIN_RESPONSE
                    ),
                    cloudfront.EdgeLambda(
                        function_version=viewer_response_lambda.current_version,
                        event_type=cloudfront.LambdaEdgeEventType.VIEWER_RESPONSE
                    )
                ]
            )
        )

