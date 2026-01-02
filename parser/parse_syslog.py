import re
import pandas as pd

LOG_PATH = "data/raw/syslog"
OUTPUT_PATH = "data/processed/syslog_parsed.csv"

pattern = re.compile(
    r'(?P<month>\w+)\s+(?P<day>\d+)\s+(?P<time>\d+:\d+:\d+)\s+'
    r'(?P<host>\S+)\s+(?P<process>[\w\-\[\]]+):\s+'
    r'(?P<message>.*)'
)

records = []

with open(LOG_PATH, "r") as file:
    for line in file:
        match = pattern.match(line)
        if not match:
            continue

        data = match.groupdict()

        records.append({
            "timestamp": f"{data['month']} {data['day']} {data['time']}",
            "host": data["host"],
            "process": data["process"],
            "message": data["message"]
        })

df = pd.DataFrame(records)
df.to_csv(OUTPUT_PATH, index=False)

print(f"[✓] Parsed syslog saved to {OUTPUT_PATH}")
