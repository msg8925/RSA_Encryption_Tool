import sqlite3

# To create an in memory DB
#conn = sqlite3.connect(':memory:')

def create_db_connection(DB_NAME):

    # Connect to a db specified by argument 'DB_NAME'  
    conn = sqlite3.connect(DB_NAME)

    # Return the DB connection
    return conn


def get_db_cursor(DB_CONN):

    # Retrieve the DB cursor from the DB connection 
    c = DB_CONN.cursor()
        
    # Return the cursor
    return c 


def create_user_table(DB_NAME):

    conn = create_db_connection(DB_NAME) 
    c = get_db_cursor(conn)

    c.execute("""

        CREATE TABLE users (
            firstname text,
            lastname text,
            email text
        )

    """)

    return 0 


def insert_user_into_db(user, DB_NAME):

    conn = create_db_connection(DB_NAME) 
    c = get_db_cursor(conn)

    c.execute("INSERT INTO users VALUES (:username, :password, :email)", {'username':user.username, 'password':user.password, 'email':user.email})

    conn.commit()

    conn.close()

    return 0


def select_user_from_db(username, DB_NAME):

    conn = create_db_connection(DB_NAME) 
    c = get_db_cursor(conn)

    c.execute("SELECT * FROM users WHERE username=:username", {'username': username})

    users = c.fetchall()

    conn.close()

    return users 

# c.execute("""

#     CREATE TABLE employees (
#         firstname text,
#         lastname text,
#         salary integer
#     )

# """)