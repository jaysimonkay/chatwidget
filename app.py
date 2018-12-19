from flask import Flask, render_template, request, jsonify, makeresponse, json
from flaskcors import CORS
from pusher import pusher
import simplejson

app = Flask(__name__)
cors = CORS(app)
app.config['CORSHEADERS'] = 'Content-Type'

# configure pusher object
pusher = pusher.Pusher(
    app_id='676121',
    key='3f39c7f18f8b0db75beb',
    secret='a831c0e5ff7ca7a93136',
    cluster='us2',
    ssl=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.route('/new/guest', methods=['POST'])
def guestUser():
    data = request.json
    pusher.trigger(u'general-channel', u'new-guest-details', {
        'name': data['name'],
        'email': data['email']
    })
    return json.dumps(data)


@app.route("/pusher/auth", methods=['POST'])
def pusher_authentication():
    auth = pusher.authenticate(
        channel=request.form['channel_name'], socket_id=request.form['socket_id'])
    return json.dumps(auth)


if _**name == '**_main_':
    app.run(host='0.0.0.0', port=6500, debug=True)
