const send_reset_url = 'https://api-politico-v2.herokuapp.com/api/v2/auth/reset';
function requestPasswordReset() {
    let email = document.getElementById('email').value;
    console.log(email)
    fetch(send_reset_url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            email: email
        }),
    })
    console.log(BASE_API_URL)
    .then(res => res.json())
    .then((data) => {
        console.log(data.status)
        // if (data.status === 200) {
        //     showSuccessMessage(data['message']);
        // }else {
        //     showErrorMessage(data['error']);
        // }

    })
    // .catch((error) => {
    //     showErrorMessage('An error occurred while checking your email');
    // });
}


function updatePassword() {
    let password = document.getElementById('password').value
    let confirmPassword = document.getElementById('confirm-password').value
    if (password !== confirmPassword){
        showErrorMessage('Ensure your Password match');
        return;
    }
    fetch(`${BASE_URL}/reset`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
            password:password
        }),
    })
    .then(res => res.json())
    .then((data) => {
        if (data.status === 200) {
            showSuccessMessage('Your password has been updated')
            setTimeout(function(){
                 window.location.replace('index.html')
            }, 3000);

        }else {
            showErrorMessage(data['error'])
        }

    })
    .catch((error) => {
        showErrorMessage('Ensure you are connected to internet')
    });
}