import os
from sys import platform
import random

"""
Function: Executes one of the listed commands on terminal
Parameters:
Returns:
"""


def run():
    try:
        print("Running a shell script.")
        choice = int(random.choice(range(1, 5)))
        if choice == 1:
            print("List Command")
            if platform.system() == 'Linux':
                os.system('ls -lh')
            if platform.system() == 'Windows':
                os.system('dir')
        elif choice == 2:
            print("Network Info")
            os.system('netstat -ant')
        elif choice == 3:
            print("Right a message")
            os.system('echo "proof that this machine was hacked." >> message.txt')
        elif choice == 4:
            print("Pinging Google")
            os.system('ping google.com')
        else:
            print("Add commands!")
    except Exception as e:
        print(f"Exception in shell script: {e}")


run()
