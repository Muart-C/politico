const BASE_API_URL = "https://api-politico-v2.herokuapp.com/api/v2"


function showErrorMessage(message){
    document.getElementById('notification_status')[0].innerText = message;
    document.getElementById('notification_status')[0].style.backgroundColor = '#FC2D2D';
    showNotificationStatus();
}

function showSuccessMessage(message){
    document.getElementById('notification_status').innerText = message;
    document.getElementById('notification_status').style.backgroundColor = '#4FC984';
    showNotificationStatus();
}

function sessionExpiry(message){
  let error_message = "Your Session "+ message + " Please login again"
  localStorage.setItem("session_expired", error_message);
  window.location.replace("index.html")
}
function showNotificationStatus() {
    var notificationStatus = document.getElementById("notification_status")[0];
    notificationStatus.className = "make_visible";
    setTimeout(function(){
    notificationStatus.className = notificationStatus.className.replace("make_visible", "");
    }, 5000);
  }

  function triggerAdminDefaults(){
    initParties();
  }
