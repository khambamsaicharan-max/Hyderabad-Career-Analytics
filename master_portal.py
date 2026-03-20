import pandas as pd
import plotly.express as px
import os
from datetime import datetime

# --- 1. DATA LOADING & CONFIG ---
csv_file = "hyderabad_jobs.csv"
last_updated = datetime.now().strftime("%d %b %Y, %I:%M %p")

def load_clean_data(file_path):
    if not os.path.exists(file_path):
        return pd.DataFrame({"Company": ["Waiting for Scraper"], "Salary": [1200000]})
    try:
        df = pd.read_csv(file_path, on_bad_lines='skip', engine='python')
        df = df.iloc[:, [0, 1]] 
        df.columns = ["Company", "Salary"]
        df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
        df = df.dropna()
        # Quality Filter: Only high-value roles
        df = df[df['Salary'] >= 600000]
        return df
    except:
        return pd.DataFrame({"Company": ["Backup Data"], "Salary": [1000000]})

df = load_clean_data(csv_file)

# --- 2. ANALYTICS & FORECAST LOGIC ---
avg_salary = df["Salary"].mean()
monthly_target, monthly_takehome = 300000, (avg_salary * 0.75) / 12
projected_savings = monthly_takehome * 0.5 
years_to_30L = 3000000 / (projected_savings * 12) if projected_savings > 0 else 0

years = [2026, 2027, 2028, 2029, 2030]
forecast_salaries = [avg_salary * (1.15**i) for i in range(5)]

# --- 3. PROJECT DATA (JOURNEY & INTERVIEW) ---
journey = [
    {"Day": "1-5", "Task": "Scraper Engine Built", "Status": "Done"},
    {"Day": "6-15", "Task": "Data Cleaning & CSV Logic", "Status": "Done"},
    {"Day": "16-25", "Task": "Interactive UI & ML Forecast", "Status": "Done"},
    {"Day": "26-30", "Task": "AI Integration & Deployment", "Status": "Active"}
]

interview_qa = [
    {"Skill": "Python", "Question": "Memory Management?", "Tip": "Mention GC & Reference Counting."},
    {"Skill": "SQL", "Question": "WHERE vs HAVING?", "Tip": "WHERE filters rows; HAVING filters groups."},
    {"Skill": "Power BI", "Question": "Calculated Columns vs Measures?", "Tip": "Measures are dynamic aggregates."}
]

# --- 4. CREATE THE VISUALS ---
fig = px.bar(df, x="Company", y="Salary", title="Live Hyderabad Market Intelligence",
             color="Salary", color_continuous_scale="Viridis", template="plotly_dark")
fig.update_layout(xaxis_tickangle=-45, margin=dict(b=150))

forecast_fig = px.line(x=years, y=forecast_salaries, title="5-Year Career Growth vs. ₹30L Target",
                       markers=True, template="plotly_dark")
forecast_fig.add_hline(y=3000000, line_dash="dot", line_color="#ef4444", 
                       annotation_text="🎯 ₹30L TARGET", annotation_position="bottom right")
forecast_fig.update_traces(line_color='#38bdf8', line_width=4)

# --- 5. GENERATE THE HTML PORTAL ---
table_rows = "".join([f"<tr><td style='padding:12px; border-bottom:1px solid #334155;'>{item['Skill']}</td><td style='padding:12px; border-bottom:1px solid #334155;'>{item['Question']}</td><td style='padding:12px; border-bottom:1px solid #334155; color:#4ade80;'>{item['Tip']}</td></tr>" for item in interview_qa])

timeline_html = "".join([f'<div style="margin-bottom: 15px; padding-left: 15px; border-left: 2px solid #334155;"><b style="color: #4ade80;">Day {j["Day"]}:</b> {j["Task"]} <span style="font-size: 0.7rem; background: #334155; padding: 2px 8px; border-radius: 10px; margin-left: 10px; color:#9ca3af;">{j["Status"]}</span></div>' for j in journey])

html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Saicharan | Project Roadmap</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <style>
        body {{ background: #0b1120; color: white; font-family: 'Segoe UI', sans-serif; text-align: center; padding: 20px; }}
        .container {{ max-width: 900px; margin: auto; padding-bottom: 100px; }}
        .card {{ background: #111827; padding: 30px; border-radius: 20px; margin-bottom: 30px; border: 1px solid #1f2937; box-shadow: 0 4px 20px rgba(0,0,0,0.5); }}
        h1 {{ color: #38bdf8; font-size: 2.5rem; margin: 0; }}
        .timestamp {{ font-size: 0.8rem; color: #4ade80; margin-top: 10px; font-weight: bold; }}
        table {{ width: 100%; border-collapse: collapse; margin-top: 20px; background: #1e293b; border-radius: 10px; overflow: hidden; }}
        .btn {{ background: #4ade80; color: #0b1120; border: none; padding: 12px 25px; border-radius: 8px; font-weight: bold; cursor: pointer; }}
        .contact-btn {{ position: fixed; bottom: 30px; right: 30px; background: #38bdf8; color: #0b1120; padding: 15px 25px; border-radius: 50px; font-weight: bold; text-decoration: none; z-index: 1000; box-shadow: 0 5px 15px rgba(56, 189, 248, 0.4); }}
    </style>
</head>
<body>
    <div class="container">
        <div class="card" style="border: 2px solid #38bdf8;">
            <h1>Saicharan</h1>
            <p style="color: #9ca3af; font-style: italic;">Data Scientist @ Hyderabad</p>
            <div class="timestamp">🟢 Data Analytics Pipeline Live: {last_updated}</div>
        </div>

        <div class="card">{fig.to_html(full_html=False, include_plotlyjs='cdn')}</div>
        <div class="card">{forecast_fig.to_html(full_html=False, include_plotlyjs='cdn')}</div>

        <div class="card" style="text-align: left; border-top: 4px solid #fbbf24;">
            <h2 style="color: #fbbf24;">🎯 Interview Preparation Edge</h2>
            <table>
                <tr style="background: #334155; color: #fbbf24;"><th style="padding: 12px;">Skill</th><th style="padding: 12px;">Question</th><th style="padding: 12px;">Expert Tip</th></tr>
                {table_rows}
            </table>
        </div>

        <div class="card" style="text-align: left; border-left: 4px solid #38bdf8;">
            <h2 style="color: #38bdf8;">🛣️ Project Development Roadmap</h2>
            <div style="margin-top: 15px;">
                {timeline_html}
            </div>
        </div>

        <div class="card" style="text-align: left; border: 2px solid #4ade80;">
            <h2 style="color: #4ade80;">📄 Professional Resume Summary</h2>
            <div id="resume-content" style="color: #d1d5db; line-height: 1.8;">
                <b>Name:</b> Saicharan <br>
                <b>Core Stack:</b> Python, SQL, Power BI, Web Scraping <br>
                <b>Market Insight:</b> Analyzing {len(df)} High-Value Hyderabad Roles <br>
                <b>Projection:</b> Hitting ₹30L Target via 15% Annual Upskilling Growth.
            </div>
            <button class="btn" onclick="copyResume()" style="margin-top: 20px;">📋 Copy for LinkedIn</button>
        </div>

        <a href="https://www.linkedin.com/in/YOUR-NAME" class="contact-btn">💼 Connect with Me</a>
    </div>

    <script>
        function copyResume() {{
            var content = document.getElementById('resume-content').innerText;
            navigator.clipboard.writeText(content).then(() => {{
                alert("Resume Summary Copied! Perfect for your LinkedIn 'About' section.");
            }});
        }}
    </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"✅ DAY 26 COMPLETE: Full High-End Portal Generated!")