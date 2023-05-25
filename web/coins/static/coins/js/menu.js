
async function getJsonData() {
    const response = await fetch("http://127.0.0.1:8000/month/2022-01-01/");
    const data = await response.json();
    return data;
}

function insertButonOfElements() {
    var data = getJsonData();
    console.log(data)
    // Get menu element
    var menu = document.getElementById("sidebar");
    // Create a buton
    var ele1 = document.createElement("button");
    ele1.setAttribute("class", "accordion");
    var node = document.createTextNode("Section 4");
    ele1.appendChild(node);
    var ele2 = document.createElement("div");
    ele2.setAttribute("class", "panel");
    // Add to menu
    menu.appendChild(ele1);
    var ele3, ele4 = "";
    for (ra in data["rates"]) {
        ele3 = document.createElement("p");
        ele4 = document.createElement("a");
        ele4.setAttribute("href", "#" + data["rates"])
        node = document.createTextNode("Link " + ra);
        ele4.appendChild(node);
        ele3.appendChild(ele4);
        ele2.appendChild(ele3);
    }
    menu.appendChild(ele2);
};

function ready() {
    insertButonOfElements();
    var acc = document.getElementsByClassName("accordion");
    var i;

    for (i = 0; i < acc.length; i++) {
        acc[i].addEventListener("click", function () {
            // Toggle between adding and removing the "active" class,
            // to highlight the button that controls the panel
            this.classList.toggle("active");
            // Toggle between hiding and showing the active panel
            var panel = this.nextElementSibling;
            if (panel.style.display === "block") {
                panel.style.display = "none";
            } else {
                panel.style.display = "block";
            }
        });
    }
};

document.addEventListener("DOMContentLoaded", ready);