import pandas as pd
import os

print("--- 📝 HYDERABAD JOB INPUT FORM ---")

# 1. Ask the user for data
new_company = input("Enter Company Name: ")
new_salary = int(input("Enter Salary (in ₹): "))
new_title = input("Enter Job Title: ")

# 2. Create a small dictionary for the new data
new_data = {
    "Job_Title": [new_title],
    "Salary": [new_salary],
    "Company": [new_company]
}

# 3. Add to the CSV without overwriting old data
new_df = pd.DataFrame(new_data)
new_df.to_csv("hyderabad_jobs.csv", mode='a', index=False, header=False)

print(f"\n✅ {new_company} added successfully!")

# 4. THE MAGIC STEP: Automatically run your Day 8 script to refresh the portal
print("🔄 Refreshing your Career Portal...")
os.system("py master_portal.py") 
print("🚀 Done! Open 'portal.html' to see the update.")