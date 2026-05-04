import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.indeed.com/jobs?q=devops+engineer&l=india"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

jobs = soup.find_all("a", attrs={"data-hide-spinner": "true"})

job_list = []

for job in jobs[:10]:
    title = job.text.strip()
    link = "https://indeed.com" + job.get("href")
    
    job_list.append([title, link])

with open("jobs.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Link"])
    writer.writerows(job_list)

print("Jobs saved successfully!")
