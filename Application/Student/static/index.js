document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('loginForm');

    loginForm.addEventListener('submit', function(event) {
        event.preventDefault(); 
        
        const email = document.getElementById('emailInput').value;
        const password = document.getElementById('passwordInput').value;
        
        console.log(`Attempting login with: Email: ${email}, Password: ${password}`);
        
        if (email.trim() === "" || password.trim() === "") {
            alert('Please fill out all fields.');
            return;
        }

        

        alert("Login attempt successful (Placeholder). Redirecting to dashboard...");
       
    });
});

function handleSocialLogin(provider) {
    console.log(`Initiating login via ${provider}...`);
    
    alert(`Redirecting to ${provider} authentication page...`);
}