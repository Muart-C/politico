window.onload = () => {
    if(localStorage.getItem('success') !== null){
        showSuccessMessage("You need to login again");
        window.location.replace("index.html")
    }
}
function createOffice(){
    if(sessionStorage.getItem('admin', true)){
        let token = sessionStorage.getItem('token');
        let name = document.getElementById('office_name').value;
        let office_type = document.getElementById('office_type').value;

        let office_data = JSON.stringify({
            name : name,
            office_type : office_type,
        })

        let post_office = {
            method : 'POST',
            body : office_data,
            headers : new Headers({
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + token
            })
        }
        fetch(`${BASE_API_URL}/offices`, post_office)
        .then(res => res.json())
        .then((data) => {
            if(data.status == 201){
                showSuccessMessage(`office Created Successfully`);
            }else if(data.status == 409){
                showErrorMessage(data['error']);
            }else if(data.status == 401){
                sessionStorage.setItem("session_expired", "Your session has expired please log in");
                window.location.replace("index.html")
            }
            else{
                showErrorMessage(data['error']);
            }
        }).catch((error) => {
            showErrorMessage('There is an issue with the internet please try again');
        });
    }
}