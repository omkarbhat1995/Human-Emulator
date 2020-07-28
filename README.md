# Human-Emulator
Inspired from MITRE human plugin.

Install requirements using requirements.txt. The human.py uses the aforementioned codes to emulate user actions based on 3 parameters.
1. Clustersize: Max Number of clusters in the operations.
2. Tasksize: Max Number of tasks in a cluster
3. TaskInterval: Max Time in seconds before next tasks is executed.
4. Clusterinterval: Max Time in seconds before next cluster is started.

Terminology:
 - Tasks: A User-action (eg. browse web, serach web, spawn shell)
 - Cluster: A group of User Actions
 
 Execution:
 
 Execute the `pyhuman.py` file as shown below to emulate a human. The tasks are parallel in behaviour.
 
