#!/usr/bin/env python3
import os

import aws_cdk as cdk

from make_cloudfront_request_and_response_lambda_edge_functions.make_cloudfront_request_and_response_lambda_edge_functions_stack import MakeCloudfrontRequestAndResponseLambdaEdgeFunctionsStack

app = cdk.App()
MakeCloudfrontRequestAndResponseLambdaEdgeFunctionsStack(
    app, 
    "MakeCloudfrontRequestAndResponseLambdaEdgeFunctionsStack",
    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
    #env=cdk.Environment(account='123456789012', region='us-east-1'),
    )

app.synth()
