import requests
import json
from sys import argv

if len(argv) != 3:
    raise Exception("Invalid arguments")

def parse_code():
    code = ""
    numbers = json.loads(requests.get(argv[1]).text)['numbers']
    numbers = int(numbers) + 1
    with open(argv[2], 'r') as file:
        code = file.read()
    update = {
    f"Code{numbers}" : code,
    "numbers" : numbers
    }
    return update

requests.post("http://dfc0fa40be8a.ngrok.io/", data=json.dumps(parse_code()))