class User:

    def __init__(self, firstname, lastname, email):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email 


    def __repr__(self):
        return f"User({self.firstname}, {self.lastname}, {self.email})"    


