from commands.Command import Command
from client.Timer import Timer

"""
SetTimer implements Command
run will set time to wait for next communication sequence
"""


class SetTimer(Command):
    Timer = Timer()

    @staticmethod
    def get_required_params():
        return ['timer']

    def run(self):
        self.Timer.set_seconds(int(self.timer))
        return f"SetTimer to: {self.Timer.get_seconds()}"
