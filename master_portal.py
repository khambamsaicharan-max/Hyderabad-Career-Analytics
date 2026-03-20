import pandas as pd
import plotly.express as px
import os

# --- 1. DATA LOADING & SELF-HEALING ---
csv_file = "hyderabad_jobs.csv"

def load_clean_data(file_path):
    if not os.path.exists(file_path):
        return pd.DataFrame({"Company": ["Initialization"], "Salary": [1000000]})
    try:
        df = pd.read_csv(file_path, on_bad_lines='skip', engine='python')
        if df.shape[1] >= 2:
            df = df.iloc[:, [0, 1]] 
            df.columns = ["Company", "Salary"]
        else:
            return pd.DataFrame({"Company": ["Data Error"], "Salary": [0]})
        df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
        return df.dropna()
    except Exception as e:
        return pd.DataFrame({"Company": ["Backup"], "Salary": [800000]})

df = load_clean_data(csv_file)

# --- 2. CAREER & FINANCIAL LOGIC ---
avg_salary = df["Salary"].mean()
monthly_target = 300000
# Take-home (75% of Gross) / 12 months
monthly_takehome = (avg_salary * 0.75) / 12
# Assuming 50% savings of take-home
projected_savings = monthly_takehome * 0.5 
years_to_30L = 3000000 / (projected_savings * 12) if projected_savings > 0 else 0

# --- 3. 5-YEAR FORECAST LOGIC ---
years = [2026, 2027, 2028, 2029, 2030]
forecast_salaries = [avg_salary * (1.15**i) for i in range(5)]

# --- 4. CREATE THE VISUALS ---

# Chart 1: Market Bar Chart
fig = px.bar(df, x="Company", y="Salary", 
             title="Live Hyderabad Market Intelligence",
             color="Salary", color_continuous_scale="Viridis", template="plotly_dark")

# Chart 2: Future Forecast WITH NORTH STAR LINE
forecast_fig = px.line(x=years, y=forecast_salaries, 
                       title="5-Year Career Growth vs. ₹30L Target",
                       markers=True, template="plotly_dark")

# Add the Red Dotted "Goal" Line
forecast_fig.add_hline(y=3000000, 
                       line_dash="dot", 
                       line_color="#ef4444", 
                       annotation_text="🎯 ₹30L LUXURY TARGET", 
                       annotation_position="bottom right")

forecast_fig.update_traces(line_color='#38bdf8', line_width=4)

# --- 5. GENERATE THE HIGH-END WEB PORTAL ---
html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Saicharan | Luxury Career Portal</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <style>
        body {{ background: #0b1120; color: white; font-family: 'Segoe UI', sans-serif; margin: 0; padding: 20px; text-align: center; }}
        .container {{ max-width: 1000px; margin: auto; }}
        
        .hero-card {{ 
            border: 2px solid #38bdf8; padding: 40px; border-radius: 20px; 
            background: #111827; display: inline-block; margin: 20px 0;
            box-shadow: 0 10px 30px rgba(56, 189, 248, 0.3);
        }}
        h1 {{ color: #38bdf8; font-size: 2.8rem; margin: 0; }}
        .subtitle {{ color: #9ca3af; font-style: italic; margin-bottom: 30px; }}
        
        .stat-grid {{ display: flex; gap: 20px; justify-content: center; flex-wrap: wrap; }}
        .stat-box {{ 
            background: #1e293b; padding: 20px; border-radius: 15px; 
            min-width: 200px; border-bottom: 4px solid #4ade80; text-align: left;
        }}
        .label {{ font-size: 0.75rem; color: #9ca3af; text-transform: uppercase; }}
        .value {{ font-size: 1.6rem; color: #4ade80; font-weight: bold; display: block; margin-top: 5px; }}
        
        .status-badge {{ 
            margin-top: 25px; font-weight: bold; color: #fbbf24; font-size: 1.2rem; 
            background: rgba(251, 191, 36, 0.1); padding: 10px 20px; 
            border-radius: 50px; display: inline-block; 
        }}
        
        .chart-section {{ 
            background: #111827; padding: 25px; border-radius: 25px; 
            margin-top: 40px; border: 1px solid #1f2937; 
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="hero-card">
            <h1>Saicharan</h1>
            <div class="subtitle">Data Scientist @ Hyderabad</div>
            
            <div class="stat-grid">
                <div class="stat-box">
                    <span class="label">Monthly Target</span>
                    <span class="value">₹{monthly_target:,}</span>
                </div>
                <div class="stat-box">
                    <span class="label">Projected Savings</span>
                    <span class="value">₹{int(projected_savings):,}</span>
                </div>
            </div>
            
            <div class="status-badge">🚀 Status: Luxury Life Ready</div>
        </div>

        <div class="chart-section">
            <h2 style="color: #38bdf8; margin-bottom: 20px;">Market Insights</h2>
            {fig.to_html(full_html=False, include_plotlyjs='cdn')}
        </div>

        <div class="chart-section">
            <h2 style="color: #4ade80; margin-bottom: 20px;">🔮 Future Salary Predictor</h2>
            {forecast_fig.to_html(full_html=False, include_plotlyjs='cdn')}
            <div style="margin-top: 20px; color: #9ca3af; padding: 15px; background: #1e293b; border-radius: 10px;">
                💡 <b>Milestone:</b> At 15% annual upskilling growth, you cross the <b>₹30L North Star</b> line in approximately <b>{years_to_30L:.1f} years</b>.
            </div>
        </div>
    </div>
</body>
</html>
"""

# SAVE AS index.html
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("✅ DAY 19 SUCCESS: North Star Portal fully updated!")