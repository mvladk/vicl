import json
import sys

import requests
HOST = "http://127.0.0.1:5000/"

def get_commands():
    action = "get_commands"
    return request_server2(action, 'get')


def upload_file(path):
    action = "uploader"
    # defining a files dict for the parameters to be sent to the API
    files = {'file': open(path, 'rb')}
    return request_server2(action, 'post', files=files)


def upload_dirlist(path, dirlist):
    action = "dirlist"
    # defining a data dict for the parameters to be sent to the API
    data = {'path': path, 'DirList': json.dumps(dirlist)}
    return request_server2(action, 'post', data=data)



"""
    Request Service
        # data = r.content
        # r.encoding = 'utf-8'  # Optional: requests infers this internally
        # # data = r.text
"""


# todo: make layer for communication of different types: http, socket
def request_server2(action, method="get", params=None, files=None, data=None):
    if method not in ["get", "post"]:
        raise RuntimeError("Request should be GET or POST")

    url = HOST + action
    # sending get request and saving the response as response object
    try:
        s = requests.Session()
        r = getattr(s, method)(url=url, params=params, files=files, data=data)
    except requests.exceptions.ConnectionError:
        pass
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    return [] if 200 != r.status_code else r.json()

