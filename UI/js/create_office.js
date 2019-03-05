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
            }else{
                showErrorMessage(data['error']);
            }
        })
    }
}