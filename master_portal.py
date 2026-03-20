import pandas as pd
import plotly.express as px
import os
from datetime import datetime

# --- 1. DATA LOADING & SELF-HEALING ---
csv_file = "hyderabad_jobs.csv"
last_updated = datetime.now().strftime("%d %b %Y, %I:%M %p")

def load_clean_data(file_path):
    if not os.path.exists(file_path):
        # Fallback if CSV is missing
        return pd.DataFrame({"Company": ["Waiting for Scraper"], "Salary": [1200000]})
    try:
        df = pd.read_csv(file_path, on_bad_lines='skip', engine='python')
        # Ensure we only take the first two columns
        df = df.iloc[:, [0, 1]] 
        df.columns = ["Company", "Salary"]
        df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
        df = df.dropna()
        # Quality Filter: Only show jobs paying 6L+
        df = df[df['Salary'] >= 600000]
        return df
    except Exception as e:
        print(f"Error: {e}")
        return pd.DataFrame({"Company": ["Backup Data"], "Salary": [1000000]})

df = load_clean_data(csv_file)

# --- 2. CAREER & FINANCIAL LOGIC ---
avg_salary = df["Salary"].mean()
monthly_target = 300000
# Take-home (75% of Gross) / 12 months
monthly_takehome = (avg_salary * 0.75) / 12
projected_savings = monthly_takehome * 0.5 
years_to_30L = 3000000 / (projected_savings * 12) if projected_savings > 0 else 0

# --- 3. 5-YEAR FORECAST & SKILLS ---
years = [2026, 2027, 2028, 2029, 2030]
forecast_salaries = [avg_salary * (1.15**i) for i in range(5)]

interview_qa = [
    {"Skill": "Python", "Question": "How is memory managed?", "Tip": "Mention Garbage Collection."},
    {"Skill": "SQL", "Question": "WHERE vs HAVING?", "Tip": "WHERE=Rows, HAVING=Groups."},
    {"Skill": "Power BI", "Question": "Measures vs Columns?", "Tip": "Measures=Aggregates (DAX)."}
]

# --- 4. CREATE THE VISUALS ---

# Chart 1: Market Bar Chart (With Tilted Labels)
fig = px.bar(df, x="Company", y="Salary", 
             title="Live Hyderabad Market Intelligence",
             color="Salary", color_continuous_scale="Viridis", template="plotly_dark")
fig.update_layout(xaxis_tickangle=-45, margin=dict(b=150))

# Chart 2: Future Forecast (With Red Target Line)
forecast_fig = px.line(x=years, y=forecast_salaries, 
                       title="5-Year Growth vs. ₹30L Goal",
                       markers=True, template="plotly_dark")
forecast_fig.add_hline(y=3000000, line_dash="dot", line_color="#ef4444", 
                       annotation_text="🎯 TARGET", annotation_position="bottom right")
forecast_fig.update_traces(line_color='#38bdf8', line_width=4)

# --- 5. GENERATE THE HIGH-END WEB PORTAL ---
table_rows = "".join([f"<tr><td style='padding:12px; border-bottom:1px solid #334155;'>{item['Skill']}</td><td style='padding:12px; border-bottom:1px solid #334155;'>{item['Question']}</td><td style='padding:12px; border-bottom:1px solid #334155; color:#4ade80;'>{item['Tip']}</td></tr>" for item in interview_qa])

html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Saicharan | Career Analytics</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <style>
        body {{ background: #0b1120; color: white; font-family: 'Segoe UI', sans-serif; margin: 0; padding: 20px; text-align: center; }}
        .container {{ max-width: 900px; margin: auto; padding-bottom: 100px; }}
        .card {{ background: #111827; padding: 30px; border-radius: 20px; margin-bottom: 30px; border: 1px solid #1f2937; box-shadow: 0 4px 20px rgba(0,0,0,0.5); }}
        .hero {{ border: 2px solid #38bdf8; }}
        h1 {{ color: #38bdf8; font-size: 2.5rem; margin: 0; }}
        .timestamp {{ font-size: 0.8rem; color: #4ade80; margin-top: 10px; font-weight: bold; }}
        table {{ width: 100%; border-collapse: collapse; margin-top: 20px; background: #1e293b; border-radius: 10px; overflow: hidden; }}
        .btn {{ background: #4ade80; color: #0b1120; border: none; padding: 12px 25px; border-radius: 8px; font-weight: bold; cursor: pointer; transition: 0.3s; }}
        .btn:hover {{ transform: scale(1.05); background: #38bdf8; }}
        .contact-btn {{ position: fixed; bottom: 30px; right: 30px; background: #38bdf8; color: #0b1120; padding: 15px 25px; border-radius: 50px; font-weight: bold; text-decoration: none; z-index: 1000; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="card hero">
            <h1>Saicharan</h1>
            <p style="color: #9ca3af;">Data Scientist @ Hyderabad</p>
            <div class="timestamp">🟢 Live Data: {last_updated}</div>
            <div style="margin-top: 20px; font-size: 1.2rem; color: #fbbf24; font-weight: bold; background: rgba(251, 191, 36, 0.1); padding: 10px; border-radius: 50px; display: inline-block;">
                🚀 Status: Luxury Life Ready
            </div>
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
                alert("Resume Summary Copied! Paste it on your LinkedIn 'About' section.");
            }});
        }}
    </script>
</body>
</html>
"""

# --- 6. SAVE & FINISH ---
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"✅ MISSION COMPLETE: Perfect Day 25 Portal Generated at {last_updated}!")