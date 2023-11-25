from flask import Flask
import flask
import json
app = Flask(__name__)

@app.route('/')
def home():
    return "Ur Mom"

@app.route('/users', methods=["GET"])
def users():
    print("Sending User Data...")
    with open("users.json",'r') as f:
        data = json.load(f)
        return flask.jsonify(data)

if __name__ == "__main__":
    app.run("localhost", 5885)
