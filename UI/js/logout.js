window.onload = () => {
    let logoutLink = document.getElementsByTagName('nav')[0];
    logoutLink.addEventListener("click", (event) => {
        if (event.target.attributes.logout.nodeName == "logout") {
            let logoutCommand = event.target.attributes.logout.nodeValue;
            if(sessionStorage.getItem("token") !== null){
                sessionStorage.clear()
                localStorage.clear()
                localStorage.setItem('success',"logged out successfully")
                window.open(logoutCommand,"_self")
            }
        }
    })
}
