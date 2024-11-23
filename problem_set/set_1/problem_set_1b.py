# Problem Set 1B
# Name: Brandon Tan
# Time Spent: 50 minutes

# Get user input for yearly_salary, portion_saved and cost_of_dream_home below
yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))


# Initialize other variables you need (if any) for your program below
amount_saved = 0
months = 0
portion_down_payment = cost_of_dream_home * 0.25
print("Down payment needed for the dream home: %s" % portion_down_payment)
monthly_savings = (yearly_salary / 12) * portion_saved

while amount_saved < portion_down_payment:
    if months % 6 == 0 and months != 0:
        yearly_salary = yearly_salary * (semi_annual_raise + 1)
        monthly_savings = (yearly_salary / 12) * portion_saved
    interest = amount_saved * (0.05 / 12)
    amount_saved = interest + (monthly_savings + amount_saved)
    months += 1


# Determine how many months it would take to get the down payment for your dream home below
print("Total amount saved: %s" % amount_saved)
print("Number of months: %s" % months)
