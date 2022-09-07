#!/usr/bin/env python3
import os

import aws_cdk as cdk

from server_timing_headers.server_timing_headers_stack import ServerTimingHeadersStack

app = cdk.App()
ServerTimingHeadersStack(app, "ServerTimingHeadersStack",
    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
    #env=cdk.Environment(account='123456789012', region='us-east-1'),
    )

app.synth()
