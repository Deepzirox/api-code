from flask import Flask, request
import json
import requests

server = Flask(__name__)
pyjson = {}
numbers = 0

@server.route('/', methods=['GET'])
def api():
    with open('data.json', 'r') as jsondata:
        pyjson = json.loads(jsondata.read())
        numbers = pyjson['numbers']
    return pyjson

@server.route('/', methods=['POST'])
def api_post():
    pyjson = json.loads(request.data.decode('utf8'))
    currentjson = json.loads(requests.get("http://dfc0fa40be8a.ngrok.io/").text)
    currentjson.update(pyjson)
    with open('data.json', 'w') as file:
        file.write(json.dumps(currentjson))
    return "Done"

if __name__ == '__main__':
    server.run(debug=True)