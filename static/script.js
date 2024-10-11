
function goToLogin() {
    window.location.href = 'login'; // Redirect to the login page
}

// Function to redirect to the registration page
function goToRegister() {
    window.location.href = 'register'; // Redirect to the registration page
}

// Event listeners for button clicks
document.getElementById('Login').addEventListener('click', goToLogin);
document.getElementById('Register').addEventListener('click', goToRegister);
