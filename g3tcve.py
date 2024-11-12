#!/usr/bin/env python3
import requests
import argparse
from bs4 import BeautifulSoup
import textwrap
from termcolor import colored

print(colored("----CVE DETAILS----", "green"))

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--id', required=True, help="Enter CVE-ID (example 'CVE-2024-51610')")
args = parser.parse_args()

web_url = 'https://nvd.nist.gov/vuln/detail/'
full_web_url = web_url + args.id

x = requests.get(full_web_url)

soup = BeautifulSoup(x.text, 'html.parser')

p_tag = soup.find('p', attrs={'data-testid': 'vuln-description'})
if p_tag:
    p_text = p_tag.get_text()
    print(colored('\nDescription: ', "green") + textwrap.fill(p_text, width=60))

a_tag = soup.find('a', attrs={'data-testid': 'vuln-cvss3-cna-panel-score'})
if a_tag:
    a_text = a_tag.get_text()
    print(colored('\nCVSS:3.1 Score: ', "green") + textwrap.fill(a_text, width=50))

td_tag_1 = soup.find('td', attrs={'data-testid': 'vuln-CWEs-link-0'})
if td_tag_1:
    td_text_1 = td_tag_1.get_text()
    print(colored('\nCWE-ID:', "green") + textwrap.fill(td_text_1, width=50))

td_tag_2 = soup.find('tbody').get_text()
clean_output = '\n'.join(line.strip() for line in td_tag_2.splitlines() if line.strip())
print(colored('\nHyper-Links:', "green") + '\n' + clean_output)
