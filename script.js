// Handle the form submission
document.getElementById('loginForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const role = document.getElementById('role').value;

    // Send data to the backend
    const response = await fetch('http://localhost:8501/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password, role })
    });

    const data = await response.json();

    if (data.success) {
        if (role === 'user') {
            window.location.href = '/user_dashboard';
        } else if (role === 'doctor') {
            window.location.href = '/doctor_dashboard';
        }
    } else {
        alert(data.message);
    }
});
