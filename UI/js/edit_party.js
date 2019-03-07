window.onload = () => {
    if(localStorage.getItem('success') !== null){
        showSuccessMessage("You need to login again");
        window.location.replace("index.html")
    }
}
let partyID = new URL(window.location.href).searchParams.get("party_id");
function editPartyName() {
    if(sessionStorage.getItem('admin', true)){
        let token = sessionStorage.getItem('token');
        let party_name = document.getElementById('party_name').value;

        let updated_name = JSON.stringify({
            name:party_name,
        });

        let patch_party = {
            method : 'PATCH',
            body : updated_name,
            headers : new Headers({
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + token
            })
        };
        fetch(`${BASE_API_URL}/parties/${partyID}/name`, patch_party)
        .then(res => res.json())
        .then((data) => {
            if(data.status == 200){
                showSuccessMessage(`Party Name Successfully Updated`);
            }else if(data.status == 401){
                sessionStorage.setItem("session_expired", "Your session has expired please log in");
                window.location.replace("index.html");
            }
            else{
                showErrorMessage(data['error']);
            }
        }).catch((error) => {
            showErrorMessage('There is an issue with the internet please try again');
        });
    }else{
        window.location.replace("index.html")
    }
}