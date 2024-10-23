import json

class JsonHandler:
    
    def __init__(self, name="None", email="example@gmail.com", password="00000000"): 
        self.name = name
        self.email = email
        self.password = password
        self.progress = 0
        self.flag = 0
        self.solution_1 = False
        self.solution_2 = False
        self.solution_3 = False
        self.solution_4 = False
        self.solution_5 = False
    
    # Method to store data as dictionary.    
    def to_dict(self):
        return {"name": self.name, "email": self.email, "password": self.password, "progress": self.progress, "flag":self.flag,
                "solution_1":self.solution_1, "solution_2":self.solution_2, "solution_3":self.solution_3, "solution_4":self.solution_4,
                "solution_5":self.solution_5}
    
    # Method to write data as json string.
    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)
    
    # Method to save data in json file.
    def save_to_json(self, fileName="data.json"):
        # Reading the content of json file.
        try:
            with open(fileName, "r") as file:
                content = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            content = []

        # Checking if the name or email are existed or not.
        for user in content:
            if self.name == user.get("name") or self.email == user.get("email"):
                return False
             
        # Appending the new data to content. 
        content.append(self.to_dict())

        # Writing the new content in the json file.
        with open(fileName, "w") as file:
            json.dump(content, file, indent=4)

        return True

# Function to check user name and password
def check_user(fileName, userName, password):
    with open(fileName, "r") as file:
        content = json.load(file)
        for user in content:
            if user["name"] == userName and user["password"] == password:
                return True
    return False

# Function to get progress property. 
def get_progress(fileName, userName):
    with open(fileName, "r") as file:
        content = json.load(file)
        for user in content:
            if user["name"] == userName:
                return user["progress"]
        return 0
    
# Function to get user properties. 
def get_userData(fileName, userName):
    with open(fileName, "r") as file:
        content = json.load(file)
        for user in content:
            if user["name"] == userName:
                return user  
    return False  

# Function to update progress of a user.
def update_progress(fileName, userName):
    with open(fileName, "r") as file:
        content = json.load(file)

    for user in content:
        if user["name"] == userName:
            user["progress"] = user.get("progress", 0) + 1  
            break

    with open(fileName, "w") as file:
        json.dump(content, file, indent=4)
    
    
# Function to update logging flag.    
def update_flag(fileName, userName):
    with open(fileName, "r") as file:
        content = json.load(file)

    for user in content:
        if user["name"] == userName:
            user["flag"] = user.get("flag", 0) + 1 
            break

    with open(fileName, "w") as file:
        json.dump(content, file, indent=4)
    
# Function to delete user.    
def del_user(fileName, name):
    flag = False
    with open(fileName, "r") as file:
        content = json.load(file)
        for user in content:
            if user["name"] == name:
                content.remove(user)
                flag = True
    if flag:
        with open(fileName, "w") as file:
            json.dump(content, file, indent=4)
            return True
    else:
        return False

    return True

# Function to update the problem flag.
def update_problem(fileName, name, solution):
    with open(fileName, "r") as file:
        content = json.load(file)

    for user in content:
        if user["name"] == name:
            user[solution] = True  
            break

    with open(fileName, "w") as file:
        json.dump(content, file, indent=4)

    return True
