import csv
import requests
import time

API_KEY = '474081efa8c6f236f2359f44a51b793c424151c26ff467941d3d73e9a58e15ab76b7e8e46904ee91'
ABUSEIPDB_URL = 'https://api.abuseipdb.com/api/v2/check'

input_file = '../logs/sample_alerts.csv'
output_file = '../logs/enriched_alerts.csv'

def enrich_ip(ip):
    headers = {
        'Key': API_KEY,
        'Accept': 'application/json'
    }
    params = {
        'ipAddress': ip,
        'maxAgeInDays': 90
    }
    try:
        response = requests.get(ABUSEIPDB_URL, headers=headers, params=params)
        data = response.json()
        abuse_score = data['data']['abuseConfidenceScore']
        category = data['data']['usageType']
        return abuse_score, category
    except Exception as e:
        return "N/A", "N/A"

with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + ['threat_score', 'abuse_category']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        ip = row['src_ip']
        score, category = enrich_ip(ip)
        row['threat_score'] = score
        row['abuse_category'] = category
        writer.writerow(row)
        time.sleep(1)

