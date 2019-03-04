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
            let admin = data['is_admin'];
            sessionStorage.setItem('token', token);
            sessionStorage.setItem('admin', admin);
            if(admin == true){
                window.location.replace('view_list_of_political_parties_admin.html');
            }else{
                window.location.replace('view_list_of_vying_politicians.html');
            }
        }else{
            showErrorMessage(data['error']);
            console.log(data.status);
        }
    })
    .catch(error => console.error('Error:', error));
}