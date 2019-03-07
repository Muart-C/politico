let tableEl = document.getElementById('logout_user').value;
console.log(tableEl)
    tableEl.addEventListener("click", (event) => {
        if (event.target.name == "logout") {
            let logoutCommand = event.target.attributes.party_id.nodeValue;
            console.log(logoutCommand)
        }
    })