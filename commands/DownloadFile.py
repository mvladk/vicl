from commands.Command import Command
from client import communication as c

"""
DownloadFile implements Command
run will upload requested file to server 
"""


class DownloadFile(Command):

    @staticmethod
    def get_required_params():
        return ['path']

    def run(self):
        c.upload_file(self.path)
        return f'DownloadFile complete: {self.path}'
