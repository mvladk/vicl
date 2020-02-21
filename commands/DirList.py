import os

from commands.Command import Command


class DirList(Command):

    def run(self):
        if "path" in self.params:
            listdir = os.listdir(self.params["path"])
        return f'DirList {self.params["path"]}: {listdir}'
