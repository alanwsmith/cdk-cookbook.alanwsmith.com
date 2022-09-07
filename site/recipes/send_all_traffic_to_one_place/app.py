#!/usr/bin/env python3
import os

import aws_cdk as cdk

from send_all_traffic_to_one_place.send_all_traffic_to_one_place_stack import SendAllTrafficToOnePlaceStack

app = cdk.App()
SendAllTrafficToOnePlaceStack(app, "SendAllTrafficToOnePlaceStack",
    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
    #env=cdk.Environment(account='123456789012', region='us-east-1'),
    )

app.synth()
