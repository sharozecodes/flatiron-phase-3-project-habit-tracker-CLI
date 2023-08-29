import os
import time
from prettycli import red, green, blue
from simple_term_menu import TerminalMenu
from queries import *
import time


def logo():
    clear_screen()
    print(blue("""
        ██   ██  █████  ██████  ██ ████████     ████████ ██████   █████   ██████ ██   ██ ███████ ██████  
        ██   ██ ██   ██ ██   ██ ██    ██           ██    ██   ██ ██   ██ ██      ██  ██  ██      ██   ██ 
        ███████ ███████ ██████  ██    ██           ██    ██████  ███████ ██      █████   █████   ██████  
        ██   ██ ██   ██ ██   ██ ██    ██           ██    ██   ██ ██   ██ ██      ██  ██  ██      ██   ██ 
        ██   ██ ██   ██ ██████  ██    ██           ██    ██   ██ ██   ██  ██████ ██   ██ ███████ ██   ██ 
        \n"""))
def start():
    logo()
    options = ["Sign In", "Sign Up", "Exit"]
    terminal_menu = TerminalMenu(options)
    menu_index = terminal_menu.show()
    handle_user_input(menu_index)

def handle_user_input(user_input):
    if(user_input == 0):
        sign_in()
    elif(user_input == 1):
        sign_up()
    elif(user_input == 2):
        logo()
        print("\nSee you later!\n")    

def clear_screen():
    os.system("clear")

def sign_in():
    logo()
    username = input("\nPlease enter username: ")
    user = find_by_username(username)
    if user:
        habit_menu(user.id)
    else:
        error_message("Username", "main")
        start()

def sign_up():
    logo()
    username = input("\nPlease enter a username: ")
    if (username.strip() == ''):
        print(red("\nUsername input cannot be empty"))
        time.sleep(3)
        sign_up()

    elif (len(username) > 9):
        print(red("\nUsername cannot be greater than 9 characters"))
        time.sleep(3)
        sign_up()

    elif check_username(username=username):
        name = input("\nPlease enter name: ")
        user = new_user(username, name)
        print(green("\nUser added successfully!"))
        print_name(user.id)    
        habit_menu(user.id)

    else:
        print(red("\nUsername already in use"))
        print("\nPlease enter a different username\n")
        time.sleep(3)
        sign_up()
    

def habit_menu(user_id):
    logo()
    print(f"user id: {user_id}")
    options = ["Add a habit", "Search a habit", "View all habits", "Go back"]
    terminal_menu = TerminalMenu(options)
    menu_index = terminal_menu.show()
    if(menu_index == 0):
        title = habit_checker()
        frequency = frequency_checker()
        add_habit(title=title, frequency=frequency, user_id=user_id)
        clear_screen()
        logo()
        redirect_to_habit_menu(user_id, "registered")
    elif(menu_index == 1):
        logo()
        title = input("\nPlease enter the habit title: ")
        matching_habits = find_by_habit(title, user_id=user_id)
        if (matching_habits == []):
            error_message("Habits", "habit")
            habit_menu(user_id)
        elif matching_habits:
            habit = make_habit_menu(matching_habits)
            habit_sub_menu(user_id, habit.id)
        else:
            error_message("Habit", "habit")
            habit_menu(user_id)

    elif(menu_index == 2):
        habit_matches = view_all_habit(user_id=user_id)
        if (habit_matches == []):
            error_message("Habits", "habit")
            habit_menu(user_id)
        elif habit_matches:
            selected_habit = make_habit_menu(habit_matches)
            habit_sub_menu(user_id, selected_habit.id)
        else:
            habit_menu(user_id)
    else:
        start()

def error_message(record_name, menu):
    print(red(f'\n{record_name} not found!'))
    print(f"\nRedirecting you to the {menu} menu...")
    time.sleep(3)

def make_habit_menu(matching_habits):

    habit_options = [habit.title for habit in matching_habits]
    terminal_menu = TerminalMenu(habit_options)
    habit_index = terminal_menu.show()
    return matching_habits[habit_index]

def habit_sub_menu(user_id, habit_id):
    logo()
    current_streak = view_streak(habit_id)
    print(blue(f"Hey! You're current streak is: {current_streak}\n"))
    options = ["Check In", "Edit habit", "Delete habit", "Reset streak", "Back"]
    terminal_menu = TerminalMenu(options)
    menu_index = terminal_menu.show()
    if(menu_index == 0):
        checked_in = check_in(habit_id)
        if checked_in:
            redirect_to_habit_menu(user_id, "checked in")
        else:
            print("\nYou are already checked in for this interval")
            redirect_to_habit_menu(user_id, "new_check_in")

    elif(menu_index == 1):
        habit_title = habit_checker()   
        habit_frequency = frequency_checker()
        edit_habit(habit_id=habit_id, title=habit_title, frequency=habit_frequency)
        redirect_to_habit_menu(user_id, "updated")

    elif(menu_index == 2):
        logo()
        print(red("Are you sure you want to delete this habit?"))
        options = ["Yes", "No"]
        terminal_menu = TerminalMenu(options)
        menu_index = terminal_menu.show()
        if (menu_index == 0):
            delete_habit(habit_id=habit_id)
            redirect_to_habit_menu(user_id, "deleted")
        else:
            logo()
            print("cancelling deletion...")
            redirect_to_habit_menu(user_id, "no")

    elif(menu_index == 3):
        reset_habit(habit_id=habit_id)
        redirect_to_habit_menu(user_id, "reset to zero")

    else:
        habit_menu(user_id)

def redirect_to_habit_menu(user_id, update):
    if (update != "new_check_in" and update != "no"):
        print(green(f"\nHabit successfully {update}"))
    time.sleep(3)
    habit_menu(user_id)

def habit_checker():
    while True:
        logo()
        title = input("Please enter the habit title: ")
        if (title.strip() == ''):
            print(red("\nHabit input cannot be empty"))
            time.sleep(3)
            continue
        else:
            return title

def frequency_checker():
    while True:
        try:
            frequency = int(input("\nPlease enter the reminding frequency (in hours): "))
            return frequency
        except ValueError:
            print(red("\nPlease enter an integer"))

def main():
    start()

if __name__ == '__main__':
    main()