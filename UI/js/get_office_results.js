window.onload = () => {
    if(localStorage.getItem('success') !== null){
        showSuccessMessage("You need to login again");
        window.location.replace("index.html")
    }
}
function getResults(data){
    let dataBodyHolder = document.getElementsByTagName('tbody')[0];
    for (let index = 0; index < data.length; index++) {
        let dataRow = `
        <tr>
            <td>${data[index].candidate}</td>
            <td>Office of the ${data[index].office}</td>
            <td>${data[index].results} Total Votes</td>
        </tr>
       `
       dataBodyHolder.insertAdjacentHTML('afterbegin', dataRow);
    }
}
function getOfficeResults(officeId){
    let get_office ={
        method:'GET',
        headers: new Headers(
            {
                'Content-Type': 'application/json',
            }
        )
    }
    fetch(`${BASE_API_URL}/offices/${officeId}/result`, get_office)
    .then(res => res.json())
    .then((data) => {
        if(data['office']){
            getResults(data['office']);
        }else{
            showSuccessMessage(data['error']);
        }
    })
}

(() => {
    let officeId = new URL(window.location.href).searchParams.get("office_id");
    getOfficeResults(officeId);
})()
