from json import *
import requests
from datetime import datetime
data = open('README.md', 'r').read( ).split('<!--automations-->')[0] + '<!--automations-->\n' + "### Coding Activity\n"
url = "https://wakatime.com/api/v1/users/VTrelat/stats"
response = requests.get(url)
stats = loads(response.text)["data"]

today = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
data += "_Last updated: " + today + "_\n"
total = "Total coding time: " + stats["human_readable_total_including_other_language"]

table="**Most used languages**:\n"+"| Language | Time | Percentage |\n"+"| ------------- | ------------- | ------------- |\n"
for line in stats["languages"][:9]:
    table += "| "+line["name"] + " | " + line["text"] + " | " + str(line["percent"]) + "% |" + "\n"

open('README.md', 'w').write(data + total + "\n" + table + "\n")