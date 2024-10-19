
if(window.location.pathname === "/")
{    
    document.getElementById('Login').addEventListener('click', ()=>{window.location.href = 'login';});
    document.getElementById('Register').addEventListener('click', ()=>{window.location.href = 'register';});
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
    const logoutQuiz = document.getElementById("logout_Quiz")
    logoutQuiz.addEventListener("click",()=>{window.location.href="/logout"})
}
