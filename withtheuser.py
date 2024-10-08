# Start by defining a function to calculate and display the budget breakdown
def budget_breakdown():
    # Prompt the user to enter their total budget
    total_budget = float(input("Enter your total budget: "))

    # Initialize a dictionary to store spending categories and their amounts
    categories = {
        "Housing": 0,
        "Utilities": 0,
        "Groceries": 0,
        "Transportation": 0,
        "Health Care": 0,
        "Personal Care": 0,
        "Clothing": 0,
        "Debt": 0,
    }

    # Loop through each category to get user input
    for category in categories:
        amount = float(input(f"Enter amount spent on {category}: "))
        categories[category] = amount

    # Calculate and print the percentage of total budget each category represents
    print("\nBudget Breakdown:")
    for category, amount in categories.items():
        percentage = (amount / total_budget) * 100
        print(f"{category}: ${amount:.2f} ({percentage:.2f}%)")

# Call the function to run the program
budget_breakdown()
