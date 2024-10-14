# Simple Python program to calculate the square of a number with error handling
def square_number():
    try:
        # Prompt the user for input
        number = input("Enter a number to square: ")
        # Convert the input to an integer
        squared_number = int(number) ** 2
        # Print the result
        print(f"The square of {number} is {squared_number}.")
    except ValueError:
        # Handle the error if the input is not an integer
        print("Invalid input. Please enter a valid number.")

# Call the function to run the program
square_number()

