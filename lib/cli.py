import os
from prettycli import red
from simple_term_menu import TerminalMenu

def start():
    print("Welcome to HABIT TRACKER\n")
    options = ["Sign In", "Sign Up", "Exit"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
   
    print(f"You have selected {options[menu_entry_index]}! ")
    # print("2) Sign Up\n")
    # print("3) Exit\n")

    # user_input = input("Please enter you selection (1 - 3): ")
    # handle_user_input(user_input)


def handle_user_input(user_input):
    if(user_input == "1"):
        print("Option 1")
    elif(user_input == "2"):
        print("option 2")
    elif(user_input == "3"):
        clear_screen()
        start()
    else:
        print(red("Invalid selection.\n"))
        # clear_screen()
        start()
    

def clear_screen():
    os.system("clear")
    

start()