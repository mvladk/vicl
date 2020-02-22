import os
import signal

from commands.Command import Command

"""
KillPid implements Command
run will kill process by pid (process id)
"""


class KillPid(Command):

    @staticmethod
    def get_required_params():
        return ['pid']

    def run(self):
        return os.kill(int(self.pid), signal.SIGTERM)
