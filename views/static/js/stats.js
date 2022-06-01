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
    console.log(reponame, username);
    fetch(SERVER_DOMAIN + '/stats', {
        method: 'POST',
        headers: {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'name': reponame,
            'username': username
        })
    });
    window.open()
}
