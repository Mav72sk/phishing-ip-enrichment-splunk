# SOC Alert Triage Workflow with Threat Intelligence Enrichment (Splunk + AbuseIPDB)

This project simulates how a SOC analyst would enrich IPs from phishing and malware alerts using **AbuseIPDB**, then visualize threat scores and abuse categories in **Splunk**.

## Tools Used
- Splunk Free (local instance)
- Python 3
- AbuseIPDB API
- CSV logs (simulated alerts)
- Basic threat enrichment


## Folder Structure

phishing-ip-enrichment-splunk/
├── enrichment/ → Python script to enrich IPs
├── logs/ → Sample alerts and enriched alerts
├── screenshots/ → Dashboard visuals
└── README.md


## Output: enriched_alerts.csv

src_ip	threat_score	abuse_category
203.0.113.5	0	Reserved


## Splunk Dashboard Panels

Top Threat Scores by IP (Bar Chart)
Abuse Category Distribution (Pie Chart)
Average Threat Score (Single Value)


## Screenshots


<img width="735" height="651" alt="Screenshot 2025-07-12 at 4 01 32 PM" src="https://github.com/user-attachments/assets/e6ba5287-36a1-42e3-835e-5bc44110f2c3" />



<img width="1470" height="707" alt="threat-intel-dashboard" src="https://github.com/user-attachments/assets/60e61ed4-cbca-439a-8ef2-0dcaa21ece28" />


## Note

This project uses safe sample IPs. In a real environment, abuse scores would vary. This method helps SOC analysts triage alerts more intelligently by adding external threat intel.

## Learnings

Automating threat enrichment
Using APIs in alert pipelines
Creating SOC dashboards in Splunk


