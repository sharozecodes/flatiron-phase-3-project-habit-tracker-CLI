import os

def start():
    print("Welcome to HABIT TRACKER\n")
    print("1) Sign In\n")
    print("2) Sign Up\n")
    print("3) Exit\n")

    user_input = input("Please enter you selection (1 - 3): ")
    handle_user_input(user_input)


def handle_user_input(user_input):
    if(user_input == "1"):
        print("Option 1")
    elif(user_input == "2"):
        print("option 2")
    elif(user_input == "3"):
        clear_screen()
        start()
    else:
        print("Invalid selection.")
        clear_screen()
        start()
    
