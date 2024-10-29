# Step 1: Define the factorial function
def factorial(n):
    # Base case: If n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: Multiply n by the factorial of n-1
    else:
        return n * factorial(n - 1)

# Step 2: Create the main function
def main():
    # Prompt the user to enter a non-negative integer
    num = int(input("Enter a non-negative integer: "))
    # Call the factorial function and store the result
    result = factorial(num)
    # Print the result in the required format
    print(f"The factorial of {num} is {result}.")

# Step 3: Call the main function to run the program
if __name__ == "__main__":
    main()
