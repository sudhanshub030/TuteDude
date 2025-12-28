# Task 1: Create a Dictionary of Student Marks

# Problem Statement: Write a Python program that:
# 1.   Creates a dictionary where student names are keys and their marks are values.
# 2.   Asks the user to input a student's name.
# 3.   Retrieves and displays the corresponding marks.
# 4.   If the student’s name is not found, display an appropriate message.

students = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92
}
name = input("Enter the student's name: ")
if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print("Student not found.")


# Problem Statement: Write a Python program that:
# 1.   Creates a list of numbers from 1 to 10.
# 2.   Extracts the first five elements from the list.
# 3.   Reverses these extracted elements.
# 4.   Prints both the extracted list and the reversed list

number = list(range(1,11))
extracted = number[:5]
reversed_list = extracted[::-1]
print("Extracted list:", extracted)
print("Reversed list:", reversed_list)