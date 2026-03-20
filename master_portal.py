import pandas as pd
import plotly.express as px
import os

# --- 1. DATA LOADING & SELF-HEALING ---
csv_file = "hyderabad_jobs.csv"

def load_clean_data(file_path):
    if not os.path.exists(file_path):
        return pd.DataFrame({"Company": ["Initialization"], "Salary": [1000000]})
    
    try:
        # 'on_bad_lines' skips the rows with too many commas (like your Line 6 error)
        df = pd.read_csv(file_path, on_bad_lines='skip', engine='python')
        
        # Ensure we have exactly 2 columns: Company and Salary
        if df.shape[1] >= 2:
            df = df.iloc[:, [0, 1]] 
            df.columns = ["Company", "Salary"]
        else:
            return pd.DataFrame({"Company": ["Data Error"], "Salary": [0]})

        # Convert Salary to numbers (removes any text accidentally scraped)
        df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
        return df.dropna()
    
    except Exception as e:
        print(f"⚠️ Error cleaning data: {e}")
        return pd.DataFrame({"Company": ["Backup"], "Salary": [800000]})

df = load_clean_data(csv_file)

# --- 2. CAREER & FINANCIAL LOGIC ---
avg_salary = df["Salary"].mean()
monthly_target = 300000
# Take-home (approx 75% after tax) divided by 12 months
monthly_takehome = (avg_salary * 0.75) / 12
projected_savings = monthly_takehome * 0.5  # Saving 50%
years_to_30L = 3000000 / (projected_savings * 12) if projected_savings > 0 else 0

# --- 3. CREATE THE VISUALS ---
fig = px.bar(df, x="Company", y="Salary", 
             title="Live Hyderabad Market Intelligence",
             color="Salary", 
             color_continuous_scale="Viridis",
             template="plotly_dark")

# --- 4. GENERATE THE HIGH-END WEB PORTAL ---
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
        .label {{ font-size: 0.75rem; color: #9ca3af; text-transform: uppercase; letter-spacing: 1px; }}
        .value {{ font-size: 1.6rem; color: #4ade80; font-weight: bold; display: block; margin-top: 5px; }}
        
        .status-badge {{ margin-top: 25px; font-weight: bold; color: #fbbf24; font-size: 1.2rem; background: rgba(251, 191, 36, 0.1); padding: 10px 20px; border-radius: 50px; display: inline-block; }}
        
        .chart-section {{ background: #111827; padding: 25px; border-radius: 25px; margin-top: 40px; border: 1px solid #1f2937; }}
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
            <h2 style="color: #38bdf8; margin-bottom: 20px;">Market Insights & Salaries</h2>
            {fig.to_html(full_html=False, include_plotlyjs='cdn')}
            <div style="margin-top: 20px; color: #9ca3af; padding: 15px; background: #1e293b; border-radius: 10px;">
                💡 <b>Strategy:</b> At this rate, your ₹30 Lakhs Asset Goal is achievable in <b>{years_to_30L:.1f} years</b>.
            </div>
        </div>
    </div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("✅ DAY 17 SUCCESS: Portal Rebuilt with Self-Healing Logic!")