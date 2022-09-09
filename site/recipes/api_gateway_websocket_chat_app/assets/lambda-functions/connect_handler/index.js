const AWS = require('aws-sdk')
const ddb = new AWS.DynamoDB.DocumentClient()
exports.handler = async function (event, context) {
  console.log(`CONNECT HANDLER`)
  try {
    await ddb
      .put({
        TableName: process.env.table,
        Item: {
          connectionId: event.requestContext.connectionId,
        },
      })
      .promise()
    console.log(`data added to able`)
  } catch (err) {
    console.log(`ERROR`)
    console.log(err)
    return {
      statusCode: 500,
    }
  }
  return {
    statusCode: 200,
  }
}
