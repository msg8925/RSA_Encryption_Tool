from db_funcs import open_db, insert_into_db, select_from_db
from user import User
import bcrypt

DB_NAME="user.db"

def login():
    
    username = input("Please enter your username: ")
    password = input("Please enter your password: ") 

    user = select_from_db(DB_NAME, username)
    if user == None:
        #print(user[4])
        print("No account with username provided.")
        return 1
    
    else:
        if bcrypt.checkpw(password.encode(), user[4]):
            print("Successfully logged in.")
            return 0
        
        else:
            print("Incorrect login credentials.")
            return 2


def register():

    firstname = input("Please enter your firstname: ")
    lastname = input("Please enter your lastname: ")
    username = input("Please enter your username: ")
    email = input("Please enter your email address: ") 
    password_1 = input("Please enter your password: ")
    password_2 = input("Please enter your password again: ")

    # Check username does not already exist
    user = select_from_db(DB_NAME, username)
    # If there is no user with that name
    if user:
        print("This username already exists.")
        return 1

    # Check the passwords match
    else: 
        if password_1 != password_2:
            print("Passwords do not match.")
            return 2

        else:
            hashed_password = bcrypt.hashpw(password_1.encode(), bcrypt.gensalt())
            #print(hashed_password)

            user = User(firstname, lastname, username, hashed_password, email)
            insert_into_db(DB_NAME, user)
    
            return 0