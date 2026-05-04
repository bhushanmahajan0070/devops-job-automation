import requests
from bs4 import BeautifulSoup
import csv
import os

URL = "https://www.indeed.com/jobs?q=devops+engineer&l=india"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

jobs = soup.select("a[data-hide-spinner='true']")

job_list = []

for job in jobs[:10]:
    title = job.text.strip()
    link = "https://indeed.com" + job.get("href")
    job_list.append(f"{title} - {link}")

# Save CSV
with open("jobs.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Jobs"])
    for j in job_list:
        writer.writerow([j])

# Telegram Alert
def send_telegram(message):
    TOKEN = os.getenv("TELEGRAM_TOKEN")
    CHAT_ID = os.getenv("CHAT_ID")

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": message})

send_telegram("\n".join(job_list))

print("Done!")
