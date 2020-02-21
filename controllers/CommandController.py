import random
from controllers.CommandFactory import CommandFactory


class CommandController:
    """
    Example result:
            # [{"com": "SetTimer", "params": {"timer": random.randint(1, 4)}},
            # {"com": "DownloadFile", "params": {"path": "README.md"}}]
    """
    def get_collection(self):
        command_factory = CommandFactory()
        collection = []
        collection.append(command_factory.create_command("SetTimer", {"timer": random.randint(3, 8)}).ready_to_json())
        # collection.append(command_factory.create_command("DownloadFile", {"path": "README.md"}).ready_to_json())
        collection.append(command_factory.create_command("DirList", {"path": "/sbin"}).ready_to_json())
        # collection.append(command_factory.create_command("DirList", {"path": "/Applications"}).ready_to_json())
        return collection
