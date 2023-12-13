const fs = require("fs");

const data = JSON.parse(fs.readFileSync("./data.json", "utf8"));
const readme = fs.readFileSync("./README.md", "utf8").split("<!--automations-->")[0] + "<!--automations-->\n";
const output = readme + "Total coding time: " + data.data.human_readable_total_including_other_language;

fs.writeFileSync("./README.md", output);
