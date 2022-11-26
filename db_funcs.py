from db_context_managers import DB_context_manager

# Create table 
def open_db(DB_NAME):

    with DB_context_manager(DB_NAME) as c:
        c.execute("""

            CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                FIRSTNAME TEXT,
                LASTNAME TEXT,
                USERNAME TEXT,
                PASSWORD TEXT           
            );
            
        """)

        c.execute("""

            CREATE TABLE IF NOT EXISTS public_keys (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                KEY_VALUE TEXT,
                user_id INTEGER,
                FOREIGN KEY (user_id) REFERENCES user (id) 
            );
            
        """)


    return 0


# Insert user into DB
def insert_into_db(DB_NAME, user):
    
    with DB_context_manager(DB_NAME) as c:
        c.execute("INSERT INTO user (id, FIRSTNAME, LASTNAME, USERNAME, PASSWORD) VALUES (:id, :firstname, :lastname, :username, :password)", {'id': None, 'firstname': user.firstname, 'lastname': user.lastname, 'username': user.username, 'password': user.password})
        
    return 0


# Select a user from DB
def select_from_db(DB_NAME, username):
    
    with DB_context_manager(DB_NAME) as c:
        c.execute("SELECT * FROM user WHERE USERNAME=:username", {'username': username})
        user = c.fetchone()

    return user