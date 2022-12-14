from auth import login, register
import os 

DB_NAME=os.getenv("DB_NAME") 

def login_required(original_function):
    
    # This code is run before original functions
    def wrapper_function(*args, **kwargs):
       
        result = login()
        
        # No account found
        if result == 1:
            print("Account does not exist. Create one now: ")
            if register() == 0:
                return original_function(*args, **kwargs)
            else:
                return 3    

        # Incorrect credentials
        elif result == 2:
            return 2
        
        # If login successful
        elif result == 0:
            return original_function(*args, **kwargs)

        # Any other result
        else:
            print(f"Result: {result}")
            return 4

    return wrapper_function



