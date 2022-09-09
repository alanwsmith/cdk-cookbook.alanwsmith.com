#!/usr/bin/env python3
import os

import aws_cdk as cdk

from api_gateway_websocket_chat_app.api_gateway_websocket_chat_app_stack import ApiGatewayWebsocketChatAppStack

app = cdk.App()
ApiGatewayWebsocketChatAppStack(app, "CDKApiGatewayWebsocketChatAppStack",
    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
    #env=cdk.Environment(account='123456789012', region='us-east-1'),
    )

app.synth()
