var iknapper;
var jsjekk;
var kslett;
var stegvalgknapper = "";
var testnummer;
var valgtsteg;
var steg;
var node = "";
var nodelabel = "";
var nodespan = "";

function leggtilknapper() {

    antknapper = document.getElementById("ant_steg").value;

    for (kslett = 0; kslett < stegvalgknapper.value; kslett++) {

        document.getElementById(kslett).remove();
        document.getElementById("mark" + kslett).remove();

    }

    for (iknapper = 0; iknapper < antknapper; iknapper++) {

        node = document.createElement("LI");
        node.setAttribute("id", "mark" + iknapper);
        node.setAttribute("name", "mark");

        stegvalgknapper = document.createElement("INPUT");
        stegvalgknapper.setAttribute("type", "radio");
        stegvalgknapper.setAttribute("name", "radiogruppe");
        stegvalgknapper.setAttribute("class", "radiogruppene");
        stegvalgknapper.setAttribute("value", iknapper + 1);
        stegvalgknapper.setAttribute("id", iknapper);

        nodelabel = document.createElement("LABEL");
        nodelabel.setAttribute("id", "container" + iknapper);
        nodelabel.setAttribute("class", "container");

        nodespan = document.createElement("SPAN");
        nodespan.setAttribute("id", "checkmark" + iknapper);
        nodespan.setAttribute("class", "checkmark");

        document.getElementById("tekstfelt").appendChild(node);
        document.getElementById("mark" + iknapper).appendChild(nodelabel);
        document.getElementById("container" + iknapper).appendChild(stegvalgknapper);
        document.getElementById("container" + iknapper).appendChild(nodespan);

        document.getElementById("container" + iknapper).innerHTML += "Steg nr. " + stegvalgknapper.value;

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
function minfunksjon() {

    document.getElementById("2").checked = true;

}