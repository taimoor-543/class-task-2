async function login() {
    let username = document.getElementById("loginUser").value;
    let password = document.getElementById("loginPass").value;

    let response = await fetch("http://localhost:5000/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
    });

    let result = await response.json();
    alert(result.message);
}

async function signup() {
    let username = document.getElementById("signupUser").value;
    let password = document.getElementById("signupPass").value;

    let response = await fetch("http://localhost:5000/signup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
    });

    let result = await response.json();
    alert(result.message);
}
