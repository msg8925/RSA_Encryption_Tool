class User:

    def __init__(self, firstname, lastname, username, password, email):
        self.firstname = firstname
        self.lastname = lastname 
        self.username = username
        self.password = password
        self.email = email 


    def __repr__(self):
        return f"User({self.username}, {self.password}, {self.email})"    


class Public_key:

    def __init__(self, key_value, user_id):
        self.key_value = key_value
        self.user_id = user_id


    def __repr__(self):
        return f"Public_key({self.key_value}, {self.user_id})" 

    def __str__(self):
        return f"Public_key({self.key_value}, {self.user_id})"   