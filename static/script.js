
function changeHead()
{
    let head = document.getElementById("challenger_name_main");
    let name = document.getElementById("userName");
    name.innerText = localStorage.getItem("NAME");
    head.innerText = "Welcome back: " + name.innerText + " !";
}

function initialHead()
{
    let head = document.getElementById("challenger_name_main");
    let name = document.getElementById("userName");
    name.innerText = localStorage.getItem("NAME");
    head.innerText = "Welcome to codeTalkers " + name.innerText + " !";
}

if(window.location.pathname === "/")
{    
    const login = document.getElementById('Login');
    login.addEventListener('click', ()=>{window.location.href = 'login';});
    
    const register = document.getElementById('Register');
    register.addEventListener('click', ()=>{window.location.href = 'register';});
}

else if(window.location.pathname === "/login")
{
    let nameBox = document.getElementById("userName");
    let loginButton = document.getElementById("loginButton");
    let ret = document.getElementById("return");
    loginButton.addEventListener("click", ()=>{
        localStorage.setItem("NAME", nameBox.value);
    });
    ret.addEventListener("click", ()=>{window.history.back();});

}

else if(window.location.pathname === "/register")
{
        const usernameInput = document.getElementById('userName');
        const emailInput = document.getElementById('email');
        const passwordInput = document.getElementById('Password');
        const registerButton = document.getElementById('registerButton');
    
        // Regular expressions for validation
        const usernameRegex = /^[A-Za-z][A-Za-z0-9_]{2,19}$/;
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        const passwordRegex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/; // At least 8 characters, including letters and numbers
        
        // Function to validate the username
        function validateUsername() {
            if (!usernameRegex.test(usernameInput.value)) {
                usernameInput.style.borderColor = "red";
                return false;
            } else {
                usernameInput.style.borderColor = "green";
                return true;
            }
        }
    
        // Function to validate the email
        function validateEmail() {
            if (!emailRegex.test(emailInput.value)) {
                emailInput.style.borderColor = "red";
                return false;
            } else {
                emailInput.style.borderColor = "green";
                return true;
            }
        }
    
        // Function to validate the password
        function validatePassword() {
            if (!passwordRegex.test(passwordInput.value)) {
                passwordInput.style.borderColor = "red";
                return false;
            } else {
                passwordInput.style.borderColor = "green";
                return true;
            }
        }
    
        // Validate on form submission
        registerButton.addEventListener('click', function (event) {
            if (!validateUsername() || !validateEmail() || !validatePassword()) {
                event.preventDefault(); // Prevent form submission if validation fails
            }
            else
            {
                localStorage.setItem("NAME",usernameInput.value);
            }
        });
    
        usernameInput.addEventListener('blur', validateUsername);
        emailInput.addEventListener('blur', validateEmail);
        passwordInput.addEventListener('blur', validatePassword);
    
        const ret = document.getElementById('return'); 
        ret.addEventListener('click',()=>{window.history.back();});
}

else if(window.location.pathname === "/main")
{
    let head = document.getElementById("challenger_name_main");
    let name = document.getElementById("userName");

    let container = document.getElementById("container_main");
    const problem_head = document.getElementById("problem_head");
    let form = document.getElementById("form_container");
    const btn_1 = document.getElementById("btn_1");
    const btn_2 = document.getElementById("btn_2");
    const btn_3 = document.getElementById("btn_3");
    const btn_4 = document.getElementById("btn_4");
    const btn_5 = document.getElementById("btn_5");
    const logout_btn = document.getElementById("logout");
    const surrender_btn = document.getElementById("surrender");
    const leaderboard_btn = document.getElementById("leaderboard");

    btn_1.addEventListener("click", ()=>{window.location.href="/quiz"});
    btn_2.addEventListener("click",()=>{window.location.href="/quiz"});
    btn_3.addEventListener("click",()=>{window.location.href="/quiz"});
    btn_4.addEventListener("click",()=>{window.location.href="/quiz"});
    btn_5.addEventListener("click",()=>{window.location.href="/quiz"});
    logout_btn.addEventListener("click",()=>{window.location.href="/logout"});
    surrender_btn.addEventListener("click",()=>{window.location.href="/surrender"});
    leaderboard_btn.addEventListener("click", ()=>{window.location.href="/leaderboard"});
    
    fetch("/get_data")
    .then(response => {return response.json();})
    .then(data =>{const flag = data.flag;
        if(flag)
        {
            changeHead();
        }
        else
        {
            initialHead();
        }
        })

    fetch("/get_data")
    .then(response => {return response.json();})
    .then(data =>{const s1 = data.solution_1;
        const s2 = data.solution_2;
        const s3 = data.solution_3;
        const s4 = data.solution_4;
        const s5 = data.solution_5;
        const champ = s1 && s2 && s3 && s4 && s5;
        if(s1)
        {
            btn_1.disabled = true;
        }
        if(s2)
        {
            btn_2.disabled = true;
        }
        if(s3)
        {
            btn_3.disabled = true;
        }
        if(s4)
        {
            btn_4.disabled = true;
        }
        if(s5)
        {
            btn_5.disabled = true;
        }
        if(champ)
        {
            container.removeChild(problem_head);
            form.removeChild(btn_1);
            form.removeChild(btn_2);
            form.removeChild(btn_3);
            form.removeChild(btn_4);
            form.removeChild(btn_5);
            let p1 = document.createElement("p");
            let p2 = document.createElement("p");
            p1.innerText = "Congratulations champ!"
            p2.innerText = "You're Officially a codeTalker.";
            form.appendChild(p1);
            form.appendChild(p2);
        }
    })
    
}

else if(window.location.pathname === "/quiz")
{
    const retButton = document.getElementById("return");


    retButton.addEventListener("click", ()=>{window.location.href="/main"});
}

else if(window.location.pathname === "/leaderboard")
{
    fetch("/sort_users", {method : "GET", headers:{"Content-Type":"application/json"}})
    .then(response =>{return response.json()})
    .then((data)=>{
        print_progress(data);
    })

    let retTable = document.getElementById("retTable");
    retTable.addEventListener("click", ()=>{window.history.back();});
}

function print_progress(data)
{
    let table = document.getElementById("table");
    for(let i = 0; i < data.length; i++)
    {
        let row = document.createElement("tr");
        let nodeName = document.createElement("td");
        let nodeProgress = document.createElement("td");
        nodeName.innerText = data[i]["name"];
        nodeProgress.innerText = data[i]["progress"];
        row.appendChild(nodeName);
        row.appendChild(nodeProgress);
        table.appendChild(row);
    }
}






