from json import *
data = open('README.md', 'r').read( ).split('<!--automations-->')[0] + '<!--automations-->\n'

stats = loads(open('data.json', 'r').read( ))["data"]

text = "Total coding time: " + stats["human_readable_total_including_other_language"]
open('README.md', 'w').write(data + text)