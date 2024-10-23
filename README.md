# Coding Competition Platform

## Description
A web-based coding competition platform designed for users to test their C++ coding skills through a series of exams. The platform includes features such as user profiles, a leaderboard, and progress tracking.

## Features
- **User Authentication**: Users can register and log in to their accounts.
- **Exams**: Users can take multiple coding exams and receive scores.
- **Leaderboard**: A ranking system that displays the top performers based on their scores.
- **User Profiles**: Each user has a profile that shows their exam history and statistics.

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **Database**: [json file]
- **Version Control**: Git

## Installation
1. Clone the repository:
   ```bash
   git clonehttps://github.com/BELALETO/my-Web-Page.git
   cd coding-competition-platform

## Install dependencies:
1. pip install flask
2. install minGW or any g++ compiler.

## configuration:
1. flask --app main.py --debug run
2. or just: python3 main.py

## Usage:
1. Sign up for an account or log in if you already have one.
2. Select an exam button from the dashboard.
3. solve the problem in C++ language.
4. Click submit button, to submit your code.
5. If your answer is correct, your progress will increment.
6. From Dashboard, you can press leaderboard button to see all users and there progress.
7. If you press Surrender button your account will be deleted from the database.
8. If you press log out button you'll be signed out.


## Project Checklist
- [x] It is available on GitHub.
- [x] It uses the Flask web framework.
- [x] It uses at least one module from the Python Standard Library other than the random module. Please provide the name of the module you are using in your app. 
- Module name: json
- Module name: subprocess
- [x] It contains at least one class written by you that has both properties and methods. It uses `__init__()` to let the class initialize the object's attributes (note that  `__init__()` doesn't count as a method). This includes instantiating the class and using the methods in your app. 
Please provide below the file name and the line number(s) of at least one example of a class definition in your code as well as the names of two properties and two methods. 
- File name for the class definition: jsonHandler 
- Line number(s) for the class definition: 18 
- Name of two properties: name, email.
- Name of two methods:  get_progress, check_user
- File name and line numbers where the methods are used: jsonHandler.py, get_progress: 60, check_user:51
- [x] It makes use of JavaScript in the front end and uses the localStorage of the web browser.
- [x] It uses modern JavaScript (for example, let and const rather than var).
- [x] It makes use of the reading and writing to the same file feature.
- [x] It contains conditional statements. Please provide below the file name and the line number(s) of at least one example of a conditional statement in your code. 
- File name: static/script.js
- Line number(s): line 53.
- [x] It contains loops. Please provide below the file name and the line number(s) of at least one example of a loop in your code. 
- File name: script.js
- Line number(s): line 216. 
- [x] It lets the user enter a value in a text box at some point. 
This value is received and processed by your back end Python code.
- [x] It doesn't generate any error message even if the user enters a wrong input. 
- [x] It is styled using your own CSS. 
- [x] The code follows the code and style conventions as introduced in the course, is fully documented using comments and doesn't contain unused or experimental code.  
In particular, the code should not use `print()` or `console.log()` for any information the app user should see. 
Instead, all user feedback needs to be visible in the browser.   
- [x] All exercises have been completed as per the requirements and pushed to the respective GitHub repository.