# Task 1: Read a File and Handle Errors
# Problem Statement:  Write a Python program that:
# 1.   Opens and reads a text file named sample.txt.
# 2.   Prints its content line by line.
# 3.   Handles errors gracefully if the file does not exist.

# try:
#     print("This is a simple text file.")
#     print("It contains multiple lines.")
#     with open('sample.txt', 'rt') as fh:
#         for line in fh:
#             print(line.strip())  # print each line without extra newline
# except FileNotFoundError:
#     print("Error : The fle 'sample.txt' was not found.")



# Task 2: Write and Append Data to a File
# Problem Statement: Write a Python program that:
# 2.   Appends additional data to the same file.
# 3.   Reads and displays the final content of the file.


# Task 2: Write and Append Data to a File

# Step 1: Take user input and write it to output.txt
text = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(text + "\n")
print("Data successfully written to output.txt.\n")

# Step 2: Append additional user input
append_text = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(append_text + "\n")
print("Data successfully appended.\n")

# Step 3: Read and display final content of the file
print("Final content of output.txt:")
with open("output.txt", "r") as file:
    print(file.read())
