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
        name = session['username']
        progress = jsonHandler.get_progress("static/users.json", name)
        return render_template("main.html", DATA="logged", INFO=str(progress))
    else:
        flash("Please log in or register to access the dashboard.")
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
    key = request.form.get("quiz_id") # temp
    print(code)
    cpp_file = "static/example.cpp"
    cpp_out = "example"
    
    # write a logic to map each file to its model solution.
    main_file = ""
    main_out = ""
    print("Your key is: " + str(key))
    
    if key == "problem_1":
        main_file = "static/exams/solution_1.cpp"
        main_out = "solution_1"

    elif key == "problem_2":
        main_file = "static/exams/solution_1.cpp"
        main_out = "solution_1"
        
    elif key == "problem_3":
        main_file = "static/exams/solution_3.cpp"
        main_out = "solution_3"
        
    elif key == "problem_4":
        main_file = "static/exams/solution_4.cpp"
        main_out = "solution_4"
        
    elif key == "problem_5":
        main_file = "static/exams/solution_5.cpp"
        main_out = "solution_5"
    
     
    with open(cpp_file, "w") as file:
        file.write(code)
    refree = judge.court(cpp_file, main_file, cpp_out, main_out)
    if refree.sentence():
        
        #increment progress here.
        return render_template("result.html", DATA = "Your Solution is correct!", FLAG = key)
    else:
        return render_template("result.html", DATA = "Wrong Solution try again!", FLAG = key)
    

if __name__ == "__main__":
    app.run(debug=True)


 
