import sys

import requests


def get_commands():
    action = "get_commands"

    # location given here
    x = "x"
    location = f"Lida {x}"

    # defining a params dict for the parameters to be sent to the API
    params = {'name': location}
    return request_server(action, params)


def upload_file(path):
    action = "uploader"
    # defining a params dict for the parameters to be sent to the API
    files = {'file': open(path, 'rb')}
    return request_post(action, files)


"""
    Request Service
        # data = r.content
        # r.encoding = 'utf-8'  # Optional: requests infers this internally
        # # data = r.text
"""


def request_server(action, params):
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

    # print(url)
    # print(r)
    # extracting data in json format
    # print(r.status_code)
    return [] if 200 != r.status_code else r.json()


def request_post(action, files):
    host = "http://127.0.0.1:5000/"
    url = host + action

    # sending get request and saving the response as response object
    r = requests.Response()
    try:
        s = requests.Session()
        r = s.post(url=url, files=files)
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
