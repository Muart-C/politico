window.onload = () => {
    if(localStorage.getItem('success') !== null){
        showSuccessMessage("You need to login again");
        window.location.replace("index.html")
    }
}
    function populateUsers(data) {
        for (let index = 0; index < data.length; index++) {
            let options = `
              <option value="${data[index].id}">${data[index].firstname} ${data[index].lastname}</option>
            `
            document.getElementById('user').insertAdjacentHTML('beforeend', options);
          }
        }
        function populateParties(data) {
          for (let index = 0; index < data.length; index++) {
            let options = `
              <option value="${data[index].id}">${data[index].name}</option>
            `
            document.getElementById('party_name').insertAdjacentHTML('beforeend', options);
          }
        }
        function populateOffices(data) {
          for (let index = 0; index < data.length; index++) {
            let options = `
              <option value="${data[index].id}">${data[index].name}</option>
            `
            document.getElementById('office_name').insertAdjacentHTML('beforeend', options);
          }
    }
    function populateCandidatesPage(){
        getUsers();
        getParties();
        getOffices();
    }
    function getParties(){
            let get_parties ={
                method:'GET',
                headers: new Headers(
                    {
                        'Content-Type': 'application/json',
                    }
                )
            }
             fetch(`${BASE_API_URL}/parties`, get_parties)
            .then(res => res.json())
            .then((data) => {
                if(data['data'].length > 0){
                    populateParties(data['data']);
                }else{
                    showSuccessMessage("No Parties were found kindly register");
                }
            })
    }

    function getUsers(){
        let get_users ={
            method:'GET',
            headers: new Headers(
                {
                    'Content-Type': 'application/json',
                }
            )
        }
        fetch(`${BASE_API_URL}/users`, get_users)
        .then(res => res.json())
            .then((data) => {
                if(data['data'].length > 0){
                    populateUsers(data['data']);
                }else{
                    showSuccessMessage("No users were found kindly add users");
                }
            })
    }

    function getOffices(){
        let get_offices ={
            method:'GET',
            headers: new Headers(
                {
                    'Content-Type': 'application/json',
                }
            )
        }
        fetch(`${BASE_API_URL}/offices`, get_offices)
        .then(res => res.json())
            .then((data) => {
                if(data['data'].length > 0){
                    populateOffices(data['data']);
                }else{
                    showSuccessMessage("No offices are registered kindly add one");
                }
            })
    }
    function createCandidate(){
        if(sessionStorage.getItem('admin', true)){
            let token = sessionStorage.getItem('token');
            let candidateId = document.getElementById('user').value;
            let officeId = document.getElementById('office_name').value;
            let partyId = document.getElementById('party_name').value;

            let candidate_data = JSON.stringify({
                candidate_id : parseInt(candidateId),
                party_id : parseInt(partyId),
            })
            let post_candidate = {
                method : 'POST',
                body : candidate_data,
                headers : new Headers({
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + token
                })
            }

            fetch(`${BASE_API_URL}/offices/${officeId}/register`, post_candidate)
            .then(res => res.json())
            .then((data) => {
                if(data.status == 201){
                    showSuccessMessage("Candidate registered successfully");
                }else if(data.status == 409){
                    showErrorMessage('Candidate is already registered');
                }else{
                    sessionExpiry(data['msg']);
                }
            })
            .catch((error) => {
                showErrorMessage('Make sure you choose all the details since they are required fields');
            });
        }else{
            window.location.replace("index.html")
        }
    }
    (() => {
        populateCandidatesPage();
    })()

