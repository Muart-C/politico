const BASE_API_URL = "127.0.0.1:5000/api/v2"


function showErrorMessage(message){
    document.getElementById('notification_status').innerText = message
    document.getElementById('notification_status').style.backgroundColor = '#FC2D2D';
    showNotificationStatus();
}

function showSuccessMessage(message){
    document.getElementById('notification_status').innerText = message
    document.getElementById('notification_status').style.backgroundColor = '#4FC984';
    showNotificationStatus();
}

function showNotificationStatus() {
    var notificationStatus = document.getElementById("notification_status");
    notificationStatus.className = "make_visible";
    setTimeout(function(){
        notificationStatus.className = notificationStatus.className.replace("make_visible", "");
    }, 5000);
  }
