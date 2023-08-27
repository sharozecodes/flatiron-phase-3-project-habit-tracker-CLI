import os
import time
from prettycli import red, green, blue
from simple_term_menu import TerminalMenu
from queries import *
import time

engine = create_engine("sqlite:///db/habittracker.db")
Session = sessionmaker(bind=engine)
session = Session()


def logo():
    os.system("clear")
    print(green("""
        ██   ██  █████  ██████  ██ ████████     ████████ ███████ ███████ ████████ ███████ ██████  
        ██   ██ ██   ██ ██   ██ ██    ██           ██    ██      ██         ██    ██      ██   ██ 
        ███████ ███████ ██████  ██    ██           ██    █████   ███████    ██    █████   ██████  
        ██   ██ ██   ██ ██   ██ ██    ██           ██    ██           ██    ██    ██      ██   ██ 
        ██   ██ ██   ██ ██████  ██    ██           ██    ███████ ███████    ██    ███████ ██   ██
        """))
def get_all_users():
    return session.query(User).all()

def get_user_id(user_ids):
    while True:
        logo()
        user_id = input("Please enter the user id: ")
        if user_id not in user_ids:
            print(red("\ninvalid user id"))
            time.sleep(1)
            continue
        elif (view_all_habit(user_id) == []):
            print(red("\nNo assigned habits"))
            time.sleep(1)
            continue
        else:
            return int(user_id)
        
def get_habit_id(user_id):
    habits = view_all_habit(user_id)
    habit_ids = []
    for habit in habits:
        print(blue(f"\nHabit ID: {habit.id}"))
        print(blue(f"Habit title: {habit.title}"))
        habit_ids.append(str(habit.id))
    print("\n-----------------------------\n")
    while True:
        habit_id = input("Please enter the habit id: ")
        if habit_id not in habit_ids:
            print(red("invalid habit id\n"))
            continue
        else:
            return int(habit_id)
        
def get_hours():
    while True:
        try:
            hours = int(input("Please enter the whole hours to add to check in: "))
            return hours
        except ValueError:
            print(red("\nPlease enter an integer"))

def update_checkin(habit_id, hours):
    query = session.query(Habit).filter_by(id=habit_id).first()
    query.last_checked_in += (hours * 3600)
    session.commit()
    print(green(f"\nCheck in set to {hours} hours ({hours*3600} seconds) ahead"))
    time.sleep(3)
    
        
def start():
    logo()
    users = get_all_users()
    user_ids = []
    for user in users:
        user_ids.append(str(user.id))

    user_id = get_user_id(user_ids)
    habit_id = get_habit_id(user_id)
    hours = get_hours()
    update_checkin(habit_id, hours)
    while True:
        logo()
        print(("\nDo you want to test check in any other habit?"))
        options = ["Yes", "No"]
        terminal_menu = TerminalMenu(options)
        menu_index = terminal_menu.show()
        if (menu_index == 0):
            start()
            break
        else:
            logo()
            print(green("\nYou can now test the check-in in the Habit Tracker app"))
            print("\nHappy Coding!\n")
            break
    
    return 1
      
def main():
    start()

if __name__ == '__main__':
    main()
