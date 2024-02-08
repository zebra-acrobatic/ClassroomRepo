'''
Sample Code for class
'''
import time

# Ask the user for input between 0 and 2
user_input = input("Enter a number between 0 and 2: ")

# Check user input and provide corresponding output
if user_input == '0':
    print("You chose 1. Something interesting could be said here.")
elif user_input == '1':
    print("You chose 2. Here's something else for you.")
elif user_input == '2':
    current_time = time.strftime("%H:%M:%S", time.localtime())
    print(f"You chose 2. The current time is {current_time}.")
else:
    print("Invalid input. Please enter a number between 0 and 2.")
