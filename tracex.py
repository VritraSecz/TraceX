#!/bin/python3

import argparse
import requests
import json
from colorama import Fore, Style

GREEN = Fore.LIGHTGREEN_EX
WHITE = Fore.LIGHTWHITE_EX

# Parse command line arguments
parser = argparse.ArgumentParser(description='Get IP address information.')
parser.add_argument('-i', '--ip', type=str, required=True, help='IP address')
parser.add_argument('-o', '--output', type=str, help='Output file name')
args = parser.parse_args()

def run():
    print()

# Make API request
url = f"http://ip-api.com/json/{args.ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query"
res = requests.get(url)
data = json.loads(res.text)

# Print banner
print(f"""{GREEN}
   _______  ____         ___  __
  /  _/ _ \/ _(_)__  ___/ / |/_/
 _/ // ___/ _/ / _ \/ _  />  <  
/___/_/  /_//_/_//_/\_,_/_/|_|  
<═-----=[{WHITE}By VritraSecz{GREEN}]=-----═>                            
""")

# Print the key-value pairs to the console
for key, value in data.items():
    print(f"{GREEN}► {key}:{WHITE} {value}")

# Save the output to a file
if args.output:
    filename = args.output
else:
    filename = f"{args.ip}.txt"
with open(filename, "w") as f:
    for key, value in data.items():
        f.write(f"{key}: {value}\n")
print(f"\n{GREEN}[✔] {WHITE}Output saved to:{GREEN} {filename}")
