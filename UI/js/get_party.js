function getParty(partyId){
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
        if(data['data'].length > 0){
            let party_name = data['data']['name'];
            localStorage.setItem('name', party_name);
        }else{
            showSuccessMessage("No party with such an id was found");
        }
    })
}