import requests

HOST = "http://127.0.0.1:5000/"


"""
    Request Service
        # data = r.content
        # r.encoding = 'utf-8'  # Optional: requests infers this internally
        # # data = r.text
"""


# todo: make layer for communication of different types: http, socket
def request_server(action, method="get", params=None, files=None, data=None):
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
    return [] if 200 != r.status_code else r.json()
