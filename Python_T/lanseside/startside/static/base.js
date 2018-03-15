//document.getElementById("hjem").setAttribute("class", 'notactive');
//document.getElementById("lanse").setAttribute("class", 'notactive');
//document.getElementById("info").setAttribute("class", 'notactive');

setTimeout(pressknapp, 20);

function pressknapp() {
    document.getElementById(document.getElementById("tittel").innerHTML).setAttribute("class", 'active');
}