import os
from prettycli import red
from simple_term_menu import TerminalMenu
from queries import new_user

def logo():
    print("""
         _   _    _    ____ ___ _____   _____ ____      _    ____ _  _______ ____
        | | | |  / \  | __ )_ _|_   _| |_   _|  _ \    / \  / ___| |/ / ____|  _ \\
        | |_| | / _ \ |  _ \| |  | |     | | | |_) |  / _ \| |   | ' /|  _| | |_) |
        |  _  |/ ___ \| |_) | |  | |     | | |  _ <  / ___ \ |___| . \| |___|  _ <
        |_| |_/_/   \_\____/___| |_|     |_| |_| \_\/_/   \_\____|_|\_\_____|_| \_\\
        """)

def start():
    logo()
    options = ["Sign In", "Sign Up", "Exit"]
    terminal_menu = TerminalMenu(options)
    menu_index = terminal_menu.show()
    handle_user_input(menu_index+1)


def handle_user_input(user_input):
    if(user_input == 1):
        sign_in()
    elif(user_input == 2):
        sign_up()
    elif(user_input == 3):
        clear_screen()
        print("\n\nGood bye!\n\n")
    

def clear_screen():
    os.system("clear")
    logo()

def sign_in():
    clear_screen()
    username = input("\n\nPlease enter username: ")
    clear_screen()
    print(f"\nHello, {username}!\n\n")

def sign_up():
    clear_screen()
    username = input("\n\nPlease enter a username: ")
    name = input("\n\nPlease enter name: ")
    new_user(username, name)
    clear_screen()
    print(f"\nHello, {username}!\n\n")


def main():
    start()

if __name__ == '__main__':
    main()