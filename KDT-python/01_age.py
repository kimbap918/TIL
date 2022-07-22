# https://api.agify.io?name=michael

import requests

URL = 'https://api.agify.io?name=michael'
params = {
    'name': 'joonhyuk'
}

response = requests.get(URL, params=params).json()
print(response)