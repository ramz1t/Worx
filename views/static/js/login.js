async function login() {
    var pass = document.getElementById("password").value;
    var email = document.getElementById("email").value;
    var response = await fetch(SERVER_DOMAIN + '/token');
    console.log(response);
}
