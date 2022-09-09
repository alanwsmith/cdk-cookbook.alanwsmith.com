exports.handler = async (event) => {
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
            socket.addEventListener('open', (event) => {
              console.log('Websocket open')
            })
            socket.addEventListener('message', (event) => {
              const message_text = JSON.parse(event.data).message
              const username = JSON.parse(event.data).username
              const newLi = document.createElement('li')
              newLi.innerHTML = username
              newLi.innerHTML += '<br />'
              newLi.innerHTML += message_text
              const theUl = document.getElementById('the_messages')
              theUl.appendChild(newLi)
            })
            document
              .getElementById('main_form')
              .addEventListener('submit', (event) => {
                event.preventDefault()
                const message_text = document.getElementById('message').value
                const username = document.getElementById('username').value
                if(message_text !== '' && username !== '') {
                  document.getElementById('message').value = ''
                  const payload = JSON.stringify({
                    action: 'send_message',
                    message: JSON.stringify({ message: message_text, username: username }),
                  })
                  socket.send(payload)
                }
              })
          })
        </script>
      </head>
      <body>
        <div>
          <div>
            <p>[Note: It can take a couple minutes for the api to come <br />
            online after the 'cdk deploy' process completes. If the<br />
            form doesn't work, give it a little time then try again.]</p>
            <form id="main_form">
              <label for="username">Name: </label>
              <input type="text" id="username" name="the_username" /><br />
              <label for="message">Message: </label>
              <input type="text" id="message" name="the_message" />
              <input type="submit" id="submitter" name="Send" value="Send" />
            </form>
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
