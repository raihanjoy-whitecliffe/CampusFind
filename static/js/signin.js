document.getElementById('signin-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const emailInput = document.getElementById('email').value.trim();
    const passwordInput = document.getElementById('password').value;
    const errorMsg = document.getElementById('error-msg');

    // test for validation
    const validEmail = "student@campus.edu";
    const validPassword = "password123";

    // Validation 
    if (emailInput === validEmail && passwordInput === validPassword) {
        errorMsg.style.display = "none";
        alert("Login successful! Redirecting to home page...");
        window.location.href = "index.html"; //redirects to home page
    } else {
        errorMsg.textContent = "Invalid campus email or password. Please try again.";
        errorMsg.style.display = "block"; // Shows error on screen
    }
});