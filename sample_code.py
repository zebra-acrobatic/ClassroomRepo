    # Ask the user for input between 1 and 3
    user_input = input("Enter a number between 1 and 3: ")

    # Check user input and provide corresponding output
    if user_input == '1':
        print("You chose 1. Something interesting could be said here.")
    elif user_input == '2':
        print("You chose 2. Here's something else for you.")
    elif user_input == '3':
        current_time = time.strftime("%H:%M:%S", time.localtime())
        print(f"You chose 3. The current time is {current_time}.")
    else:
        print("Invalid input. Please enter a number between 1 and 3.")
