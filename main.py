from flask import Flask, render_template, request, redirect, url_for
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

@app.route("/main", methods=["GET", "POST"])  
def Main():
    if request.method == "POST":  
        id = request.form.get("page_id")  
        if id == "reg_id":  
            name = request.form.get('newUserName')
            email = request.form.get('newEmail')
            password = request.form.get('newPassword')
            obj = jsonHandler.JsonHandler(name, email, password)
            flag = obj.save_to_json("static/users.json")
            if flag:
                return render_template("main.html", DATA=obj.to_json())
            else:
                return render_template("index.html")
        else:  # Login
            name = request.form.get("userName")
            password = request.form.get("password")
            flag = jsonHandler.check_user("static/users.json", name, password)
            if flag:
                return render_template("main.html", DATA="Hello " + name)
            else:
                return render_template("index.html")
    
    return redirect(url_for('Home')) 

if __name__ == "__main__":
    app.run(debug=True)
