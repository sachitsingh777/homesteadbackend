# models/user.py
class User:
    def __init__(self, username, email, password,role):
        self.username = username
        self.email = email
        self.password = password
    
    def is_valid(self):
        return bool(self.username and self.email and self.password)




