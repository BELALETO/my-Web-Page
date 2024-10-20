
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
    head.innerText = "Welcome " + name.innerText + " !";
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

    loginButton.addEventListener("click", ()=>{
        localStorage.setItem("NAME", nameBox.value);
    })
}

else if(window.location.pathname === "/register")
{

    let userName = document.getElementById("userName");
    let registerButton = document.getElementById("registerButton");

    registerButton.addEventListener("click", ()=>{
        localStorage.setItem("NAME", userName.value);
    })
}

else if(window.location.pathname === "/main")
{
    const btn_1 = document.getElementById("btn_1")
    const btn_2 = document.getElementById("btn_2")
    const btn_3 = document.getElementById("btn_3")
    const btn_4 = document.getElementById("btn_4")
    const btn_5 = document.getElementById("btn_5")
    const logout_btn = document.getElementById("logout")
    const surrender_btn = document.getElementById("surrender")
    const leaderboard_btn = document.getElementById("leaderboard")

    btn_1.addEventListener("click", ()=>{window.location.href="/quiz"})
    btn_2.addEventListener("click",()=>{window.location.href="/quiz"})
    btn_3.addEventListener("click",()=>{window.location.href="/quiz"})
    btn_4.addEventListener("click",()=>{window.location.href="/quiz"})
    btn_5.addEventListener("click",()=>{window.location.href="/quiz"})
    logout_btn.addEventListener("click",()=>{window.location.href="/logout"})
    surrender_btn.addEventListener("click",()=>{window.location.href="/surrender"})
    leaderboard_btn.addEventListener("click", ()=>{window.location.href="/leaderboard"})
    
    fetch("/get_data")
    .then(response => {return response.json();})
    .then(data =>{const flag = data.flag;
        if(flag)
        {
            console.log("I'm safe");
            console.log(flag);
            changeHead();
        }
        else
        {
            console.log("I'm not safe");
            console.log(flag)
            initialHead();
        }
        })
        .catch(error=>{console.log("error")})

    fetch("/get_data")
    .then(response => {return response.json();})
    .then(data =>{const s1 = data.solution_1;
        const s2 = data.solution_2;
        const s3 = data.solution_3;
        const s4 = data.solution_4;
        const s5 = data.solution_5;

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
    })
        
        .catch(error=>{console.log("error")})

    
}

else if(window.location.pathname === "/quiz")
{
    const logoutQuiz = document.getElementById("logout_Quiz")
    logoutQuiz.addEventListener("click",()=>{window.location.href="/logout"})
}

else if(window.location.pathname === "/leaderboard")
{
    fetch("/sort_users", {method : "GET", headers:{"Content-Type":"application/json"}})
    .then(response =>{return response.json()})
    .then((data)=>{
        /* fun */
        print_progress(data);
    })

    let retTable = document.getElementById("retTable");
    retTable.addEventListener("click", ()=>{window.location.href="/main"});
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