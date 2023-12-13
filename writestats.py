from json import *
data = open('README.md', 'r').read( ).split('<!--automations-->')[0] + '<!--automations-->\n' + "### Coding Activity\n"

stats = loads(open('data.json', 'r').read( ))["data"]

total = "Total coding time: " + stats["human_readable_total_including_other_language"]

table="**Most used languages**:\n"+"| Language | Time | Percentage |\n"+"| ------------- | ------------- | ------------- |\n"
for line in stats["languages"][:9]:
    table += "| "+line["name"] + " | " + line["text"] + " | " + str(line["percent"]) + " |" + "\n"

open('README.md', 'w').write(data + total + "\n" + table + "\n")