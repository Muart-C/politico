function getAllOffices(data){
    let dataBodyHolder = document.getElementsByTagName('tbody')[0];
    for (let index = 0; index < data.length; index++) {
        let dataRow = `
        <tr>
            <td>${data[index].name}</td>
            <td>${data[index].office_type}</td>
            <td><a class="button-edit" href="view_government_office.html?office_id=${data[index].id}">View Details</a></td>
        </tr>
       `
       dataBodyHolder.insertAdjacentHTML('afterbegin', dataRow);
    }
}

function initOffices() {
    if(sessionStorage.getItem('token') !== null){
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
                getAllOffices(data['data']);
            }else{
                showSuccessMessage("No offices kindly register them");
            }
        })
    }else{
        window.localStorage.setItem("session_expired", "Your session has expired please log in");
        window.location.replace("index.html");
    }
}


function getAllOfficesUsers(data){
    let dataBodyHolder = document.getElementsByTagName('tbody')[0];
    for (let index = 0; index < data.length; index++) {
        let dataRow = `
        <tr>
            <td>${data[index].name}</td>
            <td>${data[index].office_type}</td>
            <td><a class="button-edit" href="view_government_office.html?office_id=${data[index].id}">Proceed to vote</a></td>
        </tr>
       `
       dataBodyHolder.insertAdjacentHTML('afterbegin', dataRow);
    }
}

function initOfficesUsers() {
    if(sessionStorage.getItem('token') !== null){
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
                getAllOfficesUsers(data['data']);
            }else{
                showSuccessMessage("No offices kindly register them");
            }
        })
    }else{
        window.localStorage.setItem("session_expired", "Your session has expired please log in");
        window.location.replace("index.html");
    }
}

