import requests
from bs4 import BeautifulSoup
import pandas as pd

print("--- 🕵️ DAY 17: STARTING THE JOB SNIFFER ---")

# 1. The Target (Using a practice site first)
url = "https://realpython.github.io/fake-jobs/" 

try:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # 2. Find all Job Cards
    job_elements = soup.find_all("div", class_="card-content")

    scraped_data = []

    for job in job_elements[:5]: # Let's just grab the top 5
        title = job.find("h2", class_="title").text.strip()
        company = job.find("h3", class_="company").text.strip()
        location = job.find("p", class_="location").text.strip()
        
        # We'll assign a random market salary for now since this is a fake site
        salary = 1200000 if "Python" in title else 800000
        
        print(f"✅ Found: {title} at {company}")
        scraped_data.append({"Company": company, "Salary": salary})

    # 3. Append to your real CSV!
    new_df = pd.DataFrame(scraped_data)
    new_df.to_csv("hyderabad_jobs.csv", mode='a', index=False, header=False)
    print("\n🚀 SUCCESS: Data added to hyderabad_jobs.csv automatically!")

except Exception as e:
    print(f"❌ Scraping Error: {e}")