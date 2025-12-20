# Task 1: Check if a Number is Even or Odd
# Problem Statement:  Write a Python program that:
# 1. 	Takes an integer input from the user.
# 2. 	Checks whether the number is even or odd using an if-else statement.
# 3. 	Displays the result accordingly

num = int(input("Enter an integer: "))
if num%2 == 0:
    print(f"{num} is an Even number.")
else:
    print(f"{num} is an Odd number.")
    
    
    
    
# Task 2: Sum of Integers from 1 to 50 Using a Loop
 
# Problem Statement: Write a Python program that:
# 1.   Uses a for loop to iterate over numbers from 1 to 50.
# 2.   Calculates the sum of all integers in this range.
# 3.   Displays the final sum.

total = 0
for i in range(1,51):
    total = total + i
print("The sum of integers from 1 to 50 is:", total)
