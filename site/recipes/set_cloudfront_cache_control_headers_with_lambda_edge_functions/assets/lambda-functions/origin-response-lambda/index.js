'use strict'

exports.handler = (event, context, callback) => {
  const response = event.Records[0].cf.response
  const response_headers = response.headers

  response_headers['cache-control'] = [
    {
      key: 'cache-control',
      value: 'max-age=5000',
    },
  ]

  callback(null, response)
}
