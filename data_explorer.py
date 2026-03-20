import pandas as pd

# 1. Load the data from your new CSV file
# This is like opening the book to read it
df = pd.read_csv("hyderabad_jobs.csv")

print("--- 📊 HYDERABAD JOB ANALYSIS ---")

# 2. Show the data on screen
print("\nRaw Data from CSV:")
print(df)

# 3. Calculate the Average Salary (The 'Analyst' part)
avg_salary = df["Salary"].mean()

print("-" * 30)
print(f"Average Hyderabad Salary: ₹{avg_salary:,.2f}")
print("-" * 30)

# 4. Find the 'Dream Job' (The highest salary)
highest = df.loc[df["Salary"].idxmax()]
print(f"Top Paying Company: {highest['Company']} (₹{highest['Salary']:,})")