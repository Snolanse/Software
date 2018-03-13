var iknapper;
var jsjekk;
var kslett;
var stegvalgknapper = "";
var testnummer;
var valgtsteg;
var steg;

function leggtilknapper() {

    antknapper = document.getElementById("ant_steg").value;

    for (kslett = 0; kslett < stegvalgknapper.value; kslett++) {
        document.getElementById(kslett).remove();
    }

    for (iknapper = 0; iknapper < antknapper; iknapper++) {

        var node = document.createElement("LI");
        node.setAttribute("id", iknapper);

        stegvalgknapper = document.createElement("INPUT");
        stegvalgknapper.setAttribute("type", "radio");
        stegvalgknapper.setAttribute("name", "radiogruppe");
        stegvalgknapper.setAttribute("value", iknapper + 1);
        stegvalgknapper.setAttribute("id", iknapper);

        document.getElementById("tekstfelt").appendChild(stegvalgknapper);

        node.appendChild(stegvalgknapper);
        document.getElementById("tekstfelt").appendChild(node);
    }
}

function oppdatervalgtsteg() {
    steg = document.getElementsByName("radiogruppe");

    for (jsjekk = 0; jsjekk < steg.length; jsjekk++) {
        if (steg[jsjekk].checked == true) {
            valgtsteg = steg[jsjekk].value;
        }
    }
    document.getElementById("demo").innerHTML = "valgt steg: " + valgtsteg;
}