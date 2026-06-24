import argparse
import os
import random
import time
import subprocess
import platform
from threading import Thread

def parse_arguments():
    parser = argparse.ArgumentParser(description="Human Emulator Orchestrator")
    parser.add_argument('--numberoftasks', metavar='Max tasks per cluster', type=int, default=5)
    parser.add_argument('--numberofclusters', metavar='Total Clusters', type=int, default=5)
    parser.add_argument('--tasktime', metavar='Max time between tasks (s)', type=int, default=10)
    parser.add_argument('--clustertime', metavar='Max time between clusters (s)', type=int, default=50)
    return parser.parse_args()

def get_script_command(script_name):
    """Returns the correct subprocess command based on the operating system."""
    current_os = platform.system()
    script_path = os.path.join("scripts", script_name)
    
    if current_os == 'Linux':
        return ['nohup', 'xterm', '-e', 'python3', script_path]
    elif current_os == 'Windows':
        return ['cmd.exe', '/c', 'start', 'python3', script_path]
    else:
        raise OSError(f"Unsupported OS: {current_os}")

def run_task(script_name):
    """Spawns a subprocess for a specific task."""
    print(f"Starting Task: {script_name}")
    try:
        cmd = get_script_command(script_name)
        # Using subprocess.Popen for non-blocking execution instead of os.system
        subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"Failed to start {script_name}: {e}")

def task_manager(args):
    """Manages the execution of tasks within a single cluster."""
    # Ensure at least 1 task, up to the maximum specified
    num_tasks = random.randint(1, args.numberoftasks)
    print(f"  [+] Executing {num_tasks} tasks in this cluster.")
    
    available_scripts = [
        "shell_script.py",
        "DNSLookUp.py",
        "browse_website.py",
        "browse_google.py"
    ]
    
    active_threads = []
    
    for _ in range(num_tasks):
        chosen_script = random.choice(available_scripts)
        t = Thread(target=run_task, args=(chosen_script,))
        active_threads.append(t)
        t.start()

    # Wait for the next task interval before joining
    time.sleep(random.randint(0, args.tasktime))
    
    for thread in active_threads:
        thread.join()

def emulation(args):
    """Main emulation loop managing clusters."""
    try:
        num_clusters = random.randint(1, args.numberofclusters)
        print(f"Starting Emulation: {num_clusters} Clusters scheduled.\n" + "-"*40)
        
        for i in range(1, num_clusters + 1):
            print(f"\n[Cluster {i}/{num_clusters}]")
            task_manager(args)
            
            if i < num_clusters:
                sleep_time = random.randint(0, args.clustertime)
                print(f"  [*] Cluster complete. Sleeping for {sleep_time} seconds...")
                time.sleep(sleep_time)
                
        print("\nEmulation successfully completed.")
    except Exception as e:
        print(f"Critical exception in emulation: {e}")

if __name__ == "__main__":
    arguments = parse_arguments()
    emulation(arguments)