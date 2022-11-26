class User:

    def __init__(self, firstname, lastname, username, password, email):
        self.firstname = firstname
        self.lastname = lastname 
        self.username = username
        self.password = password
        self.email = email 


    def __repr__(self):
        return f"User({self.username}, {self.password}, {self.email})"    


