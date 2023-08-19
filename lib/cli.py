import os
from prettycli import red
from simple_term_menu import TerminalMenu


def start():
    # print("\n\n\nWelcome to HABIT TRACKER\n".center(700))
    print("""
         _   _    _    ____ ___ _____   _____ ____      _    ____ _  _______ ____
        | | | |  / \  | __ )_ _|_   _| |_   _|  _ \    / \  / ___| |/ / ____|  _ \\
        | |_| | / _ \ |  _ \| |  | |     | | | |_) |  / _ \| |   | ' /|  _| | |_) |
        |  _  |/ ___ \| |_) | |  | |     | | |  _ <  / ___ \ |___| . \| |___|  _ <
        |_| |_/_/   \_\____/___| |_|     |_| |_| \_\/_/   \_\____|_|\_\_____|_| \_\\
        """)

    options = ["Sign In", "Sign Up", "Exit"]
    terminal_menu = TerminalMenu(options)
    menu_index = terminal_menu.show()
    handle_user_input(menu_index+1)


def handle_user_input(user_input):
    if(user_input == 1):
        sign_in()
    elif(user_input == 2):
        print("option 2")
    elif(user_input == 3):
        clear_screen()
    

def clear_screen():
    os.system("clear")
    
def sign_in():
    clear_screen()
    username = input("Please enter username: ")
    print(f"\n\nHello, {username}!")

start()