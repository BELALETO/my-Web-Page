import json

class JsonHandler:
    name = ""
    email = ""
    password = ""
    
    def __init__(self, name = "None", email = "example@gmail.com", password = "00000000"): 
        self.name = name
        self.email = email
        self.password = password
        
    def to_dict(self):
        data = {"name": self.name, "email":self.email, "password": self.password}
        return data
    
    def to_json(self):
        data = self.to_dict()
        str_data = json.dumps(data, indent=4)
        return str_data
    
    def save_to_json(self, fileName = "data.json"):
        
        try:
            with open(fileName, "r") as file:
    
                content = json.load(file)
        except(FileNotFoundError, json.JSONDecodeError):
            content = []
            
        for name_chk in content:
                if self.name == name_chk:
                    file.close()
                    return False
                
        file.close()
        content.append(self.to_dict)
        
        with open(fileName, "w") as file:
            json.dump(content, file, indent=4)
            file.close()
            
        return True
    

def check_user(fileName, userName, password):
    flag = False
        
    with open(fileName, "r") as file:
        content = json.load(file)
        for user in content:
            if user["name"] == userName and user["password"] == password:
                flag = True
        file.close()
    return flag        