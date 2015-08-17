from flask import Flask, request, jsonify
import json
import hmac
from hashlib import sha1

app = Flask(__name__)


@app.route('/', methods=['POST'])
def foo():
    print "testing the webhook"

    sha_name, signature = request.headers.get('X-Hub-Signature').split('=')

    print signature

    if sha_name != 'sha1':
        print "sha name doesnt equal sha1"

    print 'got past sha1'

    mac = hmac.new(str('secret'), msg=request.data, digestmod=sha1)

    print 'got pass mac setting'

    print mac.hexdigest()

    print 'before the hmac conditional'

    print ('Push Event: {}'
           .format(request.headers.get('X-GitHub-Event') == u'push'))

    print ('Hex Comparison: {}'
           .format(hmac.compare_digest(str(mac.hexdigest()), str(signature))))

    if (hmac.compare_digest(str(mac.hexdigest()), str(signature)) and
            request.headers.get('X-GitHub-Event') == u'push'):

        print 'Got past the hexdigest and push event conditional'

        api_data = json.loads(request.data)
        print api_data
        print 'SECRET WAS A SUCCESS!'

        print 'got past json.loads(request.data)'

        success_message = {
            'status': 200,
            'message': "Github Webhook: success!"
        }

        print 'setting response'

        response = jsonify(success_message)
        response.status_code = 200
    else:
        failure_message = {
            'status': 400,
            'message': "Github Webhook: failed!"
        }

        print 'In the failure section'

        response = jsonify(failure_message)
        response.status_code = 400

    print response
    return response

if __name__ == '__main__':
    app.run()
