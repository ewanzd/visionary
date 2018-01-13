const READ = 'GET';
const CREATE = 'POST';
const UPDATE = 'PUT';
const DELETE = 'DELETE';

function sendRequest(url, httpMethod, data) {
  var request = new XMLHttpRequest();
  request.open(httpMethod, url, false);
  request.setRequestHeader("Authorization", "Basic " + btoa("admin:password123"));
  request.setRequestHeader("X-CSRFToken", readCookie("csrftoken"));
  request.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  if (typeof data !== 'undefined') {
    request.send(data);
  }
  else {
    request.send();
  }
  if(request.responseText) {
    return JSON.parse(request.responseText);
  }
  return {};
}

function readCookie(name) {
 var nameEQ = encodeURIComponent(name) + "=";
 var ca = document.cookie.split(';');
 for (var i = 0; i < ca.length; i++) {
 var c = ca[i];
 while (c.charAt(0) === ' ') c = c.substring(1, c.length);
 if (c.indexOf(nameEQ) === 0) return decodeURIComponent(c.substring(nameEQ.length, c.length));
 }
 return null;
}
