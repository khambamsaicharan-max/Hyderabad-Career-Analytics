# DAY 5: THE WEB GENERATOR
import os

print("--- 🌐 GENERATING YOUR CAREER DASHBOARD ---")

# 1. Your Data
name = "Saicharan"
role = "Data Scientist"
target_salary = 300000
savings = 155000

# 2. The HTML & CSS (The Design)
# We use f""" to write a big block of website code
html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{name}'s Portfolio</title>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0f172a; color: white; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }}
        .card {{ background: #1e293b; padding: 40px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 2px solid #38bdf8; text-align: center; width: 350px; }}
        h1 {{ color: #38bdf8; margin-bottom: 5px; }}
        .role {{ color: #94a3b8; font-style: italic; margin-bottom: 25px; }}
        .stat-box {{ background: #0f172a; padding: 15px; border-radius: 10px; margin: 10px 0; border-left: 4px solid #4ade80; text-align: left; }}
        .label {{ color: #94a3b8; font-size: 12px; text-transform: uppercase; }}
        .value {{ font-size: 20px; font-weight: bold; color: #4ade80; display: block; }}
        .status {{ margin-top: 20px; font-weight: bold; color: #facc15; }}
    </style>
</head>
<body>
    <div class="card">
        <h1>{name}</h1>
        <div class="role">{role} @ Hyderabad</div>
        
        <div class="stat-box">
            <span class="label">Monthly Target</span>
            <span class="value">₹{target_salary:,}</span>
        </div>
        
        <div class="stat-box">
            <span class="label">Projected Savings</span>
            <span class="value">₹{savings:,}</span>
        </div>
        
        <div class="status">🚀 Status: Luxury Life Ready</div>
    </div>
</body>
</html>
"""

# 3. Save as an HTML file
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("\n✅ SUCCESS!")
print("1. Look for 'index.html' in your sidebar.")
print("2. Right-click it and select 'Open in Browser' or 'Reveal in File Explorer'.")
print("3. Double-click the file to see your website!")