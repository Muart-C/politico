const BASE_API_URL = "https://api-politico-v2.herokuapp.com/api/v2/"


function showErrorMessage(message){
    document.getElementById('status').innerText = message
    document.getElementById('status').style.backgroundColor = '#FC2D2D';
    showStatus();
}

function showSuccessMessage(message){
    document.getElementById('status').innerText = message
    document.getElementById('status').style.backgroundColor = '#4FC984';
    showStatus();
}

function showStatus() {
    var statusClass = document.getElementById("status");
    statusClass.className = "show";
    setTimeout(function(){
        statusClass.className = statusClass.className.replace("show", "");
    }, 5000);
  }
