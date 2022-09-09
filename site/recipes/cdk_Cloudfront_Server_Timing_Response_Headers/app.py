#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_cloudfront_server_timing_response_headers.cdk_cloudfront_server_timing_response_headers_stack import CdkCloudfrontServerTimingResponseHeadersStack

app = cdk.App()
CdkCloudfrontServerTimingResponseHeadersStack(app, "CdkCloudfrontServerTimingResponseHeadersStack",
    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
    #env=cdk.Environment(account='123456789012', region='us-east-1'),
    )

app.synth()
