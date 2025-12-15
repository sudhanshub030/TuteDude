# Task 1: Perform Basic Mathematical Operations
# Problem Statement: Write a Python program that does the following:
# 1.  Takes two numbers as input from the user.
# 2.  Performs the basic mathematical operations on these two numbers:
# o	Addition
# o	Subtraction
# o	Multiplication
# o	Division
# 3.  Displays the results of each operation on the screen.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum = a + b
print("Addition:", sum)

diff = a - b
print("Subtraction:", diff)

prod = a * b
print("Multiplication:", prod)

div = a / b
print("Division:", div)

# Task 2: Create a Personalized Greeting
# Problem Statement: Write a Python program that:
# 1.  Takes a user's first name and last name as input.
# 2.  Concatenates the first name and last name into a full name.
# 3.  Prints a personalized greeting message using the full name.


name = input("Enter your name: ")
last = input("Enter your last name: ")

print(f"Hello, {name} {last}! Welcome to Python programming.")