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
    window.open(SERVER_DOMAIN + '/stats/' + reponame + '/' + username, '_self')
}
