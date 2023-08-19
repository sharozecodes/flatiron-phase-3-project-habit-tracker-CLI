import os
from prettycli import red
from simple_term_menu import TerminalMenu

def start():
    print("Welcome to HABIT TRACKER\n")
    options = ["Sign In", "Sign Up", "Exit"]
    terminal_menu = TerminalMenu(options)
    menu_index = terminal_menu.show()
    handle_user_input(menu_index+1)


def handle_user_input(user_input):
    if(user_input == 1):
        print("Option 1")
    elif(user_input == 2):
        print("option 2")
    elif(user_input == 3):
        clear_screen()
    

def clear_screen():
    os.system("clear")
    

start()