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
        console.log(get_parties);
        fetch(`${BASE_API_URL}/parties`, get_parties)
        .then(res => res.json())
        .then((data) => {
            if(data.length > 0){
                getAllParties(data);
                console.log(data);
            }else{
                showSuccessMessage("No parties were registered kindly add one");
            }
        })
        function getAllParties(data){
            let dataBodyHolder = document.getElementsByTagName('tbody')[0];
            for (let index = 0; index < data.length; index++) {
                let dataRow = `
                <tr>
                    <td>${data[index].logo_url}</td>
                    <td>${data[index].name}</td>
                    <td>${data[index].hq_address}</td>
                    <td><a class="button-edit" href="edit_a_political_party_admin.html">Edit</a><a class="button-delete" href="http://delete">Delete</a></td>
                </tr>
               `
               dataBodyHolder.insertAdjacentHTML('afterbegin', dataRow);
            }
        }
    }
}

