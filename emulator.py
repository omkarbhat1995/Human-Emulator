import argparse
import os
import random
import time
from threading import Thread
from sys import platform

task_handling = []

parser = argparse.ArgumentParser(description="Server parser")
parser.add_argument('--numberoftasks', metavar='Max number of tasks per clusters', type=int, nargs='?', default=5)
parser.add_argument('--numberofclusters', metavar='Total number of Clusters', type=int, nargs='?', default=5)
parser.add_argument('--tasktime', metavar='Max time between tasks', type=int, nargs='?', default=10)
parser.add_argument('--clustertime', metavar='Max time between clusters', type=int, nargs='?', default=50)
args = parser.parse_args()

"""
Function : Emulator to emulate a human using google browse, browse websites , DNS look up and Shell script.
Parameters :
Returns : 
"""


def emulation():
    try:
        print(f"{platform.system()}")
        #if platform.system() == 'Linux':
        Numberofclusters = random.choice(range(args.numberofclusters + 1))
        print(f"Clusters : {Numberofclusters}")
        for i in range(Numberofclusters + 1):
            print(f"Cluster:{i}")
            task_manager(args.tasktime)
            time.sleep(random.choice(range(args.clustertime + 1)))
    except Exception as e:
        print(f"Exception in emulation:{e}")


# noinspection PyInterpreter,PyInterpreter
def task_manager(tasktime):
    number_of_tasks = 4  # random.choice(range(3,args.numberoftasks + 1))
    print(f"Tasks : {number_of_tasks}")
    if number_of_tasks >= 4:
        if platform.system() == 'Linux':
            t = Thread(target=start_dns_lookup_linux())
            task_handling.append(t)
            t1 = Thread(target=start_terminal_linux())
            task_handling.append(t1)
            t2 = Thread(target=start_browsing_google_linux())
            task_handling.append(t2)
            t3 = Thread(target=start_browsing_websites_linux())
            task_handling.append(t3)
            number_of_tasks = number_of_tasks - 4
            t.start()
            t1.start()
            t2.start()
            t3.start()
        if platform.system()=='Windows':
            t = Thread(target=start_dns_lookup_windows())
            task_handling.append(t)
            t1 = Thread(target=start_terminal_windows())
            task_handling.append(t1)
            t2 = Thread(target=start_browsing_google_windows())
            task_handling.append(t2)
            t3 = Thread(target=start_browsing_websites_windows())
            task_handling.append(t3)
            number_of_tasks = number_of_tasks - 4
            t.start()
            t1.start()
            t2.start()
            t3.start()

    for i in range(number_of_tasks + 1):
        # noinspection PyInterpreter
        choice = int(random.choice(range(1, 4)))
        if choice == 1:
            if platform.system() == 'Linux':
                t = Thread(target=start_terminal_linux())
            if platform.system() == 'Windows':
                t= Thread(target = start_terminal_windows())
            task_handling.append(t)
            t.start()
        elif choice == 2:
            if platform.system()=='Linux':
                t = Thread(target=start_dns_lookup_linux())
            if platform.system() == 'Windows':
                t=Thread(target=start_dns_lookup_windows())
            task_handling.append(t)
            t.start()
        elif choice == 3:
            if platform.system() == 'Linux':
                t = Thread(target=start_browsing_websites_linux())
            if platform.system() == 'Windows':
                t= Thread(target=start_browsing_websites_windows())
            task_handling.append(t)
            t.start()
        elif choice == 4:
            if platform.system() == 'Linux':
                t = Thread(target=start_browsing_google_linux())
            if platform.system() == '':
                t=Thread(target=start_browsing_google_windows())
            task_handling.append(t)
            t.start()
        else:
            print("Need to add more tasks")
    time.sleep(random.choice(range(tasktime + 1)))
    for thread in task_handling:
        thread.join()
    return


def start_browsing_google_linux():
    print("Starting the Google Browsing")
    os.system('nohup xterm -e python3 scripts/browse_google.py &')


def start_browsing_google_windows():
    print("Starting the Google Browsing")
    os.system(r'start cmd.exe /c python3 scripts\browse_google.py')



def start_browsing_websites_linux():
    print("Starting the Website Browsing")
    os.system('nohup xterm -e python3 scripts/browse_website.py &')


def start_browsing_websites_windows():
    print("Starting the Website Browsing")
    os.system(r'start cmd.exe /c python3 scripts\browse_website.py')


def start_dns_lookup_linux():
    print("Starting the DNS Lookup")
    os.system('nohup xterm -e python3 scripts/DNSLookUp.py &')


def start_dns_lookup_windows():
    print("Starting the DNS Lookup")
    os.system(r'start cmd.exe /c python3 scripts\DNSLookUp.py')


def start_terminal_linux():
    print(f"Starting a Linux terminal")
    os.system('nohup xterm -e python3 scripts/shell_script.py &')


def start_terminal_windows():
    print("Starting a Windows Command")
    os.system(r'start cmd.exe /c python3 scripts\shell_script.py')


emulation()
