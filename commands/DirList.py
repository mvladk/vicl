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
        listdir = os.listdir(self.path)
        c.upload_dirlist(self.path, listdir)
        return f'DirList {self.path}: {listdir}'
