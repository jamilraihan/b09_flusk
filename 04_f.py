import json
from flask import Flask, request, jsonify
from my_class import info
aa = info()


app = Flask(__name__)

"""server gets the info when client send info to the server"""
@app.route("/post_info/", methods=['POST'])
def post_data():
    if request.method == 'POST':
        data = json.loads(request.data.decode('utf-8'))
        print(data['file'])
        aa.get(int(data['file']))
        return "okk"

app.run()