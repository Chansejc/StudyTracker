from flask import Flask, request
import flask
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    print("Greeting our guest...")
    return "Ur mom"

@app.route('/users', methods=['GET','POST'])
def users():
    print("Women working here...")
    if request.method == "GET":
        with open("users.json",'r') as f:
            data = json.load(f)
            data.append({
                'username': 'chanse',
                'pets': ['pterodactyl']
                })
            return flask.jsonify(data)
    elif request.method == "POST":
        # Requests.get_json() we can extract the JSON data that was sent 
        # as a JSON dictionary
        received_data = request.get_json()
        print("received data: {}".format(received_data))
        # Storing the data from the 'data' key in the JSON dictionary
        message = received_data['data']
        # The response data object that will be sent back as a Response object
        # with status code 201
        return_data = {
            "status": "success",
            "message": "received: {}".format(message)
        }
        return flask.Response(response=json.dumps(return_data), status=201)
    else:
        return 'Request was not a "GET" or "POST".' 


if __name__ == "__main__":
    app.run('localhost', 5885)
