window.onload = () => {
    function vote(officeId,candidateId, partyId){
        if(sessionStorage.getItem('token') !== null){
            let token = sessionStorage.getItem('token');
            let vote_data = JSON.stringify({
                office_id : parseInt(officeId),
                candidate_id : parseInt(candidateId),
                party_id : parseInt(partyId),
            })
            let post_vote = {
                method : 'POST',
                body : vote_data,
                headers : new Headers({
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + token
                })
            }

            fetch(`${BASE_API_URL}/votes`, post_vote)
            .then(res => res.json())
            .then((data) => {
                if(data.status == 201){
                    showSuccessMessage("You voted Successfully Check out other offices and vote for other candidates");
                }else if(data.status == 409){
                    showErrorMessage('You have already voted for this office vote for other offices');
                }else{
                    sessionExpiry(data['msg']);                }
            })
            .catch((error) => {
                showErrorMessage('Make sure you choose all the details since they are required fields');
            });
        }else{
            window.location.replace("index.html")
        }
    }
    let tableEl = document.getElementsByTagName("table")[0]
    tableEl.addEventListener("click", (event) => {
    if (event.target.name == "vote") {
        let partyId = event.target.attributes.party_id.nodeValue;
        let candidateId = event.target.attributes.candidate_id.nodeValue;
        let officeId = event.target.attributes.office_id.nodeValue;
        vote(officeId, candidateId, partyId);
    }
})
}