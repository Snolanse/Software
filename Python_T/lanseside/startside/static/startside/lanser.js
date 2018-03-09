//setInterval(function () {
//    window.location.reload(false);
//}, 1000);

$(function faadata(idnavn) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    $(document).ready(function () {
        $(idnavn).click(function (e) {
            //e.preventDefault();
            console.log('plz')
            $.ajax({
                type: "POST",
                url: "valgtlanse",
                data: {
                    'csrfmiddlewaretoken': csrftoken,
                    'test': 'FUNKFORFAEN'

                },
                success: function (result) {
                    href = "valgtlanse";
                    alert('ok');
                },
                error: function (result) {
                    alert('error');
                }
            });
        });
    });
})