import json

class JsonHandler:
    name = ""
    email = ""
    password = ""
    progress = 0
    def __init__(self, name="None", email="example@gmail.com", password="00000000"): 
        self.name = name
        self.email = email
        self.password = password
        self.progress = 0
        
    def to_dict(self):
        return {"name": self.name, "email": self.email, "password": self.password, "progress": self.progress}
    
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
                return False 

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

def get_progress(fileName, userName):
    with open(fileName, "r") as file:
        content = json.load(file)
        for user in content:
            if user["name"] == userName:
                return user["progress"]
        return 0




def update_progress(fileName, userName):
    try:
        with open(fileName, "r") as file:
            content = json.load(file)
    except FileNotFoundError:
        print(f"Error: The file {fileName} does not exist.")
        return False
    except json.JSONDecodeError:
        print(f"Error: The file {fileName} contains invalid JSON.")
        return False

    user_found = False

    for user in content:
        if user.get("name") == userName:
            if "progress" in user and isinstance(user["progress"], int):
                user["progress"] += 1
            else:
                user["progress"] = 1
            user_found = True
            break 

    if not user_found:
        print(f"Error: User '{userName}' not found.")
        return False

    try:
        with open(fileName, "w") as file:
            json.dump(content, file, indent=4)
    except IOError as e:
        print(f"Error writing to file {fileName}: {e}")
        return False

    return True

             