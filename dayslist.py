days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

steps_per_day = []

for i in range(len(days_of_week)):
    day = days_of_week[i]
    steps = int(input(f"Enter steps for {day}: "))
    steps_per_day.append(steps)

    print(f"{day} has {steps} steps")

total_steps = sum(steps_per_day) # sum() is a built-in function that calculates the sum of all elements in a list

print(f"Total steps: {t0tal_steps}")



