async function change_email() {
    var new_email = document.getElementById("New_email").value;
    var password = document.getElementById("password").value;
    var response = await fetch(SERVER_DOMAIN + '/change_email', {
        method: 'POST',
        headers: {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'new_email': new_email
        })
    });

    if (response.status == '201') {
        response = await fetch(SERVER_DOMAIN + '/token', {
                            method: 'POST',
                            headers: {
                                'accept': 'application/json'
                            },
                            body: new URLSearchParams({
                                'username': new_email,
                                'password': password
                            })
                        });
        window.open(SERVER_DOMAIN + '/profile', '_self');
    } else {
        alert('Wrong credentials');
    }
}

async function change_name() {
    var new_name = document.getElementById("New_name").value;
    var response = await fetch(SERVER_DOMAIN + '/change_name', {
        method: 'POST',
        headers: {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'new_name': new_name
        })
    });
    window.open(SERVER_DOMAIN + '/profile', '_self');
}

async function change_gender() {
    if (document.querySelector('input[name="gender"]:checked') != null) {
        var new_gender = document.querySelector('input[name="gender"]:checked').value;
    } else {
        return;
    }
    var response = await fetch(SERVER_DOMAIN + '/change_gender', {
        method: 'POST',
        headers: {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'new_gender': new_gender
        })
    });
    window.open(SERVER_DOMAIN + '/profile', '_self');
}

async function change_password() {
    var new_pass = document.getElementById("New_pass").value;
    var old_pass = document.getElementById("Old_pass").value;
    var repeat_new_pass = document.getElementById("Repeat_new_pass").value;
    var response = await fetch(SERVER_DOMAIN + '/change_password', {
        method: 'POST',
        headers: {
            'accept': 'application/json'
        },
        body: new URLSearchParams({
            "new_password": new_pass,
            "old_password": old_pass
        })
    });
}
