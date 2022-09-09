#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_serve_wildcard_urls_from_a_single_source_in_cloudfront.cdk_serve_wildcard_urls_from_a_single_source_in_cloudfront_stack import CdkServeWildcardUrlsFromASingleSourceInCloudfrontStack

app = cdk.App()
CdkServeWildcardUrlsFromASingleSourceInCloudfrontStack(app, "CdkServeWildcardUrlsFromASingleSourceInCloudfrontStack",
    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
    #env=cdk.Environment(account='123456789012', region='us-east-1'),
    )

app.synth()
