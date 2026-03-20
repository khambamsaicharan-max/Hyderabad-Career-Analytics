# DAY 2.5: THE HYDERABAD WEALTH TRACKER (LOOPS)
print("--- 🚀 12-MONTH SAVINGS PROJECTION ---")

name = "Saicharan"
monthly_salary = 200000
monthly_rent = 45000  # Luxury flat in Financial District
other_expenses = 35000

monthly_savings = monthly_salary - (monthly_rent + other_expenses)
total_wealth = 0

print(f"\nMonth-by-Month Growth for {name}:")

# This "Loop" repeats the code 12 times automatically
for month in range(1, 37):
    total_wealth = total_wealth + monthly_savings
    print(f"Month {month}: Total Savings = ₹{total_wealth:,}")

print(f"\n💰 After 1 year, you will have ₹{total_wealth:,} in your bank!")