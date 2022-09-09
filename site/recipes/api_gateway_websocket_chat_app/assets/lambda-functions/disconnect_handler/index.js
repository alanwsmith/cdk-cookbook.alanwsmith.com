const AWS = require('aws-sdk')
const ddb = new AWS.DynamoDB.DocumentClient()
exports.handler = async function (event, context) {
  console.log(`DISCONNECT HANDLER`)
  await ddb
    .delete({
      TableName: process.env.table,
      Key: {
        connectionId: event.requestContext.connectionId,
      },
    })
    .promise()
  return {
    statusCode: 200,
  }
}
