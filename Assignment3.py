# Task 1: Calculate Factorial Using a Function 


# Problem Statement: Write a Python program that:
# 1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
# 2.   Returns the calculated factorial.
# 3.   Calls the function with a sample number and prints the output.



def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter the number: "))
result = factorial(num)
print(f"Factorial of {num} is {result}.")


# Task 2: Using the Math Module for Calculations
 
# Problem Statement: Write a Python program that:
# 1.   Asks the user for a number as input.
# 2.   Uses the math module to calculate the:
# o   Square root of the number
# o   Natural logarithm (log base e) of the number
# o   Sine of the number (in radians)
# 3.   Displays the calculated results.

import math
num = int(input("Enter a number : "))
result = math.sqrt(num)
natural_log = math.log(num)
sine_value = math.sin(num)

print(f"Square root of {num} is: {result}.")
print(f"Natural logarithm (log base e) of {num} is: {natural_log}")
print(f"Sine of {num} radians is: {sine_value}")
