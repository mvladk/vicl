from commands.Command import Command
from client import communication as server

"""
DownloadFile implements Command
run will upload requested file to server 
"""


class DownloadFile(Command):

    @staticmethod
    def get_required_params():
        return ['path']

    def run(self):
        # defining a files dict for the parameters to be sent to the API
        files = {'file': open(self.path, 'rb')}
        return server.request_server('uploader', 'post', files=files)
