from flask import Flask, render_template, request, redirect, url_for, session, flash
import jsonHandler
import localCompiler
import os  # Import the os module to handle file removal

app = Flask(__name__)
app.secret_key = "your_secret_key"

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
        page_id = request.form.get("page_id")

        # Registration process
        if page_id == "reg_id":
            name = request.form.get('newUserName')
            email = request.form.get('newEmail')
            password = request.form.get('newPassword')

            obj = jsonHandler.JsonHandler(name, email, password)
            flag = obj.save_to_json("static/users.json")

            if flag:
                session['username'] = name
                flash("Welcome Challenger!")
                return redirect(url_for("Main"))
            else:
                flash("Invalid user name or email!", "error")
                return redirect(url_for("Register"))

        # Login process
        else:
            name = request.form.get("userName")
            password = request.form.get("password")
            flag = jsonHandler.check_user("static/users.json", name, password)

            if flag:
                session['username'] = name
                flash("You've been logged in successfully!", "info")
                return redirect(url_for("Main"))
            else:
                flash("Wrong name or password!")
                return redirect(url_for("Login"))

    if 'username' in session:
        session_name = session['username']
        progress = jsonHandler.get_progress("static/users.json", session_name)
        return render_template("main.html", DATA="logged", INFO=str(progress), NAME=session_name)
    else:
        return redirect(url_for('Home'))

# Quiz page
@app.route("/quiz", methods=["GET", "POST"])
def Quiz():
    if request.method == "GET" and "username" in session:
        session_name = session["username"]
        content = request.args.get("problem_description")
        return render_template("quiz.html", QUIZ=content, NAME=session_name)
    else:
        flash("Please log in or register to access the Quiz form.")
        return redirect(url_for("Home"))


@app.route("/result", methods=["POST"])
def Result():
    code = request.form.get("code")
    key = request.form.get("quiz_id")

    cpp_file = "static/example.cpp"
    cpp_out = "example"  # User's compiled executable
    input_file = None

    # Map quiz keys to the correct solution files
    solutions = {
        "problem_1": ("static/exams/solution_1/solution_1.cpp", "solution_1"),
        "problem_2": ("static/exams/solution_2/solution2.cpp", "solution_2", "static/exams/solution_2/test.txt"),
        "problem_3": ("static/exams/solution_3/solution3.cpp", "solution_3", "static/exams/solution_3/test.txt"),
        "problem_4": ("static/exams/solution_4/solution4.cpp", "solution_4", "static/exams/solution_4/test.txt"),
        "problem_5": ("static/exams/solution_5/solution5.cpp", "solution_5", "static/exams/solution_5/test.txt"),
    }

    if key in solutions:
        solution = solutions[key]
        main_file = solution[0]
        main_out = solution[1]  # Correct solution's compiled executable
        if len(solution) > 2:
            input_file = solution[2]

        # Check if the code is for "problem_1" and requires input via cin
        if key == "problem_1":
            # Provide a default input file for "Hello World" case
            input_file = "static/exams/solution_1/input.txt"
            with open(input_file, "w") as input_f:
                input_f.write("Sample Input\n")  # Replace with actual expected input

        # Write the user-submitted code to a file
        with open(cpp_file, "w") as file:
            file.write(code)

        # Compile and run the submitted code and correct solution
        user_output = localCompiler.compile_and_run(cpp_file, cpp_out, input_file)
        expected_output = localCompiler.compile_and_run(main_file, main_out, input_file)

        # Compare outputs
        is_correct = localCompiler.compare_outputs(cpp_file, main_file, cpp_out, main_out, input_file)

        if is_correct:
            jsonHandler.update_progress("static/users.json", request.form.get("userName"))
            result_message = "Your Solution is correct!"
        else:
            result_message = "Wrong Solution, try again!"

        # Cleanup: Remove compiled executables (user's and correct solution's)
        try:
            if os.path.exists(cpp_out):  # Check if user's executable exists
                os.remove(cpp_out)
            if os.path.exists(main_out):  # Check if solution's executable exists
                os.remove(main_out)
        except Exception as e:
            print(f"Error while cleaning up executable files: {e}")

        # Pass user output and expected output to the result page
        return render_template("result.html", DATA=result_message, FLAG=key, UOUTPUT=user_output, EOUTPUT=expected_output)

    else:
        flash("Invalid quiz ID!")
        return redirect(url_for("Main"))
        

@app.route("/logout")
def Logout():
    session.pop("username", None)
    return redirect(url_for("Home"))

@app.route("/surrender")
def Surrender():
    if "username" in session:
        name = session["username"]
        jsonHandler.del_user("static/users.json", name)
    return redirect(url_for("Logout"))

if __name__ == "__main__":
    app.run(debug=True)
