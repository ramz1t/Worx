function stringToHash(string) {
            var hash = 0;
            if (string.length == 0) return hash;
            for (i = 0; i < string.length; i++) {
                char = string.charCodeAt(i);
                hash = ((hash << 5) - hash) + char;
                hash = hash & hash;
            }
            return hash;
        }


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
    var passhash = stringToHash(pass);
    var url = SERVER_DOMAIN + '/createaccount/' + email + '/' + passhash + '/' + gender
    var response = fetch(url, {method: "POST", mode: "no-cors"});
    document.getElementById("email").classList.remove('is-invalid');
    document.getElementById("repeatemail").classList.remove('is-invalid');
    document.getElementById("password").classList.remove('is-invalid');
    document.getElementById("repeatpassword").classList.remove('is-invalid');
    document.getElementById("email").value = "";
    document.getElementById("repeatemail").value = "";
    document.getElementById("password").value = "";
    document.getElementById("repeatpassword").value = "";
}
