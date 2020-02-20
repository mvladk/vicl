from commands.Command import Command
from client.Timer import Timer


class SetTimer(Command):
    def run(self):
        if "timer" in self.params:
            Timer.set_seconds(int(self.params["timer"]))
        return f"SetTimer to: {Timer.get_seconds()}"
