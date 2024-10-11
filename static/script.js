
function goToLogin() {
    window.location.href = 'login';
}

function goToRegister() {
    window.location.href = 'register';
}

document.getElementById('Login').addEventListener('click', goToLogin);
document.getElementById('Register').addEventListener('click', goToRegister);
