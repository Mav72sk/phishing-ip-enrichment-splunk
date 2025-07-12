# 📡 Phishing IP Enrichment & Threat Dashboard (Splunk + AbuseIPDB)

This project simulates how a SOC analyst would enrich IPs from phishing and malware alerts using **AbuseIPDB**, then visualize threat scores and abuse categories in **Splunk**.

## 🔧 Tools Used
- Splunk Free (local instance)
- Python 3
- AbuseIPDB API
- CSV logs (simulated alerts)
- Basic threat enrichment

## 📁 Folder Structure

phishing-ip-enrichment-splunk/
├── enrichment/ → Python script to enrich IPs
├── logs/ → Sample alerts and enriched alerts
├── screenshots/ → Dashboard visuals
└── README.md


## 🧪 Sample Input: `sample_alerts.csv`

```csv
timestamp,alert_type,src_ip,dest_ip,user,subject,file_name,process
2025-07-13 10:04:00,Phishing,203.0.113.5,192.168.1.15,bob,Urgent: Account Notice,invoice.exe,


✅ Output: enriched_alerts.csv

src_ip	threat_score	abuse_category
203.0.113.5	0	Reserved


📊 Splunk Dashboard Panels

Top Threat Scores by IP (Bar Chart)
Abuse Category Distribution (Pie Chart)
Average Threat Score (Single Value)

🖼️ Screenshots




💡 Note

This project uses safe sample IPs. In a real environment, abuse scores would vary. This method helps SOC analysts triage alerts more intelligently by adding external threat intel.

📌 Learnings

Automating threat enrichment
Using APIs in alert pipelines
Creating SOC dashboards in Splunk


