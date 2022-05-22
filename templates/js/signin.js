function signin() {
    var email = document.getElementById('email').value;
    var pass = document.getElementById('password').value;
    var url = SERVER_DOMAIN + '/token';
    var response = fetch(url, {method: 'POST', mode: 'no-cors', body: {username: email, password: pass}});
    console.log(response);
}
