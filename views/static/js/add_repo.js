function add_repo() {
        var reponame = document.getElementById("repository_name").value.toLowerCase();
        var ownername = document.getElementById("owner_name").value.toLowerCase();
        var repourl = document.getElementById("repourl").value.toLowerCase();
        if (reponame != "" && ownername != "") {
            var url = SERVER_DOMAIN + "/addrepo/" + reponame + "/" + ownername;
            var response = fetch(url, {method: "POST", mode: "no-cors"});
            document.getElementById('closerepo').click();
            document.getElementById("repository_name").value = "";
            document.getElementById("owner_name").value = "";
            document.getElementById("repourl").value = "";
            document.getElementById("inputerror").style = "visibility: hidden";
        } else if (repourl != "") {
            var url = repourl.slice(18);
            var a = url.split("/");
            reponame = a[2];
            ownername = a[1];
            var url = SERVER_DOMAIN + "/addrepo/" + reponame + "/" + ownername;
            var response = fetch(url, {method: "POST", mode: "no-cors"});
            document.getElementById('closerepo').click();
            document.getElementById("repository_name").value = "";
            document.getElementById("owner_name").value = "";
            document.getElementById("repourl").value = "";
            document.getElementById("inputerror").style = "visibility: hidden";
        } else {
            document.getElementById("inputerror").style = "visibility: visible";
        }
    }
