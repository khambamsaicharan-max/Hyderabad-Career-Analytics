import pandas as pd
import plotly.express as px

print("--- 🎨 GENERATING SALARY VISUALS ---")

# 1. Load the data you updated yesterday
df = pd.read_csv("hyderabad_jobs.csv")

# 2. Create a Bar Chart
# We tell Plotly: Use Company for X-axis and Salary for Y-axis
fig = px.bar(df, 
             x='Company', 
             y='Salary', 
             title='Hyderabad Tech Salary Comparison 2026',
             color='Salary', # This makes higher salaries a different color!
             text_auto='.2s') # This puts the salary labels on top of the bars

# 3. Save it as a Website File
fig.write_html("salary_chart.html")

print("\n✅ CHART GENERATED!")
print("1. Look for 'salary_chart.html' in your sidebar.")
print("2. Open it in your browser to see the interactive graph.")