exports.handler = async (event) => {
  console.log(`WEB PAGE`)
  const response = {
    isBase64Encoded: false,
    statusCode: 200,
    body: `<!DOCTYPE html>
  <html>
    <head>
      <style>
        body {
          background-color: #333;
          color: #eee;
        }
      </style>
      <script>
        addEventListener('DOMContentLoaded', (event) => {
          const socket = new WebSocket(
            '${process.env.websocket_endpoint}'
          )
          socket.addEventListener('message', (event) => {
            // console.log(event)
            const message_text = JSON.parse(event.data).message
            const connection_id = JSON.parse(event.data).connectionId
            // console.log(message_text)
            const newLi = document.createElement('li')
            newLi.innerHTML = connection_id
            newLi.innerHTML += '<br />'
            newLi.innerHTML += message_text
            const theUl = document.getElementById('the_messages')
            theUl.appendChild(newLi)
          })
          document
            .getElementById('submitter')
            .addEventListener('click', (event) => {
              const message_text = document.getElementById('message').value
              const payload = JSON.stringify({
                action: 'sendmessage',
                message: JSON.stringify({ message: message_text }),
              })
              socket.send(payload)
            })
        })
      </script>
    </head>
    <body>
      <div>
        <div>
          <label for="message">Message: </label>
          <input type="text" id="message" name="themessage" />
          <button id="submitter">Send</button>
        </div>
        <ul id="the_messages"></ul>
      </div>
    </body>
  </html>
  `,
    headers: {
      'content-type': 'text/html',
    },
  }
  return response
}
