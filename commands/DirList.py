import json
import os

from commands.Command import Command
from client import communication as c

"""
DirList implements Command
run will return os dir command output and upload to server 
"""


class DirList(Command):

    @staticmethod
    def get_required_params():
        return ['path']

    def run(self):
        dirlist = os.listdir(self.path)

        # defining a data dict for the parameters to be sent to the API
        data = {'path': self.path, 'DirList': json.dumps(dirlist)}
        return c.request_server('dirlist', 'post', data=data)

