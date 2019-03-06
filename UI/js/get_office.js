function getCandidates(data){
    let dataBodyHolder = document.getElementsByTagName('tbody')[0];
    for (let index = 0; index < data.length; index++) {
        let dataRow = `
        <tr>
            <td>${data[index].passport_url}</td>
            <td>${data[index].candidate}</td>
            <td>${data[index].office}</td>
            <td>${data[index].party}</td>
            <td><a class="button-edit" href="view_offices.html?office_id=${data[index].id}">Vote</a></td>
        </tr>
       `
       dataBodyHolder.insertAdjacentHTML('afterbegin', dataRow);
    }
}
function getOfficeCandidates(officeId){
    let get_office ={
        method:'GET',
        headers: new Headers(
            {
                'Content-Type': 'application/json',
            }
        )
    }
    fetch(`${BASE_API_URL}/offices/${officeId}/candidates`, get_office)
    .then(res => res.json())
    .then((data) => {
        if(data['data'].length > 0){
            getCandidates(data['data']);
        }else{
            showSuccessMessage("No politicians that applied for office");
        }
    })
}
