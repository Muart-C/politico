window.onload = () => {
    function getCandidates(data){
        let dataBodyHolder = document.getElementsByTagName('tbody')[0];
        for (let index = 0; index < data.length; index++) {
            let dataRow = `
            <tr>
                <td><img src="${data[index].passport_url}" alt="${data[index].candidate} Passport"> </td>
                <td>${data[index].candidate}</td>
                <td>${data[index].office}</td>
                <td>${data[index].party}</td>
                <td><a class="button-edit" name="vote" party="jama" id="${data[index].candidate_id}">Vote</a></td>
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
        let tableEl = document.getElementsByTagName("table")[0]
        tableEl.addEventListener("click", (event) => {
            if (event.target.name == "vote") {
                console.log(event.target.attributes.party.nodeValue);
                vote(parseInt(event.target.attributes.party.nodeValue))
            }
        })
    })()
}