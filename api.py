#! /usr/bin/python3

import requests
import json

baseURL = 'https://jsonplaceholder.typicode.com/'

HEADERS = {'Content-Type': 'application/json',
           'Accept': 'application/json'}


def get(path, params = None):
    """GET from path"""

    if params:
        response = requests.get(baseURL + path + str(params))
    else:
        response = requests.get(baseURL + path)
    
    response.raise_for_status()

    return response.text


def put(path, payload):
    """Put data to path"""

    response = requests.put(baseURL + path,
                            data = json.dumps(payload),
                            headers = HEADERS)

    print('Status Code: %s\n' % (response.status_code))

    return response.json()

def patch(path, payload):
    """Put data to path"""

    response = requests.patch(baseURL + path,
                            data = json.dumps(payload),
                            headers = HEADERS)

    print('Status Code: %s\n' % (response.status_code))

    return response.json()

def post(environment, user, password, path, payload):
    """Post data to path"""

    response = requests.post(baseURL[environment] + path,
                             data = json.dumps(payload),
                             auth = (user, password),
                             headers = HEADERS)

    response.raise_for_status()

    return response.json()

def change(elementName, newElementValue):
    """Change element value"""

    element = dict([(elementName, user[elementName])])
    print('\nOld: %s' % (element))
    element[elementName] = newElementValue
    print('New: %s\n' % (element)) 

    return element   

if __name__ == "__main__":

    user_id = 7
    newPhone = '101-101-101'
    newName = 'NicestMan InMedia'

    res = get('users/', user_id)
    user = json.loads(res)

    phone = change('phone', newPhone)

    patch('users/' + str(user_id), phone)