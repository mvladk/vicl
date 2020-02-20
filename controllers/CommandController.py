import random
from controllers.CommandFactory import CommandFactory


class CommandController:

    def get_collection(self):
        command_factory = CommandFactory()

        return [
            command_factory.create_command("SetTimer", {"timer": random.randint(1, 4)}).ready_to_json(),
            command_factory.create_command("DownloadFile", {"path": "README.md"}).ready_to_json()
            # {"com": "SetTimer", "params": {"timer": random.randint(1, 4)}},
            # {"com": "DownloadFile", "params": {"path": "Car.py"}}
        ]
