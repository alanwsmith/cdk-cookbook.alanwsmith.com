#!/usr/bin/env python3
import os

import aws_cdk as cdk

from serve_one_s3_file_to_multiple_urls_in_cloudfront_with_lambda_edge_functions.serve_one_s3_file_to_multiple_urls_in_cloudfront_with_lambda_edge_functions_stack import ServeOneS3FileToMultipleUrlsInCloudfrontWithLambdaEdgeFunctionsStack

app = cdk.App()
ServeOneS3FileToMultipleUrlsInCloudfrontWithLambdaEdgeFunctionsStack(app, "ServeOneS3FileToMultipleUrlsInCloudfrontWithLambdaEdgeFunctionsStack",
    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
    #env=cdk.Environment(account='123456789012', region='us-east-1'),
    )

app.synth()
