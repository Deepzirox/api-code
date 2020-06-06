import requests
import json
from sys import argv

if len(argv) != 2:
    raise Exception("Invalid arguments")

def parse_code():
    code = ""
    numbers = json.loads(requests.get("http://dfc0fa40be8a.ngrok.io/").text)['numbers']
    numbers = int(numbers) + 1
    with open(argv[1], 'r') as file:
        code = file.read()
    update = {
    f"Code{numbers}" : code,
    "numbers" : numbers
    }
    return update

requests.post("http://dfc0fa40be8a.ngrok.io/", data=json.dumps(parse_code()))