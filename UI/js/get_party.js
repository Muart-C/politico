window.onload = () => {
    if(localStorage.getItem('success') !== null){
        showSuccessMessage("You need to login again");
        window.location.replace("index.html")
    }
}
function getPartyPartyName(partyId){
    let get_party ={
        method:'GET',
        headers: new Headers(
            {
                'Content-Type': 'application/json',
            }
        )
    }
    fetch(`${BASE_API_URL}/parties/${partyId}`, get_party)
    .then(res => res.json())
    .then((data) => {
        if(data['data']['id'] !== null){
            let party_name = data['data']['name'];
            let name = document.getElementById('party_name');
            name.value = party_name
        }else{
            showSuccessMessage("No party with such an id was found");
        }
    })
}
