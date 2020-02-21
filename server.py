import os

from flask import Flask, escape, request
from werkzeug.utils import secure_filename
import json
import time
from tinydb import TinyDB, Query

from controllers.CommandController import CommandController

UPLOAD_FOLDER = '/Users/michael/Downloads/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'py'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
db = TinyDB('db.json')


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


@app.route('/get_commands')
def get_commands():
    cc = CommandController()
    a = cc.get_collection()
    return json.dumps(a)


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename) + "." + str(time.time())
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return json.dumps({"message": 'file uploaded successfully'})


@app.route('/dirlist', methods=['GET', 'POST'])
def dir_list():
    if request.method == 'POST':
        path = request.values.get('path')
        data = request.values.get('DirList')
        print(path)
        print(data)
        db.insert({'command': 'DirList', 'client_id': 777, 'path': path, 'data': data, 'time': time.time()})
        return json.dumps({"message": 'dirlist saved successfully'})


if __name__ == '__main__':
    app.run()
