const AWS = require('aws-sdk')
const ddb = new AWS.DynamoDB.DocumentClient()

exports.handler = async function (event, context) {
  let connections
  try {
    connections = await ddb.scan({ TableName: process.env.table }).promise()
  } catch (err) {
    return {
      statusCode: 500,
    }
  }
  const callbackAPI = new AWS.ApiGatewayManagementApi({
    apiVersion: '2018-11-29',
    endpoint:
      event.requestContext.domainName + '/' + event.requestContext.stage,
  })

  const message = JSON.parse(event.body).message
  const messageJSON = JSON.parse(message)

  const sendMessages = connections.Items.map(async ({ connectionId }) => {
    messageJSON.connectionId = connectionId
    try {
      await callbackAPI
        .postToConnection({
          ConnectionId: connectionId,
          Data: JSON.stringify(messageJSON),
        })
        .promise()
    } catch (e) {
      console.log(e)
    }
  })

  try {
    await Promise.all(sendMessages)
  } catch (e) {
    console.log(e)
    return {
      statusCode: 500,
    }
  }

  return { statusCode: 200 }
}
