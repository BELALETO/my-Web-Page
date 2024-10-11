from flask import Flask ,render_template


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
    # open json file
    # check if the user is allready existed or not.
    # append into json file.
    # close the json file.
    # display the main page.
    # else redirect into an error page
    return render_template("main.html")

if __name__ == "__main__":
    app.run(debug=True)