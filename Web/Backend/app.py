#Working on figuring out how to redirect a user after their entry has been added to 
#the database.
#Also another problem is what happens when a user forgets their username. Should there
#be user authentication first to ensure that they won't leave infinite sessions running?

import sys, os
sys.path.append(os.getcwd() + '/..')
from flask import Flask, jsonify, request
import flask
from flask_cors import CORS
import json
import others

DATABASETables = {
        'Records': others.RecordsDatabase("./Databases/Records", 'all_records'),
        }

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Ur Mom"

@app.route('/logStart', methods=["POST"])
    # Requests.get_json() we can extract the JSON data that was sent as a JSON dictionary
    # Storing the data from the 'data' key in the JSON dictionary
    # The response data object that will be sent back as a Response object with status code 201
def logStart():
    received_data = request.get_json()
    dataList = [i.strip(' ') for i in received_data['data'].strip('[]').split(',')]
    print(dataList)
    username = dataList[0] 
    topic = dataList[1]
    DATABASETables['Records'].send_start_entry('all_records',[username, topic])

    print("Creating a session for:\nUsername: {0}\nTopic: {1}".format(username, topic))

    message = received_data['data']
    return_data = {
            'Status': 'Successful',
            'data': message
            }
    return flask.Response(response=json.dumps(return_data), status=201)

@app.route('/logEnd', methods=['POST'])
def logEnd():
    received_data = request.get_json()
    username = received_data['username']
    try:
        DATABASETables['Records'].send_end_entry('all_records', username)
        print("End of Session entry sent for {}".format(username))
        return flask.Response(response=json.dumps(username), status=201)
    except TypeError:
        print("Username: {} has no current session".format(username))
        return flask.Response(response=json.dumps(jsonify({'error':f'Username {username} has no current session'})),status=415)

@app.route('/sendEndUsername', methods=['POST'])
def getInfo():
    data = request.data
    username = str(data)[1:].strip("'{}'").split(':')[1].strip('""')
    sessionLength = DATABASETables['Records'].getRecentSessionLength(username)
    toSend = sessionLength
    print(toSend[0])
    with open('currentUser.json', 'w') as f:
        json.dump({'data': toSend[0]},f)
    return flask.Response(response=json.dumps('Resolved'),status=201)

@app.route('/getEndInfo')
def getEndInfo():
    with open('currentUser.json', 'r') as f:
        data = json.load(f)
    return data


if __name__ == "__main__":
    app.run("localhost", 5885)
