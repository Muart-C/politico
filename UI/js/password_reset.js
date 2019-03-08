const send_reset_url = 'https://api-politico-v2.herokuapp.com/api/v2/auth/reset';
const new_password_url = 'https://api-politico-v2.herokuapp.com/api/v2/reset';
function requestPasswordReset() {
    let email = document.getElementById('email').value;
    console.log(email)
    let post_email = {
        method: 'POST',
        headers: new Headers({
            'Content-Type': 'application/json',
        }),
        body: JSON.stringify({
            email: email
        }),
    }
    fetch(send_reset_url, post_email)
    .then(res => res.json())
    .then((data) => {
        let message = data['message']
        let error = data['error']
     if (message) {
         alert("Check your email for password reset link")
     }else if(error){
        alert("Your email does not exist register as new user")
     }
    })
    .catch((error) => {
        console.log(error)
    });
}


function updatePassword() {
    let email = document.getElementById('email').value
    let password = document.getElementById('password').value
    let confirmPassword = document.getElementById('confirm-password').value
    if (password !== confirmPassword){
        showErrorMessage('Ensure your Password match');
        return;
    }
    fetch(new_password_url, {
        method: 'POST',
        headers: new Headers({
            'Content-Type': 'application/json',
        }),
        body: JSON.stringify({
            password : password,
            email : email
        }),
    })
    .then(res => res.json())
    .then((data) => {
        console.log(data)
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
