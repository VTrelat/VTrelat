import * as fs from "fs";
import fetch from "node-fetch";

const url = "https://wakatime.com/api/v1/users/VTrelat/stats";

const response = await fetch(url);

// save the response as a JSON object
const data = await response.json();
// save the data to a file
fs.writeFileSync("./data.json", JSON.stringify(data));
