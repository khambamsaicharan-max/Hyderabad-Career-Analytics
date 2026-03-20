# DAY 4: HYDERABAD PORTFOLIO PROJECT
print("--- 🏦 SAVING YOUR HYDERABAD PLAN ---")

# 1. Real-world Data
name = "Saicharan"
salary = 200000 
rent = 45000
savings = salary - rent

# 2. Designing the Report
report_layout = f"""
==========================================
        HYDERABAD CAREER REPORT 2026
==========================================
CANDIDATE: {name}
TARGET SALARY: ₹{salary:,}
ESTIMATED RENT: ₹{rent:,}
------------------------------------------
MONTHLY SAVINGS: ₹{savings:,}
ANNUAL SAVINGS:  ₹{savings * 12:,}
==========================================
STATUS: READY FOR LUXURY LIFE IN KOKAPET
==========================================
"""

# 3. Saving to a professional filename
with open("hyderabad_plan.txt", "w",encoding="utf-8") as f:
    f.write(report_layout)

print("\n✅ PROJECT COMPLETE!")
print("Check your sidebar for 'hyderabad_plan.txt'.")