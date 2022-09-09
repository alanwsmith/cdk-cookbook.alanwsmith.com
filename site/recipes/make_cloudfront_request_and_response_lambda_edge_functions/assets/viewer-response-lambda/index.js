'use strict'

exports.handler = (event, context, callback) => {
  const request = event.Records[0].cf.request
  const request_headers = request.headers
  const response = event.Records[0].cf.response
  const response_headers = response.headers

  console.log(`--------------------`)
  console.log(`VIEWER_RESPONSE_LAMBDA`)
  console.log(`--------------------`)
  console.log(request_headers)
  console.log(`--------------------`)
  console.log(response_headers)
  console.log(`--------------------`)

  response_headers['x-cdk-viewer-request'] = [
    {
      key: 'x-cdk-viewer-request',
      value: request_headers['x-cdk-viewer-request'][0].value,
    },
  ]

  response_headers['x-cdk-origin-request'] = [
    {
      key: 'x-cdk-origin-request',
      value: request_headers['x-cdk-origin-request'][0].value,
    },
  ]

  response_headers['x-cdk-viewer-response'] = [
    {
      key: 'x-cdk-viewer-response',
      value: 'FROM_VIEWER_RESPONSE_LAMBDA',
    },
  ]

  callback(null, response)
}
