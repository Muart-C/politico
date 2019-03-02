const login_user = 'https://api-politico-v2.herokuapp.com/api/v2/auth/login';

if(window.localStorage.getItem('email') !== null){
    document.getElementById('notification_status').innerText = `You successfully created your account go ahead and login to your account`;
    document.getElementById('notification_status').style.backgroundColor = '#4FC984';
    document.getElementById('notification_status').className = "make_visible";
}

function userLogin() {
    let email = document.getElementById('email').value;
    let password = document.getElementById('password').value;
    let login_data = JSON.stringify({
        email: email,
        password: password
    });
    let post_user ={
        method:'POST',
        body : login_data,
        headers: new Headers(
            {
                'Content-Type': 'application/json',
            }
        )
    }
    fetch(login_user, post_user)
    .then(res => res.json())
    .then((data) => {
        if (data['token']) {
            let token = data['token'];
            window.localStorage.setItem('token', token);
            window.localStorage.setItem('admin', admin);
            if(admin){
                window.location.replace('admin.html');
            }else{
                window.location.replace('user.html');
            }
        }else{
            showErrorMessage("An error occurred while logging in to your account");
            //console.log(data.status);
        }
    })
    .catch(error => console.error('Error:', error));
}