# from client.Timer import Timer
# from client import communication as c
# from commands.Command import Command
import commands

# class SetTimer(Command):
#     def run(self):
#         if "timer" in self.params:
#             Timer.set_seconds(int(self.params["timer"]))
#         return Timer.get_seconds()


# class DownloadFile(Command):
#     def run(self):
#         print(self.params)
#         if "path" in self.params:
#             c.upload_file(self.params["path"])
#         return "Jaja"
from commands.Command import Command
from commands.DirList import DirList
from commands.DownloadFile import DownloadFile
from commands.SetTimer import SetTimer

class KillPid(Command):
    result = "pid"

class CommandFactory:
    def create_command(self, com, params):
        com_obj = Command()
        allowed_commands = ["DirList", "DownloadFile", "SetTimer", "KillPid"]
        if com in allowed_commands:
            com_obj = globals()[com](params)
        return com_obj
