# Problem Set 1C
# Name: Brandon Tan
# Time Spent: 50 minutes

# Get user input for yearly_salary, portion_saved and cost_of_dream_home below
initial_deposit = float(input("Enter the initial deposit: "))

cost_of_house = 800000
down_payment = 0.25 * cost_of_house
months = 36

epsilon = 100
high = 1.0
low = 0


if initial_deposit >= down_payment - epsilon:
    print("The best rate of return is 0.0%. You already have sufficient savings.")
else:
    steps = 0
    best_r = None
    while high - low > 1e-7:
        steps += 1
        middle = (high + low) / 2
        total_savings = initial_deposit
        for _ in range(months):
            total_savings += total_savings * (middle / 12)  # Monthly return

        # Check if the savings are within the acceptable range
        if abs(total_savings - down_payment) <= epsilon:
            best_r = middle
            break
        elif total_savings < down_payment:
            # Savings are too low, need a higher rate
            low = middle
        else:
            # Savings are too high, need a lower rate
            high = middle

    # Output the result
    print(f"Best savings rate: {best_r}")
    print(f"Steps in bisection search: {steps}")
