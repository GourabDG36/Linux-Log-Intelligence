import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# ---------------- LOAD DATA ----------------

AUTH_PATH = "data/features/auth_features.csv"
SYS_PATH = "data/features/syslog_features.csv"

auth_df = pd.read_csv(AUTH_PATH)
sys_df = pd.read_csv(SYS_PATH)

# Drop hour column for clustering
auth_X = auth_df.drop(columns=["hour"])
sys_X = sys_df.drop(columns=["hour"])

# ---------------- SCALE FEATURES ----------------

scaler = StandardScaler()
auth_X_scaled = scaler.fit_transform(auth_X)
sys_X_scaled = scaler.fit_transform(sys_X)

# ---------------- KMEANS ----------------

kmeans_auth = KMeans(n_clusters=2, random_state=42)
kmeans_sys = KMeans(n_clusters=2, random_state=42)

auth_clusters = kmeans_auth.fit_predict(auth_X_scaled)
sys_clusters = kmeans_sys.fit_predict(sys_X_scaled)

auth_df["cluster"] = auth_clusters
sys_df["cluster"] = sys_clusters

# ---------------- SAVE OUTPUT ----------------

auth_df.to_csv("data/features/auth_clustered.csv", index=False)
sys_df.to_csv("data/features/syslog_clustered.csv", index=False)

# ---------------- QUICK VISUALIZATION ----------------

plt.figure()
plt.scatter(
    auth_df["failed_login_count"],
    auth_df["success_login_count"],
    c=auth_df["cluster"]
)
plt.xlabel("Failed Logins")
plt.ylabel("Successful Logins")
plt.title("Auth Log Clustering")
plt.show()
