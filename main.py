from flask import Flask ,render_template, request, url_for, redirect
import jsonHandler

app = Flask(__name__)



@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/login")
def Login():
    return render_template("login.html")


@app.route("/register")
def Register():
    return render_template("register.html")


@app.route("/main")
def Main():
    id = request.args.get("page_id")
    
    if id == "reg_id":
        name = request.args.get('newUserName')
        email = request.args.get('newEmail')
        password = request.args.get('newPassword')
        print(name)
        print(email)
        print(password)
        obj = jsonHandler.JsonHandler(name, email, password)
        print(obj.to_json())
        flag = obj.save_to_json("static/users.json")
        if flag:
            return render_template("main.html", DATA = obj.to_json())
        else:
            return render_template("index.html")
    else:
        name = request.args.get("userName")
        password = request.args.get("password")
        flag = jsonHandler.check_user("static/users.json", name, password)
        print("Hello")
        if flag:
            return render_template("main.html", DATA = "Hello" + name)
        else:
            return render_template("index.html")
    

if __name__ == "__main__":
    app.run(debug=True)