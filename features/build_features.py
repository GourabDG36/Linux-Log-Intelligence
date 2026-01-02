import pandas as pd

AUTH_INPUT = "data/processed/auth_parsed.csv"
SYS_INPUT = "data/processed/syslog_parsed.csv"

AUTH_OUTPUT = "data/features/auth_features.csv"
SYS_OUTPUT = "data/features/syslog_features.csv"

# ------------------ AUTH LOG FEATURES ------------------

auth_df = pd.read_csv(AUTH_INPUT)

auth_df["hour"] = auth_df["timestamp"].str.extract(r'(\d+):').astype(int)

auth_features = auth_df.groupby("hour").agg(
    failed_login_count=("event_type", lambda x: (x == "failed_login").sum()),
    success_login_count=("event_type", lambda x: (x == "successful_login").sum()),
    unique_ips=("ip", "nunique"),
    unique_users=("user", "nunique"),
    total_events=("event_type", "count")
).reset_index()

auth_features.to_csv(AUTH_OUTPUT, index=False)

# ------------------ SYSLOG FEATURES ------------------

sys_df = pd.read_csv(SYS_INPUT)

sys_df["hour"] = sys_df["timestamp"].str.extract(r'(\d+):').astype(int)

sys_features = sys_df.groupby("hour").agg(
    kernel_events=("process", lambda x: x.str.contains("kernel").sum()),
    oom_events=("message", lambda x: x.str.contains("Out of memory|Killed process").sum()),
    network_events=("message", lambda x: x.str.contains("eth|Network").sum()),
    cron_jobs=("process", lambda x: x.str.contains("CRON").sum()),
    total_events=("process", "count")
).reset_index()

sys_features.to_csv(SYS_OUTPUT, index=False)

print("[✓] Feature engineering completed successfully")
