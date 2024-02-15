'''
Sample Code for class
'''
import time

list_of_results = [
    "Something interesting could be said here.", 
    "Here's something else for you.", 
    "The current time is {0}", 
    "What a shame..."
]

# Checks that the results list has enough entries for the number entered.
def exists_in_table(input):
    return int(input) < len(list_of_results)

# Moving the code to a function allows for recursion and trying again.
def main_code_block():
    # Ask the user for input greater than 0.
    user_input = input("Enter a number greater than 0: ")
    if not user_input.isdigit(): 
        print("Please try again, this time entering a number.")
        main_code_block()
        return
    # Changes the input to be an integer value for better reading.
    int_input = int(user_input)
    # Makes sure the number, is infact, greater than 0.
    if int_input <= 0:
        print("Please try again. Your value must be equal to 1 or greater.")
        main_code_block()
    # Checks the number isn't greater than the limit.
    elif int_input >= 9000:
        print("Your number was too great for our code. The power levels are off the charts!!")
        main_code_block()
    # Checks that the number has a result within `list_of_results` and returns the value found.
    elif (exists_in_table(int_input)):
        current_time = time.strftime("%H:%M:%S", time.localtime())
        output = list_of_results[int(int_input-1)].format(current_time)
        print(f"You chose {int_input}. {output}")
    # If the number is greater than the length of the list and is less than 9000, return an apology.
    else:
        print(f"You chose {int_input}. Unfortunately we don't have a result for that. We're so sorry for the inconvenience!")
        main_code_block()

main_code_block()
input("")
# Ask the user for input between 1 and 3
user_input = input("Enter a number between 1 and 3: ")
# Luke Skywalker was here
# Check user input and provide corresponding output
if user_input == '1':
    print("You chose 1. Something interesting could be said here.")
elif user_input == '2':
    print("You chose 2. Here's something else for you.")
elif user_input == '3':
    current_time = time.strftime("%H:%M:%S", time.localtime())
    print(f"You chose 3. The current time is {current_time}.")
elif user_input == '4':
    print("You chose 4. What a shame...")
elif user_input >= 9000:
    print("Your number was too great for our code. The power levels are off the charts!!")
else:
    print("Invalid input. Please enter a number between 1 and 3.")
# Luke Skywalker was here
