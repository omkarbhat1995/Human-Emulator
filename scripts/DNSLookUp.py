import argparse
import time
import random
import dns.resolver
import numpy
import pandas as pd
"""
Function: Reads a list of URls and then does a DNS lookup on some of them
Parameters: 
Returns: 
"""


list = []
links = []
prob = []
total = 0
parser = argparse.ArgumentParser(description="DNS Query Engine Parser")
parser.add_argument('--file', metavar='File with Domains and Prob', type=str, nargs='?', default="data/top500Domains.csv")
parser.add_argument('--time', metavar='Run time for the Engine', type=int, nargs='?', default=35)
parser.add_argument('--inttime', metavar='Max Time Interval', type=int, nargs='?', default=30)
args = parser.parse_args()
filename = args.file
run_time = args.time
try:
    df = pd.read_csv(filename)
    df.dropna(how='all')
except FileNotFoundError or IOError as e:
    print(f"Exception in opening file in DNSLookup:{e}")
record_type = ['A']  # , 'AAAA', 'MX', 'NS', 'TXT', 'SOA']

try:
    for name in df['Domain']:
        if name != '0':
            list.append(name)
    for number in df['Links']:
        number = str(number).replace(',', '')
        if int(number) != 0:
            links.append(number)
            total += int(number)
    for link in links:
        prob.append(int(link) / total)
    exit_time = time.time() + run_time
except IOError as e:
    print(f"File import error in DNSLookup:{e}")
try:
    while time.time() < exit_time:
        try:
            name = numpy.random.choice(list, replace=True,
                                       p=prob)  # get a DNS name at random but using the probabilities and then use it for the DNS Query
            for qtype in record_type:
                answer = dns.resolver.query(name, qtype, raise_on_no_answer=False)
                if answer.rrset is not None:
                    print(answer.rrset)
            r = random.uniform(1, args.inttime)
            print(f"Sleep:{r}")
            time.sleep(r)
        except Exception as e:
            print(e)
        except dns.exception.DNSException as e:
            print("Query Failed!")
    print("Shutting Down the DNS Query Engine")
except Exception as e:
    print(f"Exception in DNSLookup:{e}")