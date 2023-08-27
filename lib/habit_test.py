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
        else:
            return user_id
        
def start():
    logo()
    users = get_all_users()
    user_ids = []
    for user in users:
        user_ids.append(str(user.id))

    print(get_user_id(user_ids))
    

    

    
def main():
    start()

if __name__ == '__main__':
    main()
