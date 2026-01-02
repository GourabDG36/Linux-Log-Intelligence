import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Linux Log Intelligence Platform", layout="wide")

st.title("🔐 Linux System Log Intelligence Platform")

# ---------------- LOAD DATA ----------------

auth_df = pd.read_csv("data/features/auth_anomalies.csv")
sys_df = pd.read_csv("data/features/syslog_anomalies.csv")

# ---------------- METRICS ----------------

col1, col2, col3 = st.columns(3)

col1.metric("Auth Events", len(auth_df))
col2.metric("Auth Anomalies", auth_df["is_anomaly"].sum())
col3.metric("Syslog Anomalies", sys_df["is_anomaly"].sum())

# ---------------- AUTH ANOMALY TABLE ----------------

st.subheader("🚨 Authentication Anomalies")
st.dataframe(auth_df[auth_df["is_anomaly"]])

# ---------------- PLOT ----------------

st.subheader("📊 Failed vs Successful Logins")

fig, ax = plt.subplots()
ax.scatter(
    auth_df["failed_login_count"],
    auth_df["success_login_count"],
    c=auth_df["is_anomaly"]
)
ax.set_xlabel("Failed Logins")
ax.set_ylabel("Successful Logins")
ax.set_title("Authentication Anomaly Detection")

st.pyplot(fig)
