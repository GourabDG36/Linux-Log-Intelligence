import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# ---------------- LOAD DATA ----------------

AUTH_PATH = "data/features/auth_clustered.csv"
SYS_PATH = "data/features/syslog_clustered.csv"

auth_df = pd.read_csv(AUTH_PATH)
sys_df = pd.read_csv(SYS_PATH)

auth_X = auth_df.drop(columns=["hour", "cluster"])
sys_X = sys_df.drop(columns=["hour", "cluster"])

# ---------------- SCALE ----------------

scaler = StandardScaler()
auth_X_scaled = scaler.fit_transform(auth_X)
sys_X_scaled = scaler.fit_transform(sys_X)

# ---------------- ISOLATION FOREST ----------------

iso_auth = IsolationForest(contamination=0.2, random_state=42)
iso_sys = IsolationForest(contamination=0.2, random_state=42)

auth_df["anomaly"] = iso_auth.fit_predict(auth_X_scaled)
sys_df["anomaly"] = iso_sys.fit_predict(sys_X_scaled)

# -1 = anomaly, 1 = normal
auth_df["is_anomaly"] = auth_df["anomaly"] == -1
sys_df["is_anomaly"] = sys_df["anomaly"] == -1

# ---------------- SAVE ----------------

auth_df.to_csv("data/features/auth_anomalies.csv", index=False)
sys_df.to_csv("data/features/syslog_anomalies.csv", index=False)

# ---------------- VISUAL ----------------

plt.figure()
plt.scatter(
    auth_df["failed_login_count"],
    auth_df["success_login_count"],
    c=auth_df["is_anomaly"]
)
plt.xlabel("Failed Logins")
plt.ylabel("Successful Logins")
plt.title("Auth Log Anomaly Detection")
plt.show()
