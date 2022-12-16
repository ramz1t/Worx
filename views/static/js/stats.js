async function get_stats() {
    if (document.querySelector('input[name="choose_repo"]:checked') != null) {
        var reponame = document.querySelector('input[name="choose_repo"]:checked').value;
    } else {
        return;
    }
    if (document.querySelector('input[name="choose_user"]:checked') != null) {
        var username = document.querySelector('input[name="choose_user"]:checked').value;
    } else {
        return;
    }
    window.open('/stats/' + reponame + '/' + username, '_self')
}

async function set_chosen_repo() {
    if (document.querySelector('input[name="choose_repo"]:checked') != null) {
        var reponame = document.querySelector('input[name="choose_repo"]:checked').value;
    } else {
        return;
    }
    var wrapper = document.getElementById("users_wrapper");
    var users = await fetch('/users/' + reponame)
    var data = await users.json()
    wrapper.innerHTML = "";
    for (let i = 0; i < data.length; i++) {
        var username = data[i];
        var userLi = document.createElement('li');
        var formcheckDiv = document.createElement('div');
        formcheckDiv.classList.add('form-check');
        formcheckDiv.classList.add('navbar-choice');
        var input = document.createElement('input');
        input.setAttribute('type', 'radio');
        input.setAttribute('name', 'choose_user');
        input.setAttribute('id', username);
        input.setAttribute('value', username);
        input.classList.add('form-check-input');
        formcheckDiv.append(input);
        var label = document.createElement('label');
        label.classList.add('form-check-label');
        label.setAttribute('for', username);
        label.innerHTML = username;
        formcheckDiv.append(label);
        userLi.append(formcheckDiv);
        wrapper.append(userLi);
    }
}
