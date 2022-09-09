'use strict'

exports.handler = (event, context, callback) => {
  const request = event.Records[0].cf.request
  const request_headers = request.headers
  const response = event.Records[0].cf.response
  const response_headers = response.headers

  console.log(`--------------------`)
  console.log(`ORIGIN_RESPONSE_LAMBDA`)
  console.log(`--------------------`)
  console.log(request_headers)
  console.log(`--------------------`)
  console.log(response_headers)
  console.log(`--------------------`)

  response_headers['x-cdk-origin-response'] = [
    {
      key: 'x-cdk-origin-response',
      value: 'FROM_ORIGIN_RESPONSE_LAMBDA',
    },
  ]

  callback(null, response)
}
