from flask import Flask, render_template, request, redirect, url_for, session, flash
import jsonHandler
import localCompiler


app = Flask(__name__)
app.secret_key = "codeTalkers"




# The home page
@app.route("/")
def Home():
    return render_template("index.html")

# Login page
@app.route("/login")
def Login():
    return render_template("login.html")


# Register page
@app.route("/register")
def Register():
    return render_template("register.html")


# Dashboard page
@app.route("/main", methods=["GET", "POST"])  
def Main():
    if request.method == "POST":  
        id = request.form.get("page_id") # checking page id to know if the request from existing user or new one. 
        if id == "reg_id":  
            name = request.form.get('newUserName')  #getting user name
            email = request.form.get('newEmail')    #getting user email
            password = request.form.get('newPassword') #getting user password
            obj = jsonHandler.JsonHandler(name, email, password) # creating a jsonHandler object.
            flag = obj.save_to_json("static/users.json") # save user info
            if flag: #checking if the user is allready existed or not.
                flash("Welcome Challenger!") # flashing a new message to the new challenger
                progress = jsonHandler.get_progress("static/users.json", name) # fetching the progress property.
                return render_template("main.html", DATA="logged", INFO = str(progress)) # showing the page with data
            else:
                flash("Invalid user name or email!", "error") # flashing error message.
                return redirect(url_for("Register")) # return to the Register page.
        else:
            name = request.form.get("userName")
            password = request.form.get("password")
            flag = jsonHandler.check_user("static/users.json", name, password)
            if flag:
                flash("You've been logged in successfully!", "info")
                progress = jsonHandler.get_progress("static/users.json", name)
                return render_template("main.html", DATA="logged", INFO = str(progress))
            else:
                flash("Wrong name or password!")
                return redirect(url_for("Login"))
    
    return redirect(url_for('Home'))


@app.route("/quiz", methods = ["GET", "POST"])
def Quiz():
    if request.method == "GET":
        content = request.args.get("problem_description")
        print(content)
        return render_template("quiz.html", QUIZ = content)

@app.route("/result", methods = ["GET", "POST"])
def Result():
    code = request.form.get("code")
    print(code)
    cpp_file = "static/example.cpp"
    cpp_out = "example"
    with open(cpp_file, "w") as file:
        file.write(code)
    obj = localCompiler.compiler(cpp_file, cpp_out)
    print(obj.build_Run())
    return render_template("result.html", DATA = code)


if __name__ == "__main__":
    app.run(debug=True)
