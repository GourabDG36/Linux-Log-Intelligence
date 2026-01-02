import re
import pandas as pd
from datetime import datetime

LOG_PATH = "data/raw/auth.log"
OUTPUT_PATH = "data/processed/auth_parsed.csv"

pattern = re.compile(
    r'(?P<month>\w+)\s+(?P<day>\d+)\s+(?P<time>\d+:\d+:\d+)\s+'
    r'(?P<host>\S+)\s+(?P<process>\S+):\s+'
    r'(?P<message>.*)'
)

records = []

with open(LOG_PATH, "r") as file:
    for line in file:
        match = pattern.match(line)
        if not match:
            continue

        data = match.groupdict()
        message = data["message"]

        event_type = "other"
        user = None
        ip = None

        if "Failed password" in message:
            event_type = "failed_login"
            user_match = re.search(r'for (\w+)', message)
            ip_match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', message)

            if user_match:
                user = user_match.group(1)
            if ip_match:
                ip = ip_match.group(1)

        elif "Accepted password" in message:
            event_type = "successful_login"
            user_match = re.search(r'for (\w+)', message)
            ip_match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', message)

            if user_match:
                user = user_match.group(1)
            if ip_match:
                ip = ip_match.group(1)

        timestamp = f"{data['month']} {data['day']} {data['time']}"

        records.append({
            "timestamp": timestamp,
            "host": data["host"],
            "process": data["process"],
            "event_type": event_type,
            "user": user,
            "ip": ip,
            "raw_message": message
        })

df = pd.DataFrame(records)
df.to_csv(OUTPUT_PATH, index=False)

print(f"[✓] Parsed auth logs saved to {OUTPUT_PATH}")
