from constructs import Construct
from aws_cdk import Duration 
from aws_cdk import Stack
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_cloudfront as cloudfront
from aws_cdk import aws_cloudfront_origins as origins
from aws_cdk import aws_lambda as lambda_ 
from aws_cdk import aws_s3_deployment as s3deploy
from os import path


class MakeCloudfrontRequestAndResponseLambdaEdgeFunctionsStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        target_bucket = s3.Bucket(
            self, 
            'cdkMakeCloudfrontRequestAndResponseLambdaEdgeFunctionsBucket'
        )

        s3deploy.BucketDeployment(
            self, 
            'cdkMakeCloudfrontRequestAndResponseLambdaEdgeFunctionsDeployment',
            sources=[s3deploy.Source.asset(
                path.join("assets", "s3-files")
            )],
            destination_bucket=target_bucket
        )

        viewer_request_lambda = cloudfront.experimental.EdgeFunction(
            self, 
            'cdkMakeCloudfrontRequestAndResponseLambdaEdgeFunctionsViewerRequest',
            runtime=lambda_.Runtime.NODEJS_16_X,
            handler="index.handler",
            code=lambda_.Code.from_asset(
                path.join('assets', 'viewer-request-lambda')
            )
        )

        viewer_response_lambda = cloudfront.experimental.EdgeFunction(
            self, 
            'cdkMakeCloudfrontRequestAndResponseLambdaEdgeFunctionsViewerResponse',
            runtime=lambda_.Runtime.NODEJS_16_X,
            handler="index.handler",
            code=lambda_.Code.from_asset(
                path.join('assets', 'viewer-response-lambda')
            )
        )

        origin_request_lambda = cloudfront.experimental.EdgeFunction(
            self, 
            'cdkMakeCloudfrontRequestAndResponseLambdaEdgeFunctionsOriginRequest',
            runtime=lambda_.Runtime.NODEJS_16_X,
            handler="index.handler",
            code=lambda_.Code.from_asset(
                path.join('assets', 'origin-request-lambda')
            )
        )

        origin_response_lambda = cloudfront.experimental.EdgeFunction(
            self, 
            'cdkMakeCloudfrontRequestAndResponseLambdaEdgeFunctionsOriginResponse',
            runtime=lambda_.Runtime.NODEJS_16_X,
            handler="index.handler",
            code=lambda_.Code.from_asset(
                path.join('assets', 'origin-response-lambda')
            )
        )

        cloudfront.Distribution(
            self, 
            'cdkMakeCloudfrontRequestAndResponseLambdaEdgeFunctionsStack',
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.S3Origin(target_bucket),
                edge_lambdas=[
                    cloudfront.EdgeLambda(
                        function_version=viewer_request_lambda.current_version,
                        event_type=cloudfront.LambdaEdgeEventType.VIEWER_REQUEST
                    ),
                    cloudfront.EdgeLambda(
                        function_version=origin_request_lambda.current_version,
                        event_type=cloudfront.LambdaEdgeEventType.ORIGIN_REQUEST
                    ),
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

