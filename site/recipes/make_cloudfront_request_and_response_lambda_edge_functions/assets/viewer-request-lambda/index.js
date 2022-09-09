'use strict'

exports.handler = (event, context, callback) => {
  const request = event.Records[0].cf.request
  const request_headers = request.headers
  const response = event.Records[0].cf.response
  const response_headers = response.headers

  console.log(`--------------------`)
  console.log(`VIEWER_REQUEST_LAMBDA`)
  console.log(`--------------------`)
  console.log(request_headers)
  console.log(`--------------------`)
  console.log(response_headers)
  console.log(`--------------------`)

  request_headers['x-cdk-viewer-request'] = [
    {
      key: 'x-cdk-viewer-request',
      value: 'FROM_VIEWER_REQUEST_LAMBDA',
    },
  ]

  callback(null, request)
}
