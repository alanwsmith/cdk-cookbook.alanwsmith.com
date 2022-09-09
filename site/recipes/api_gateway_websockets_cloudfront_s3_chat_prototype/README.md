This sets up a working chat prototype
with an S3 web page served from cloudfront
and connected with api gateway web sockets

NOTE That you have to install:

pip install aws-cdk.aws-apigatewayv2-alpha

and

pip install aws-cdk.aws-apigatewayv2-integrations-alpha

---

Setting this up so that it uses the HTTPAPI
(in addition to the websocket api)
for serving the HTML file. Another alternative
is to spin up cloud front and/or serve
from S3. Examples of those are forthcoming.

---

TODO: Remove Cloudfront and S3 refrence since
this is all done over the api gateway now.
