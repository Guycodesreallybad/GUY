# Define a bmi function that takes weight and height as arguments and returns the bmi value. 
def bmi(weight,height): 
    return weight / height ** 2
# Prompt the user for input
weight =float(input('Enter weight in kg: ')) 
height = float(input('Enter height in meters: '))
# Calculate the BMI
bmi_value = bmi(weight, height)
print(f'Your BMI is {bmi_value}')
