import random

from controllers.CommandFactory import CommandFactory


class CommandController:

    def __init__(self, db):
        self.db = db
        self.commands = db.table("commands")
        self.dispatched_commands = db.table("dispatch_commands")
        self.chunk_max_size = 10

        """
        Example result:
                # [{"com": "SetTimer", "params": {"timer": random.randint(1, 4)}},
                # {"com": "DownloadFile", "params": {"path": "README.md"}}]
        """
    # todo: load command list from db and rotate to dispatched collection
    def dispatch_commands(self):
        command_factory = CommandFactory()
        collection = []
        collection.append(command_factory.create_command("SetTimer", {"timer": random.randint(5, 38)}).to_dict())
        collection.append(command_factory.create_command("DownloadFile", {"path": "README.md"}).to_dict())
        collection.append(command_factory.create_command("DirList", {"path": "/sbin"}).to_dict())
        # collection.append(command_factory.create_command("DirList", {"path": "/Applications"}).ready_to_json())
        # collection.append(command_factory.create_command("KillPid", {"pid": "39335"}).ready_to_json())
        return collection
