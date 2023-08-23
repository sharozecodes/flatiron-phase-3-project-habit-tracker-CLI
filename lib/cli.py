import os
import time
from prettycli import red
from simple_term_menu import TerminalMenu
from queries import *

def logo():
    clear_screen()
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

def sign_in():
    logo()
    username = input("\n\nPlease enter username: ")
    user = find_by_username(username)
    if user:
        habit_menu(user.id)
    else:
        error_message("Username", "main")
        start()

    

def sign_up():
    logo()
    username = input("\n\nPlease enter a username: ")
    name = input("\n\nPlease enter name: ")
    new_user(username, name)
    clear_screen()
    print(f"\nHello, {username}!\n\n")

def habit_menu(user_id):
    logo()
    print(f"User id:", user_id)
    options = ["Add a habit", "Search a habit", "View all habits", "Go back"]
    terminal_menu = TerminalMenu(options)
    menu_index = terminal_menu.show()
    if(menu_index == 0):
        logo()
        title = input("\n\nPlease enter the habit title: ")
        frequency = input("\n\nPlease enter the reminding frequency: ")
        add_habit(title=title, frequency=frequency, user_id=user_id)
        clear_screen()
    elif(menu_index == 1):
        logo()
        title = input("\n\nPlease enter the habit title: ")
        matching_habits = find_by_habit(title, user_id=user_id)
        if matching_habits:
            habit = make_habit_menu(matching_habits=matching_habits)
            print(habit)
        else:
            error_message("Habit", "habit")
            habit_menu(user_id)
    elif(menu_index == 2):
        selected_habit = make_habit_menu(view_all_habit(user_id=user_id))
        print(selected_habit)
    else:
        print("Go back")

def error_message(record_name, menu):
    print(f"\n{red(f'{record_name} not found.')}\n\nRedirecting you to the {menu} menu...")
    time.sleep(3)

def make_habit_menu(matching_habits):
    habit_options = []
    for habit in matching_habits:
        habit_options.append(habit.title)
    terminal_menu = TerminalMenu(habit_options)
    habit_index = terminal_menu.show()
    return matching_habits[habit_index]

def main():
    start()

if __name__ == '__main__':
    main()