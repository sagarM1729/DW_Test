const fs = require("fs");
const html = fs.readFileSync("tables_mapping.html", "utf-8");
const match = html.match(/const TABLES = (\{[\s\S]*?\});\n\n\/\* ─── RELATIONSHIPS/);
if (match) {
  // Use eval to parse the JS object literal into a JS object
  let tablesStr = match[1];
  let code = "var TABLES = " + tablesStr + "; TABLES;";
  let tables = eval(code);
  fs.writeFileSync("src/utils/tables.json", JSON.stringify(tables, null, 2));
  console.log("Successfully extracted TABLES to src/utils/tables.json");
} else {
  console.error("Could not match TABLES regex");
}
