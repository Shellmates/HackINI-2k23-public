function submitLogRegForm(event) {
    event.preventDefault();
    let formData = new FormData(event.target);
    
    var data = {};
    formData.forEach((value, key) => data[key] = value);
    
    let xhr = new XMLHttpRequest();
    xhr.addEventListener("load", reqListener);
    xhr.open(event.target.method, event.target.action);
    xhr.setRequestHeader('Content-type', 'application/json');
    xhr.send(JSON.stringify(data));
}

function reqListener() {
    let { success, message } = JSON.parse(this.response);

    let div = document.createElement("div");
    div.innerHTML = message;
    div.id = "result-submit";
    if (success) {
        div.className = "text-success text-center";
        if (window.location.pathname === '/login') window.location.reload();
    } else 
        div.className = "text-danger text-center";
   
    // if this element exists already, remove it
    let elem = document.getElementById(div.id);
    if (elem !== null) elem.remove();

    // attach it the new one
    let parent = document.getElementById("form");
    parent.prepend(div);

}

document.getElementById("form").onsubmit = submitLogRegForm;