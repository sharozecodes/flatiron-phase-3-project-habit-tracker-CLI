
def start():
    print("Welcome to HABIT TRACKER\n")
    print("1) Sign In\n")
    print("2) Sign Up\n")
    print("3) Exit\n")

    user_input = input("Please enter you selection (1 - 3): ")
    handle_user_input(user_input)


def handle_user_input(user_input):
    if(user_input == 1):
        sign_in()
    elif(user_input == 1):
        sign_up()
    elif(user_input == 1):
        exit_menu()
    else:
        print("Invalid selection.")
        clear_screen()
        start()