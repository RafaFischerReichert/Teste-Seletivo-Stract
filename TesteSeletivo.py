from flask import Flask, jsonify, request
import requests
import csv
from io import StringIO

app = Flask(__name__)

API_URL = "https://sidebar.stract.to/api"
HEADERS = {
    "Authorization": "Bearer ProcessoSeletivoStract2025"
}

@app.route('/')
def home():
    return jsonify({
        "name": "Rafael Fischer Reichert",
        "email": "rafa.fr2011@gmail.com",
        "linkedin": "https://www.linkedin.com/in/rafael-fischer-reichert-81b33a206/"
    })

@app.route('/<platform>', methods=['GET'])
def get_ads(platform):
    accounts = requests.get(f'{API_URL}/accounts?platform={platform}', headers=HEADERS).json()
    insights_data = []

    for account in accounts:
        insights = requests.get(f'{API_URL}/insights?platform={platform}&account={account}', headers=HEADERS).json()
        for insight in insights:
            insights_data.append({
                "Platform": platform,
                **insight,
                "Account Name": account
            })

    return generate_csv(insights_data)

@app.route('/<platform>/resumo', methods=['GET'])
def get_ads_summary(platform):
    accounts = requests.get(f'{API_URL}/accounts?platform={platform}', headers=HEADERS).json()
    summary_data = {}

    for account in accounts:
        insights = requests.get(f'{API_URL}/insights?platform={platform}&account={account}', headers=HEADERS).json()
        for insight in insights:
            if account not in summary_data:
                summary_data[account] = {"Clicks": 0}
            summary_data[account]["Clicks"] += insight["clicks"]

    return generate_csv_summary(summary_data, platform)

@app.route('/geral', methods=['GET'])
def get_all_ads():
    platforms = requests.get(f'{API_URL}/platforms', headers=HEADERS).json()
    all_insights_data = []

    for platform in platforms:
        accounts = requests.get(f'{API_URL}/accounts?platform={platform}', headers=HEADERS).json()
        for account in accounts:
            insights = requests.get(f'{API_URL}/insights?platform={platform}&account={account}', headers=HEADERS).json()
            for insight in insights:
                all_insights_data.append({
                    "Platform": platform,
                    **insight,
                    "Account Name": account
                })

    return generate_csv(all_insights_data)

@app.route('/geral/resumo', methods=['GET'])
def get_all_ads_summary():
    platforms = requests.get(f'{API_URL}/platforms', headers=HEADERS).json()
    summary_data = {}

    for platform in platforms:
        accounts = requests.get(f'{API_URL}/accounts?platform={platform}', headers=HEADERS).json()
        for account in accounts:
            insights = requests.get(f'{API_URL}/insights?platform={platform}&account={account}', headers=HEADERS).json()
            for insight in insights:
                if platform not in summary_data:
                    summary_data[platform] = {"Clicks": 0}
                summary_data[platform]["Clicks"] += insight["clicks"]

    return generate_csv_summary(summary_data)

def generate_csv(data):
    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
    return output.getvalue(), 200, {'Content-Type': 'text/csv'}

def generate_csv_summary(data, platform):
    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=["Platform", "Ad Name", "Clicks"])
    writer.writeheader()
    for account, values in data.items():
        writer.writerow({"Platform": platform, "Ad Name": account, "Clicks": values["Clicks"]})
    return output.getvalue(), 200, {'Content-Type': 'text/csv'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
