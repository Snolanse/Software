function toggleLED() {
    token = getCookie('csrftoken')
    status = document.getElementById('led_status').innerHTML.substr(12)
    if (status == 'True') {
        led_status = 0;
    }
    else if (status == 'False') {
        led_status = 1;
    }
    
    data = {
        'csrfmiddlewaretoken': token,
        'id': 1,
        'stat': led_status
    };
    var posting = $.post("test", data);

    posting.done(function (data) {
        console.log('har oppdatert siden')
        console.log(data.stat)
    })
}