const create_user_url = 'https://api-politico-v2.herokuapp.com/api/v2/auth/signup';
function userSignUp() {
    let first_password = document.getElementById('password').value;
    let confirm_password = document.getElementById('confirm-password').value;

    if (first_password != confirm_password) {
        showErrorMessage("Ensure the password and confirm password match");
        return;
    }
    let firstName = document.getElementById('first_name').value;
    let lastName = document.getElementById('last_name').value;
    let otherName = document.getElementById('other_name').value;
    let email = document.getElementById('email').value;
    let passportUrl = document.getElementById('passport_url').value;
    let phoneNumber = document.getElementById('phone_number').value;
    let password = document.getElementById('password').value;

    let user_data = JSON.stringify({
        firstname:firstName,
        lastname: lastName,
        othername: otherName,
        email: email,
        passport_url: passportUrl,
        phone_number : phoneNumber,
        password: password,
        is_admin: false
    })
    let post_user ={
        method:'POST',
        body : user_data,
        headers: new Headers(
            {
                'Content-Type': 'application/json',
            }
        )
    }
    fetch(create_user_url, post_user)
    .then(res => res.json())
    .then((data) => {
        if (data.status == 201) {
            showSuccessMessage(`${user_data.firstName} you successfully created your account go ahead and login to your account`);
            setTimeout(function () {
                window.location.replace("index.html");
            }, 4000);
        }else{
            showErrorMessage("An error occurred while creating a new user");
            console.log(data.status);
        }
    })
    .catch(error => console.error('Error:', error));
}