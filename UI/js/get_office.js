    function getCandidates(data){
        let dataBodyHolder = document.getElementsByTagName('tbody')[0];
        for (let index = 0; index < data.length; index++) {
            let dataRow = `
            <tr>
                <td><img src="${data[index].passport_url}" alt="${data[index].candidate} Passport"> </td>
                <td>${data[index].candidate}</td>
                <td>${data[index].office}</td>
                <td>${data[index].party}</td>
                <td><a class="button-edit" name="vote" party_id="${data[index].party_id}" candidate_id="${data[index].candidate_id}" office_id="${data[index].office_id}">Vote</a></td>
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
            if(data['data']){
                getCandidates(data['data']);
            }else{
                showSuccessMessage(data['error']);
            }
        })
    }

    (() => {
        let officeId = new URL(window.location.href).searchParams.get("office_id");
        getOfficeCandidates(officeId);
    })()
