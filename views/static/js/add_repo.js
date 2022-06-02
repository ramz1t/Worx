async function add_repo() {
        var reponame = document.getElementById("repository_name").value.toLowerCase();
        var ownername = document.getElementById("owner_name").value.toLowerCase();
        var repourl = document.getElementById("repourl").value.toLowerCase();
        if (reponame != "" && ownername != "") {
            var response = await fetch(SERVER_DOMAIN + '/addrepo', {
                            method: 'POST',
                            headers: {
                                'accept': 'application/json',
                                'Content-Type': 'application/json'
                            },
                            body: JSON.stringify({
                                'name': reponame,
                                'owner_username': ownername
                            })
            });
        } else if (repourl != "") {
            var a = url.split("/");
            reponame = a[2];
            ownername = a[1];
            var response = await fetch(SERVER_DOMAIN + '/addrepo', {
                            method: 'POST',
                            headers: {
                                'accept': 'application/json',
                                'Content-Type': 'application/json'
                            },
                            body: JSON.stringify({
                                'name': reponame,
                                'owner_username': ownername
                            })
            });
        } else {
            document.getElementById("inputerror").style = "visibility: visible";
        }
        if (response.ok) {
            document.getElementById('closerepo').click();
            document.getElementById("repository_name").value = "";
            document.getElementById("owner_name").value = "";
            document.getElementById("repourl").value = "";
            document.getElementById("inputerror").style = "visibility: hidden";
            window.open(window.location.href, '_self');
        } else {
            alert('error while adding repo');
        }
    }
