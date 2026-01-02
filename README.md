# 🔐 Linux System Log Intelligence Platform

An end-to-end **machine learning–based log intelligence system** that analyzes Linux system and authentication logs to detect **anomalies, failures, and potential intrusions** using **unsupervised learning techniques**.

This project demonstrates how real-world system logs can be transformed into actionable security insights using data science.

---

## 🚀 Features

- Parses raw Linux system and authentication logs
- Performs feature engineering on time-based log data
- Learns **normal system behavior** using clustering
- Detects **anomalous and suspicious activity** using Isolation Forest
- Interactive **Streamlit dashboard** for monitoring and visualization

---

## 🧠 Motivation

Linux systems generate large volumes of logs that are rarely analyzed proactively.  
Manual inspection is inefficient and error-prone.

This project aims to:
- Automate log analysis
- Identify abnormal patterns without labeled data
- Bridge **systems knowledge + data science + security analytics**

---

## 🏗️ System Architecture

Raw Linux Logs
↓
Log Parsing
↓
Feature Engineering (Time-based Aggregation)
↓
Clustering (Normal Behavior)
↓
Anomaly Detection (Isolation Forest)
↓
Streamlit Dashboard

---

## 🛠️ Tech Stack

- **Language:** Python
- **Data Processing:** Pandas
- **Machine Learning:** Scikit-learn
- **Visualization:** Matplotlib
- **Dashboard:** Streamlit
- **Logs:** Linux `auth.log` and `syslog`
- **Version Control:** Git & GitHub

---

## 📁 Project Structure

Linux-Log-Intelligence/
├── parser/ # Log parsing scripts
├── features/ # Feature engineering
├── models/ # Clustering & anomaly detection
├── dashboard/ # Streamlit app
├── data/
│ ├── raw/ # Sample log files
│ ├── processed/ # Parsed CSV files
│ └── features/ # ML-ready datasets
├── requirements.txt
├── README.md
└── .gitignore


---

## 📊 Machine Learning Approach

### 1️⃣ Feature Engineering
- Aggregated log events by hour
- Extracted security-relevant metrics:
  - Failed login count
  - Successful login count
  - Unique IPs and users
  - Kernel and system error indicators

### 2️⃣ Clustering
- **KMeans** used to learn baseline (normal) system behavior
- Helps identify behavioral patterns without labels

### 3️⃣ Anomaly Detection
- **Isolation Forest** used to detect deviations from normal behavior
- Flags suspicious login bursts, abnormal system activity, and rare events

---

## 📈 Dashboard Preview

The Streamlit dashboard provides:
- Total events and anomaly counts
- Tables of suspicious activity
- Visual plots of detected anomalies

---

## ▶️ How to Run the Project

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt

2️⃣ Parse logs
python parser/parse_auth.py
python parser/parse_syslog.py

3️⃣ Build features
python features/build_features.py

4️⃣ Run clustering
python models/clustering.py

5️⃣ Detect anomalies
python models/anomaly_detection.py

6️⃣ Launch dashboard
streamlit run dashboard/app.py

🔐 Data Disclaimer

Log files used in this project are sanitized samples

They strictly follow real Linux log formats

No sensitive or personal data is included

This approach is standard practice for security-focused academic projects

🔮 Future Enhancements

Real-time log streaming

NLP-based log embeddings

Alerting and notification system

Dockerized deployment

Integration with SIEM tools
