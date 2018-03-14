//document.getElementById("hjem").setAttribute("class", 'notactive');
//document.getElementById("lanse").setAttribute("class", 'notactive');
//document.getElementById("info").setAttribute("class", 'notactive');

setTimeout(pressknapp, 20);

function pressknapp() {
    l = document.getElementById("tittel").innerHTML;
    document.getElementById(l).setAttribute("class", 'active');
}