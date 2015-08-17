from flask import Flask, request, jsonify
import json
import hmac
from hashlib import sha1

app = Flask(__name__)


@app.route('/', methods=['POST'])
def foo():
    sha_name, signature = request.headers.get('X-Hub-Signature').split('=')
    if sha_name != 'sha1':
        print "sha name doesnt equal sha1"

    mac = hmac.new(str('secret'), msg=request.data, digestmod=sha1)

    if (hmac.compare_digest(str(mac.hexdigest()), str('secret')) and
            request.headers.get('X-GitHub-Event') == u'push'):

        api_data = json.loads(request.data)
        print api_data
        print 'SECRET WAS A SUCCESS!'

        success_message = {
            'status': 200,
            'message': "Github Webhook: success!"
        }

        response = jsonify(success_message)
        response.status_code = 200

        return response
    else:
        failure_message = {
            'status': 400,
            'message': "Github Webhook: failed!"
        }

        response = jsonify(failure_message)
        response.status_code = 400

if __name__ == '__main__':
    app.run()
