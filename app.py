from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/',methods=['POST'])
def foo():
   message = {
      'status': 200,
      'message': "Github Webhook: success!"

   response = jsonify(message)
   response.status_code = 200

   if request.headers.get('X-GitHub-Event') == PUSH_EVENT:
        api_data = json.loads(request.data)
        print api_data

   return response

if __name__ == '__main__':
    app.run()
