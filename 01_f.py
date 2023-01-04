import json
from flask import Flask, request, jsonify

app = Flask(__name__)

"""server gets the info when client send info to the server"""
@app.route("/post_info/", methods=['POST'])
def post_data():
    if request.method == 'POST':
        data = json.loads(request.data.decode('utf-8'))
        print(data['file'])
        return "okk"

"""client get info from this server when client ask for info from the server"""
@app.route("/get_info/", methods=['GET'])
def get_data():
    if request.method == 'GET':
        data = jsonify({
            "name": "RAIHAN" 
            })
        return data

app.run()