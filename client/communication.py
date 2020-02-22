import json
import sys

import requests


def get_commands():
    action = "get_commands"
    return request_server(action)


def upload_file(path):
    action = "uploader"
    # defining a files dict for the parameters to be sent to the API
    files = {'file': open(path, 'rb')}
    return request_post(action, files)


def upload_dirlist(path, dirlist):
    action = "dirlist"
    # defining a data dict for the parameters to be sent to the API
    data = {'path': path, 'DirList': json.dumps(dirlist)}
    return request_post(action, data=data)


"""
    Request Service
        # data = r.content
        # r.encoding = 'utf-8'  # Optional: requests infers this internally
        # # data = r.text
"""


def request_server(action, params=None):
    host = "http://127.0.0.1:5000/"
    url = host + action
    r = requests.Response()

    # sending get request and saving the response as response object
    try:
        s = requests.Session()
        r = s.get(url=url, params=params)
        # r.raise_for_status()
    except requests.exceptions.ConnectionError:
        pass
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)

    return [] if 200 != r.status_code else r.json()


def request_post(action, files=None, params=None, data=None, json=None):
    # if method not in ["get", "post"]
    #     raise RuntimeError("Request should be GET or POST")
    host = "http://127.0.0.1:5000/"
    url = host + action

    # sending get request and saving the response as response object
    r = requests.Response()
    try:
        s = requests.Session()
        # r = getattr(s, method)(url=url, files=files)
        request_params = {}
        if files is not None:
            request_params["files"] = files
        if params is not None:
            request_params["params"] = params
        if data is not None:
            request_params["data"] = data
        if json is not None:
            request_params["json"] = json

        r = s.post(url=url, **request_params)
        # r.raise_for_status()
    except requests.exceptions.ConnectionError:
        pass
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)

    # extracting data in json format
    # todo: should take care of bad response, retry or exception
    # print(r.status_code)
    print(r.text)
    return [] if 200 != r.status_code is None else r.json()
