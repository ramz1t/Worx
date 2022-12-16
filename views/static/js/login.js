async function login() {
    var pass = document.getElementById("password").value;
    var email = document.getElementById("email").value;
    var data = { 'username': email, 'password': pass };
    var response = await fetch('/token', {
        method: 'POST',
        headers: {
            'accept': 'application/json'
        },
        body: new URLSearchParams({
            'username': email,
            'password': pass
        })
    });
    if (response.status == '200') {
        window.open(SERVER_DOMAIN + '/main', '_self');
    } else {
        alert(response.status);
    }
}
