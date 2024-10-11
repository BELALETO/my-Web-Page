import json

class JsonHandler:
    name = ""
    email = ""
    password = ""
    
    def __init__(self, name="None", email="example@gmail.com", password="00000000"): 
        self.name = name
        self.email = email
        self.password = password
        
    def to_dict(self):
        return {"name": self.name, "email": self.email, "password": self.password}
    
    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)
    
    def save_to_json(self, fileName="data.json"):
        try:
            with open(fileName, "r") as file:
                content = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            content = []

        for user in content:
            if self.name == user.get("name") or self.email == user.get("email"):
                return False  # Name already exists

        content.append(self.to_dict())

        with open(fileName, "w") as file:
            json.dump(content, file, indent=4)

        return True

def check_user(fileName, userName, password):
    with open(fileName, "r") as file:
        content = json.load(file)
        for user in content:
            if user["name"] == userName and user["password"] == password:
                return True
    return False
