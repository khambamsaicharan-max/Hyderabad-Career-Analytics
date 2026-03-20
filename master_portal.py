import pandas as pd
import plotly.express as px
import os

# --- 1. DATA LOADING ---
csv_file = "hyderabad_jobs.csv"
def load_clean_data(file_path):
    if not os.path.exists(file_path):
        return pd.DataFrame({"Company": ["Initialization"], "Salary": [1000000]})
    try:
        df = pd.read_csv(file_path, on_bad_lines='skip', engine='python')
        if df.shape[1] >= 2:
            df = df.iloc[:, [0, 1]] 
            df.columns = ["Company", "Salary"]
        df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
        return df.dropna()
    except:
        return pd.DataFrame({"Company": ["Backup"], "Salary": [800000]})

df = load_clean_data(csv_file)

# --- 2. LOGIC & FORECAST ---
avg_salary = df["Salary"].mean()
monthly_target, monthly_takehome = 300000, (avg_salary * 0.75) / 12
projected_savings = monthly_takehome * 0.5 
years_to_30L = 3000000 / (projected_savings * 12) if projected_savings > 0 else 0
years = [2026, 2027, 2028, 2029, 2030]
forecast_salaries = [avg_salary * (1.15**i) for i in range(5)]

# --- 3. INTERVIEW DATA ---
interview_qa = [
    {"Skill": "Python", "Question": "How do you handle memory management?", "Tip": "Mention Garbage Collector."},
    {"Skill": "SQL", "Question": "WHERE vs HAVING?", "Tip": "WHERE filters rows; HAVING filters groups."},
    {"Skill": "Power BI", "Question": "Calculated Columns vs Measures?", "Tip": "Columns = row-level; Measures = aggregates."}
]

# --- 4. VISUALS ---
fig = px.bar(df, x="Company", y="Salary", title="Market Intelligence", template="plotly_dark")
forecast_fig = px.line(x=years, y=forecast_salaries, title="5-Year Growth", markers=True, template="plotly_dark")
forecast_fig.add_hline(y=3000000, line_dash="dot", line_color="#ef4444")

# --- 5. THE HTML PORTAL ---
# We build the table rows using a loop inside the f-string
table_rows = "".join([f"""
    <tr>
        <td style='padding:12px; border-bottom:1px solid #334155;'>{item['Skill']}</td>
        <td style='padding:12px; border-bottom:1px solid #334155;'>{item['Question']}</td>
        <td style='padding:12px; border-bottom:1px solid #334155; color:#4ade80;'>{item['Tip']}</td>
    </tr>
""" for item in interview_qa])

html_template = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Saicharan | Interview Ready</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <style>
        body {{ background: #0b1120; color: white; font-family: sans-serif; text-align: center; padding: 20px; }}
        .container {{ max-width: 900px; margin: auto; }}
        .card {{ background: #111827; padding: 25px; border-radius: 20px; margin-bottom: 30px; border: 1px solid #1f2937; }}
        table {{ width: 100%; border-collapse: collapse; margin-top: 20px; background: #1e293b; border-radius: 10px; overflow: hidden; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="card" style="border: 2px solid #38bdf8;">
            <h1>Saicharan</h1>
            <p>🚀 Status: Luxury Life Ready (Target: ₹30L)</p>
        </div>

        <div class="card">
            {fig.to_html(full_html=False, include_plotlyjs='cdn')}
        </div>

        <div class="card">
            {forecast_fig.to_html(full_html=False, include_plotlyjs='cdn')}
        </div>

        <div class="card" style="border-top: 4px solid #fbbf24; text-align: left;">
            <h2 style="color: #fbbf24;">🎯 Interview Preparation Edge</h2>
            <table>
                <tr style="background: #334155; color: #fbbf24;">
                    <th style="padding: 12px;">Skill</th>
                    <th style="padding: 12px;">Question</th>
                    <th style="padding: 12px;">Expert Tip</th>
                </tr>
                {table_rows}
            </table>
        </div>
    </div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_template)
print("✅ DAY 21 COMPLETE: Interview Table Added!")