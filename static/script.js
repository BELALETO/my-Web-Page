
if(window.location.pathname === "/")
{
    function goToLogin() {
        window.location.href = 'login';
    }
    
    function goToRegister() {
        window.location.href = 'register';
    }
    
    document.getElementById('Login').addEventListener('click', goToLogin);
    document.getElementById('Register').addEventListener('click', goToRegister);
}


else if(window.location.pathname === "/main")
{
    btn_1 = document.getElementById("btn_1")
    btn_2 = document.getElementById("btn_2")
    btn_3 = document.getElementById("btn_3")
    btn_4 = document.getElementById("btn_4")
    btn_5 = document.getElementById("btn_5")
    logout_btn = document.getElementById("logout_Btn")
    surrender_btn = document.getElementById("surrender_Btn")

    btn_1.addEventListener("click", ()=>{window.location.href="/quiz"})
    btn_2.addEventListener("click",()=>{window.location.href="/quiz"})
    btn_3.addEventListener("click",()=>{window.location.href="/quiz"})
    btn_4.addEventListener("click",()=>{window.location.href="/quiz"})
    btn_5.addEventListener("click",()=>{window.location.href="/quiz"})
    logout_btn.addEventListener("click",()=>{window.location.href="/logout"})
    surrender_btn.addEventListener("click",()=>{window.location.href="/surrender"})
}

else if(window.location.pathname === "/quiz")
{
    logoutQuiz = document.getElementById("logout_Quiz")
    logoutQuiz.addEventListener("click",()=>{window.location.href="/logout"})
}
