# define the function that calculates the BMI
def calculate_bmi(weight, height):
  # BMI formula
  bmi = weight / (height * height)

  # check if the BMI is within a healthy range
  if bmi < 18.5:
    status = "underweight"
  elif bmi >= 18.5 and bmi <= 25:
    status = "healthy"
  elif bmi > 25 and bmi <= 30:
    status = "overweight"
  else:
    status = "obese"

  # return the calculated BMI and status
  return bmi, status

# ask the user to input their weight and height
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# check for invalid input (i.e. non-positive numbers)
if weight <= 0 or height <= 0:
  print("Invalid input. Weight and height must be positive numbers.")
else:
  # calculate the BMI and status
  bmi, status = calculate_bmi(weight, height)

  # print the BMI and status
  print("Your BMI is:", bmi)
  print("Based on your BMI, you are considered", status)
