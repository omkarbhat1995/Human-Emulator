# Human Emulator

A Python-based framework designed to emulate realistic user behavior and generate network noise, inspired by the MITRE Caldera human plugin.

This tool is highly valuable for Purple Teaming, SOC training, and validating intrusion detection systems (IDS) by creating legitimate baseline traffic (web browsing, DNS queries, CLI execution) that can mask or run alongside adversarial actions.

## 🚀 Features

* **Cross-Platform:** Seamlessly runs on both Linux and Windows environments.
* **Multithreaded Task Execution:** Spawns parallel processes to simulate a user actively multitasking.
* **Dynamic Web Browsing:** Uses Selenium and BeautifulSoup to search Google, click through links, manage tabs, and browse arbitrary domains dynamically.
* **Network & OS Activity:** Automates DNS resolution requests against top domains and executes standard shell commands to simulate local user interaction.
* **Highly Configurable:** Control the cadence of the emulator by adjusting task and cluster intervals.

## 🏗️ Terminology

* **Task:** A single user action (e.g., browse the web, search Google, perform a DNS lookup, spawn a shell).
* **Cluster:** A grouped batch of Tasks executed in a specific window of time.

## 📦 Installation

**Prerequisites:** Python 3.8+ and Google Chrome installed on your machine.
1. Clone the repository:
   
   `git clone [https://github.com/YourUsername/Human-Emulator.git](https://github.com/YourUsername/Human-Emulator.git)
   cd Human-Emulator`

2. Install the required dependencies:
 
` pip install -r requirements.txt`

(Note: The emulator utilizes webdriver-manager to automatically handle ChromeDriver installation based on your browser version.)


## ⚙️ Usage
The main entry point is emulator.py. You can execute it directly via Python or use the provided interactive bash script.

### Option 1: Interactive Execution (Linux/Mac)
`chmod +x emulator.sh`
`./emulator.sh`

### Option 2: Command Line Execution
`python3 emulator.py --numberoftasks 5 --numberofclusters 3 --tasktime 10 --clustertime 30`


## Parameters
--numberofclustersMaximum number of clusters to run during the session.5--tasktimeMax wait time (in seconds) between individual tasks.10--clustertimeMax wait time (in seconds) between clusters.50
| Argument | Description | Default |
|----------|----------|----------|
| --numberoftasks    | Maximum number of tasks to execute per cluster.   | 5   |
| --numberofclusters    | Maximum number of clusters to run during the session.   | 5   |
| --tasktimeMax    | Max wait time (in seconds) between individual tasks.   | 10   |
| --clustertime    | Max wait time (in seconds) between clusters   | 50   |



## 📁 Project Structure
* emulator.py: The core orchestrator managing threads and clusters.

* webdriver_helper.py: Wrapper for Selenium and ChromeDriver setup.

* /scripts/

    * browse_google.py: Generates randomized search queries and interacts with Google results.

    * browse_website.py: Navigates through a provided list of target websites (websites.txt).

    * DNSLookUp.py: Resolves domain names sequentially based on probability metrics (top500Domains.csv).

    * shell_script.py: Executes localized OS commands (e.g., ping, netstat, directory listing).

* /data/: Contains target datasets (websites.txt, top500Domains.csv) for the browsing and DNS modules.


## ⚠️ Disclaimer
This tool is designed strictly for educational purposes, authorized security testing, and defensive baseline generation.
