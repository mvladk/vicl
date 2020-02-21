from commands.Command import Command
from client.Timer import Timer


class SetTimer(Command):
    Timer = Timer()

    def run(self):
        if "timer" in self.params:
            self.Timer.set_seconds(int(self.params["timer"]))
        return f"SetTimer to: {self.Timer.get_seconds()}"
