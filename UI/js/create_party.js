function createParty(){
    if(sessionStorage.getItem('admin', true)){

        let token = sessionStorage.getItem('token');
        let name = document.getElementById('party_name').value;
        let logoUrl = document.getElementById('logo_url').value;
        let hqAddress = document.getElementById('hq_address').value;

        let party_data = JSON.stringify({
            name : name,
            logoUrl : logoUrl,
            hqAddress : hqAddress,
        })

        let post_party = {
            method : 'POST',
            body : party_data,
            headers : new Headers({
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + token
            })
        }
        fetch(`${BASE_API_URL}/parties`, post_party)
        .then(res => res.json())
        .then((data) => {
            if(data.status == 201){
                showSuccessMessage(`Party ${post_party.name} Created Successfully`);
            }else{
                showErrorMessage(data['error']);
            }
        })
    }
}