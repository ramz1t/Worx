async function login() {
    var pass = document.getElementById("password").value;
    var email = document.getElementById("email").value;
    var data = {'username': email, 'password': pass};
    var response = await fetch(SERVER_DOMAIN + '/token', {
        method: 'POST',
        headers: {
            'accept': 'application/json'
        },
        body: new URLSearchParams({
            'username': email,
            'password': pass
        })
    });
    console.log(response);
}
