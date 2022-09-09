#/usr/bin/env python3
import os

import aws_cdk as cdk

from api_gateway_websockets_cloudfront_s3_chat_prototype.api_gateway_websockets_cloudfront_s3_chat_prototype_stack import ApiGatewayWebsocketsCloudfrontS3ChatPrototypeStack

app = cdk.App()
ApiGatewayWebsocketsCloudfrontS3ChatPrototypeStack(app, "ApiGatewayWebsocketsCloudfrontS3ChatPrototypeStack",
    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
    #env=cdk.Environment(account='123456789012', region='us-east-1'),
    )

app.synth()
