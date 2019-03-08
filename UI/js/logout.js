window.onload = () => {
    function deleteParty(partyId){
        if(sessionStorage.getItem('token') !== null){
            let token = sessionStorage.getItem('token');
            let party_id = parseInt(partyId);

            let delete_party = {
                method : 'DELETE',
                headers : new Headers({
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + token
                })
            }

            fetch(`${BASE_API_URL}/parties/${party_id}`, delete_party)
            .then(res => res.json())
            .then((data) => {
                if(data.status == 200){
                    sessionStorage.setItem("delete_success", data['error'])
                    window.location.reload()
                    let delete_party = sessionStorage.getItem("delete_success")
                    showSuccessMessage(delete_party);
                }else{
                    sessionExpiry(data['msg'])
                }
            })
            .catch((error) => {
                showErrorMessage('An issue with the internet connection occurred please try again');
            });
        }else{
            window.location.replace("index.html")
        }
    }
    let tableEl = document.getElementsByTagName("table")[0]
    tableEl.addEventListener("click", (event) => {
        if (event.target.name == "delete_party") {
            let partyId = event.target.attributes.party_id.nodeValue;
            deleteParty(partyId);
        }
    })

    let logoutLink = document.getElementsByTagName('nav')[0];
    logoutLink.addEventListener("click", (event) => {
        if (event.target.attributes.logout.nodeName == "logout") {
            let logoutCommand = event.target.attributes.logout.nodeValue;
            if(sessionStorage.getItem("token") !== null){
                sessionStorage.clear()
                localStorage.setItem('session_expired',"logged out successfully")
                window.open(logoutCommand,"_self")
            }
        }
    })
}
