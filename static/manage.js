function sendRequest(httpMethod, path, jsonObj) {
  var request = new XMLHttpRequest();
  request.open(httpMethod, "http://127.0.0.1:8000/" + path, false);
  request.setRequestHeader("Authorization", "Basic " + btoa("admin:password123"));
  request.setRequestHeader("X-CSRFToken", readCookie("csrftoken"));
  request.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  request.send(jsonObj);
  var array = JSON.parse(request.responseText);
  return array;
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
