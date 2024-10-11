import json

class jsonHandler:
    name =""
    email = ""
    password = ""
    
    def __init__(self, name = "None", email = "example@gmail.com", password = "00000000"):
        self.name = name
        self.email= email
        self.password = password
    
    def write():
        with open("static/users.json", "a") as file:
            # print("Hello")
            file.close()
         