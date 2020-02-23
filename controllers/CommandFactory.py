from commands.Command import Command
from commands.DirList import DirList
from commands.DownloadFile import DownloadFile
from commands.KillPid import KillPid
from commands.SetTimer import SetTimer


class CommandFactory:
    @staticmethod
    def create_command(com, params):
        com_obj = Command(params)
        allowed_commands = ["DirList", "DownloadFile", "SetTimer", "KillPid"]
        if com in allowed_commands:
            com_obj = globals()[com](params)
        return com_obj
