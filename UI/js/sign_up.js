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

    fetch(`${BASE_API_URL}/auth/signup`, {
        method:'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body : user_data
    }).then(response => response.json())
    .then(data => {
        if(data['data']){
            showSuccessMessage(`${user_data.firstName}, your account was successfully created you can now login into your account`)
            window.location.replace('login.html')
        }
    })
}