function getAllParties(data){
    let dataBodyHolder = document.getElementsByTagName('tbody')[0];
    for (let index = 0; index < data.length; index++) {
        let dataRow = `
        <tr>
            <td><img src="${data[index].logo_url}" alt="${data[index].name} Logo"> </td>
            <td>${data[index].name}</td>
            <td>${data[index].hq_address}</td>
            <td><a class="button-edit" href="edit_a_political_party_admin.html?party_id=${data[index]}">Edit</a><a class="button-delete" href="http://delete">Delete</a></td>
        </tr>
       `
       dataBodyHolder.insertAdjacentHTML('afterbegin', dataRow);
    }
}
function initParties() {
    if(sessionStorage.getItem('admin', true)){
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
                getAllParties(data['data']);
            }else{
                showSuccessMessage("No parties were registered kindly add one");
            }
        })
    }else{
        window.location.replace("index.html");
    }
}

