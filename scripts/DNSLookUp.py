import argparse
import time
import random
import dns.resolver
import numpy as np
import pandas as pd
import sys
import os

def main():
    parser = argparse.ArgumentParser(description="DNS Query Engine Parser")
    parser.add_argument('--file', metavar='File with Domains and Prob', type=str, default=os.path.join("data", "top500Domains.csv"))
    parser.add_argument('--time', metavar='Run time for the Engine', type=int, default=35)
    parser.add_argument('--inttime', metavar='Max Time Interval', type=int, default=30)
    args = parser.parse_args()

    filename = args.file
    run_time = args.time

    domain_list = []
    links = []
    prob = []
    total = 0

    try:
        df = pd.read_csv(filename)
        df.dropna(how='all', inplace=True)
    except (FileNotFoundError, IOError) as e:
        print(f"[-] Exception opening file in DNSLookup: {e}")
        print("[-] Ensure 'data/top500Domains.csv' exists. Exiting DNS task.")
        sys.exit(1)

    record_types = ['A']  # Can be expanded: ['A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA']

    try:
        for name in df['Domain']:
            if str(name) != '0':
                domain_list.append(str(name))
                
        for number in df['Links']:
            number = str(number).replace(',', '')
            if number.isdigit() and int(number) != 0:
                links.append(number)
                total += int(number)
                
        if total == 0:
            print("[-] Total links calculate to 0. Cannot compute probabilities. Exiting.")
            sys.exit(1)

        for link in links:
            prob.append(int(link) / total)
            
        exit_time = time.time() + run_time
        
    except Exception as e:
        print(f"[-] Data processing error in DNSLookup: {e}")
        sys.exit(1)

    print(f"[+] Starting DNS Query Engine for {run_time} seconds...")
    
    try:
        while time.time() < exit_time:
            try:
                # Get a DNS name at random using the calculated probabilities
                name = np.random.choice(domain_list, replace=True, p=prob)
                
                for qtype in record_types:
                    answer = dns.resolver.resolve(name, qtype, raise_on_no_answer=False)
                    if answer.rrset is not None:
                        print(f"[DNS] Resolved {name} ({qtype}): {answer.rrset}")
                        
                r = random.uniform(1, args.inttime)
                print(f"[*] Sleeping DNS Engine for {r:.2f} seconds...")
                time.sleep(r)
                
            except dns.exception.DNSException:
                print(f"[-] Query Failed for {name}")
            except Exception as e:
                print(f"[-] Unexpected inner exception: {e}")
                
        print("[+] Shutting Down the DNS Query Engine (Time expired).")
    except Exception as e:
        print(f"[-] Fatal Exception in DNSLookup: {e}")

if __name__ == "__main__":
    main()