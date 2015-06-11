var currentURL = location.href;
var xmlhttp = new XMLHttpRequest();

xmlhttp.onreadystatechange = function() {
    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
        if (xmlhttp.responseText == 'true') location.reload();
        // console.log(xhr.responseText);
    } else if (xmlhttp.readyState == 4) {
        alert('The server does not respond or an error has ocurred.');
    }
}

// xmlhttp.open('POST', 'http://my.server.url:8801/', true);
xmlhttp.open('POST', 'http://localhost:8801/haschanged', true);
xmlhttp.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
xmlhttp.send('url=' + encodeURIComponent(currentURL));
