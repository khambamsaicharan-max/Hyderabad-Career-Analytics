import pandas as pd
import plotly.express as px
import math
from datetime import datetime

print("--- 🏗️ BUILDING YOUR DAY 14 ASSET TRACKER ---")

# 1. LOAD & CLEAN DATA
try:
    df = pd.read_csv("hyderabad_jobs.csv", on_bad_lines='skip')
    df['Company'] = df['Company'].str.strip() 
    df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
    df = df.dropna(subset=['Salary']).sort_values(by='Salary', ascending=False)
except Exception as e:
    print(f"❌ Error: {e}")
    exit()

# 2. TAX FUNCTION
def calculate_in_hand(total_salary):
    taxable_income = max(0, total_salary - 75000)
    tax = 0 if taxable_income <= 700000 else taxable_income * 0.15 
    return total_salary - tax

# 3. ANALYTICS & SAVINGS LOGIC
avg_salary = df["Salary"].mean()
in_hand_avg = calculate_in_hand(avg_salary)
job_count = len(df)

# Asset Goal Logic
asset_name = "Dream Car"
asset_price = 1500000 # ₹15L
savings_rate = 0.30    # Saving 30%
monthly_savings = (in_hand_avg / 12) * savings_rate
months_to_asset = asset_price / monthly_savings

# Projections
future_avg = avg_salary * (1.10 ** 5)
in_hand_future = calculate_in_hand(future_avg)
last_updated = datetime.now().strftime("%Y-%m-%d %H:%M")

# 4. CHART
fig = px.bar(df, x='Company', y='Salary', color='Salary', template='plotly_dark')
chart_html = fig.to_html(full_html=False, include_plotlyjs='cdn')

# 5. HTML LAYOUT
name = "Saicharan"
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>{name}'s Portfolio</title>
    <style>
        body {{ font-family: 'Segoe UI', sans-serif; background-color: #0f172a; color: white; text-align: center; padding: 20px; }}
        .container {{ max-width: 1100px; margin: auto; background: #1e293b; padding: 30px; border-radius: 20px; border: 2px solid #38bdf8; }}
        .stats-container {{ display: flex; justify-content: center; gap: 15px; margin-bottom: 20px; flex-wrap: wrap; }}
        .stat-box {{ background: #0f172a; padding: 15px; border-radius: 12px; border-left: 5px solid #4ade80; flex: 1; min-width: 200px; }}
        .goal-card {{ background: #0f172a; padding: 20px; border-radius: 15px; margin-top: 20px; border: 2px solid #fbbf24; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 {name}'s Career & Wealth Portal</h1>
        <div class="stats-container">
            <div class="stat-box"><b>In-Hand Monthly</b><br>₹{in_hand_avg/12:,.0f}</div>
            <div class="stat-box" style="border-color:#a855f7"><b>5-Year Monthly</b><br>₹{in_hand_future/12:,.0f}</div>
            <div class="stat-box" style="border-color:#38bdf8"><b>Data Points</b><br>{job_count} Jobs</div>
        </div>

        <div style="background:#111; border-radius:15px; padding:10px;">{chart_html}</div>

        <div class="goal-card">
            <h2 style="color:#fbbf24; margin-top:0;">🏎️ {asset_name} Timeline</h2>
            <p>Target: ₹{asset_price:,.0f} | Monthly Savings (30%): <b>₹{monthly_savings:,.0f}</b></p>
            <p style="font-size: 24px;">Time to Buy: <b>{months_to_asset:.1f} Months</b></p>
        </div>

        <p style="color:#64748b; font-size:12px; margin-top:30px;">Refreshed: {last_updated}</p>
    </div>
</body>
</html>
"""

with open("portal.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"✅ DAY 14 COMPLETE: Asset tracker is live!")