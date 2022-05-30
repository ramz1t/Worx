function submit() {
    var pass = document.getElementById("password").value;
    var subpass = document.getElementById("repeatpassword").value;
    var email = document.getElementById("email").value;
    var subemail = document.getElementById("repeatemail").value;
    if (email.search("@") == -1 || email == "") {
        document.getElementById("email").classList.add('is-invalid');
        return;
    }
    if (email != subemail) {
        document.getElementById("email").classList.add('is-invalid');
        document.getElementById("repeatemail").classList.add('is-invalid');
        return;
    }
    if (pass == "") {
        document.getElementById("password").classList.add('is-invalid');
        return;
    }
    if (pass != subpass) {
        document.getElementById("password").classList.add('is-invalid');
        document.getElementById("repeatpassword").classList.add('is-invalid');
        return;
    }
    if (document.querySelector('input[name="gender"]:checked') != null) {
        var gender = document.querySelector('input[name="gender"]:checked').value;
    } else {
        return;
    }
    var url = SERVER_DOMAIN + '/createaccount/' + email + '/' + pass + '/' + gender;
    var response = fetch(url, {method: "POST", mode: "no-cors"});
    document.getElementById("email").classList.remove('is-invalid');
    document.getElementById("repeatemail").classList.remove('is-invalid');
    document.getElementById("password").classList.remove('is-invalid');
    document.getElementById("repeatpassword").classList.remove('is-invalid');
    document.getElementById("email").value = "";
    document.getElementById("repeatemail").value = "";
    document.getElementById("password").value = "";
    document.getElementById("repeatpassword").value = "";
    window.open(SERVER_DOMAIN + '/', '_self');
}
