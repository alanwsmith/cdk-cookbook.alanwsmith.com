#!/usr/bin/env python3
import os

import aws_cdk as cdk

from set_cloudfront_cache_control_headers_with_lambda_edge_functions.set_cloudfront_cache_control_headers_with_lambda_edge_functions_stack import SetCloudfrontCacheControlHeadersWithLambdaEdgeFunctionsStack

app = cdk.App()
SetCloudfrontCacheControlHeadersWithLambdaEdgeFunctionsStack(app, "SetCloudfrontCacheControlHeadersWithLambdaEdgeFunctionsStack",
    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
    #env=cdk.Environment(account='123456789012', region='us-east-1'),
    )

app.synth()
