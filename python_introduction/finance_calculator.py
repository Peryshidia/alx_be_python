monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Calculate annual savings with 5% interest
annual_savings = monthly_savings * 12
interest_rate = 0.05
interest_earned = annual_savings * interest_rate
projected_annual_savings = annual_savings + interest_earned

# Display results
print(f"\nYour monthly savings: ${monthly_savings:.2f}")
print(f"Projected annual savings (with 5% interest): ${projected_annual_savings:.2f}") 