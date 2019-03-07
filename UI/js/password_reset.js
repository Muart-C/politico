function requestPasswordReset() {
    let email = document.getElementById('email').value;
    fetch(`${BASE_API_URL}/auth/reset`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            email: email
        }),
    })
    .then(res => res.json())
    .then((data) => {
        if (data.status === 200) {
            showSuccessMessage(data['message']);
        }else {
            showErrorMessage(data['error']);
        }

    })
    .catch((error) => {
        showErrorMessage('An error occurred while checking your email');
    });
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