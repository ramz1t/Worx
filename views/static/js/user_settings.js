async function change_email() {
    var new_email = document.getElementById("New_email").value;
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
    console.log(response);
    if (response.status == '201') {
        document.getElementById("email").text = new_email;
    }
}

async function change_name() {
    var new_name = document.getElementById("New_email").value;
    var response = await fetch(SERVER_DOMAIN + '/change_email', {
        method: 'POST',
        headers: {
            'accept': 'application/json'
        },
        body: new URLSearchParams({
            "new_name": new_name
        })
    });
}

async function change_gender() {
    var new_gender = document.getElementById("New_email").value;
    var response = await fetch(SERVER_DOMAIN + '/change_gender', {
        method: 'POST',
        headers: {
            'accept': 'application/json'
        },
        body: new URLSearchParams({
            "new_gender": new_gender
        })
    });
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
