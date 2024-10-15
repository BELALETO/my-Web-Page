from flask import Flask, render_template, request, redirect, url_for, session, flash
import jsonHandler
import judge


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
        id = request.form.get("page_id")  # Determine if request is from register or login

        if id == "reg_id":  
            # Registration Process
            name = request.form.get('newUserName')  
            email = request.form.get('newEmail')    
            password = request.form.get('newPassword') 

            obj = jsonHandler.JsonHandler(name, email, password) 
            flag = obj.save_to_json("static/users.json") 

            if flag:  # Registration successful
                session['username'] = name  # Set session variable
                flash("Welcome Challenger!") 
                
                progress = jsonHandler.get_progress("static/users.json", name) 
                return redirect(url_for("Main"))  # Redirect to dashboard
            else:
                flash("Invalid user name or email!", "error") 
                return redirect(url_for("Register")) 

        else:
            # Login Process
            name = request.form.get("userName")
            password = request.form.get("password")
            flag = jsonHandler.check_user("static/users.json", name, password)

            if flag:
                session['username'] = name  # Set session variable
                flash("You've been logged in successfully!", "info")
                return redirect(url_for("Main"))  # Redirect to dashboard
            else:
                flash("Wrong name or password!")
                return redirect(url_for("Login"))
    
    # Handle GET request: Display Dashboard if logged in
    if 'username' in session:
        session_name = session['username']
        progress = jsonHandler.get_progress("static/users.json", session_name)
        return render_template("main.html", DATA="logged", INFO=str(progress), NAME = session_name)
    else:
        flash("Please log in or register to access the dashboard.")
        return redirect(url_for('Home'))

@app.route("/quiz", methods = ["GET", "POST"])
def Quiz():
    if request.method == "GET" and "username" in session:
        session_name = session["username"]
        content = request.args.get("problem_description")
        print(content)
        return render_template("quiz.html", QUIZ = content, NAME = session_name)
    else :
        # flash("Please log in or register to access the Quiz form.")
        return redirect(url_for("Home"))
        
    
    
    

@app.route("/result", methods = ["GET", "POST"])
def Result():
    code = request.form.get("code")
    key = request.form.get("quiz_id") # temp
    print(code)
    cpp_file = "static/example.cpp"
    cpp_out = "example"
    input_file = ""
    
    # write a logic to map each file to its model solution.
    main_file = ""
    main_out = ""
    print("Your key is: " + str(key))
    
    if key == "problem_1":
        main_file = "static/exams/solution_1/solution_1.cpp"
        main_out = "solution_1"
        # No test.txt file.

    elif key == "problem_2":
        main_file = "static\exams\solution_2\solution2.cpp"
        main_out = "solution_2"
        input_file = "static/exams/solution_2/test.txt"
        
    elif key == "problem_3":
        main_file = "static\exams\solution_3\solution3.cpp"
        main_out = "solution_3"
        input_file = "static/exams/solution_3/test.txt"

        
        
    elif key == "problem_4":
        main_file = "static\exams\solution_4\solution4.cpp"
        main_out = "solution_4"
        input_file = "static/exams/solution_4/test.txt"

    elif key == "problem_5":
        main_file = "static\exams\solution_5\solution5.cpp"
        main_out = "solution_5"
        input_file = "static/exams/solution_5/test.txt"

     
    with open(cpp_file, "w") as file:
        file.write(code)
    refree = judge.court(cpp_file, main_file, cpp_out, main_out, input_file)
    if refree.sentence():
        
        fileName = "static/users.json"
        userName = request.form.get("userName")
        print(userName)
        #increment progress here.
        jsonHandler.update_progress(fileName, userName)
        return render_template("result.html", DATA = "Your Solution is correct!", FLAG = key)
    else:
        return render_template("result.html", DATA = "Wrong Solution try again!", FLAG = key)
    

@app.route("/logout")
def Logout():
    session.pop("username", None)
    return redirect(url_for("Home"))


@app.route("/surrender")
def Surrender():
    print("I'm in surrender route")
    #deleting user from json file logic.
    fileName = "static/users.json"
    name = session["username"]
    print(name)
    flag = jsonHandler.del_user(fileName, name)
    print(flag)
    return redirect(url_for("Logout"))


if __name__ == "__main__":
    app.run(debug=True)


 
