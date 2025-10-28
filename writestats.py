from json import *
import requests
from datetime import datetime

MERGED_LANGUAGE_GROUPS = {
    "Lean": {"Lean", "Lean4"},
}


def _format_duration(total_seconds: float) -> str:
    total_seconds = int(round(total_seconds))
    hours, remainder = divmod(total_seconds, 3600)
    minutes = remainder // 60
    parts = []
    if hours:
        parts.append(f"{hours} {'hr' if hours == 1 else 'hrs'}")
    if minutes:
        parts.append(f"{minutes} {'min' if minutes == 1 else 'mins'}")
    if not parts:
        parts.append("0 secs")
    return " ".join(parts)


def _format_percent(value: float) -> str:
    formatted = f"{value:.2f}"
    return formatted.rstrip("0").rstrip(".")


def _merge_languages(languages):
    merged = {}
    order = {}
    for index, language in enumerate(languages):
        target_name = next(
            (
                merged_name
                for merged_name, group in MERGED_LANGUAGE_GROUPS.items()
                if language["name"] in group
            ),
            language["name"],
        )
        if target_name not in merged:
            merged[target_name] = {"total_seconds": 0.0, "percent": 0.0}
            order[target_name] = index
        merged[target_name]["total_seconds"] += language.get("total_seconds", 0)
        merged[target_name]["percent"] += language.get("percent", 0)

    merged_list = []
    for name, info in merged.items():
        merged_list.append(
            {
                "name": name,
                "total_seconds": info["total_seconds"],
                "percent": info["percent"],
            }
        )

    merged_list.sort(key=lambda item: (-item["total_seconds"], order[item["name"]]))
    return merged_list


data = open('README.md', 'r').read( ).split('<!--automations-->')[0] + '<!--automations-->\n' + "### Coding Activity\n"
url = "https://wakatime.com/api/v1/users/VTrelat/stats"
response = requests.get(url)
stats = loads(response.text)["data"]

today = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
data += "_Last updated: " + today + "_\n"
total = "\nTotal coding time: " + stats["human_readable_total_including_other_language"]

languages = _merge_languages(stats["languages"])

table="\n**Most used languages**:\n"+"\n| Language | Time | Percentage |\n"+"| ------------- | ------------- | ------------- |\n"
for line in languages[:9]:
    table += (
        "| "
        + line["name"]
        + " | "
        + _format_duration(line["total_seconds"])
        + " | "
        + _format_percent(line["percent"])
        + "% |\n"
    )

open('README.md', 'w').write(data + total + "\n" + table + "\n")
