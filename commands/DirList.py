import os

from commands.Command import Command


class DirList(Command):
    arr = os.listdir("/Applications")
    result = "dir"
