function sendGQL(query, callback) {
    let xhr = new XMLHttpRequest();
    xhr.addEventListener("load", callback);
    xhr.open("POST", "/graphql");
    xhr.setRequestHeader('Content-type', 'application/json');
    xhr.send(JSON.stringify(query));
}

function getData() {
    let query = {query: `
        {
            user { 
                username,
                email
            }
        }
    `};

    sendGQL(query, reqListener)
}

function reqListener() {
    let info = JSON.parse(this.response).data.user;

    let div = document.getElementById('username');
    div.innerHTML = info.username;

    div = document.getElementById('email');
    div.innerHTML = info.email;
}

getData();