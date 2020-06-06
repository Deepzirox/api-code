import json
import requests
import sys

if len(sys.argv) != 4:
    raise Exception('Invalid arguments')

def petition():
    pyjson = {}
    pyjson = json.loads(requests.get(sys.argv[1]).text)
    return pyjson

def create_file():
    with open(sys.argv[2], 'w+') as writefile:
        writefile.write(petition()[f'Code{sys.argv[3]}'])

create_file()
