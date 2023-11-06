let menuicn = document.querySelector(".menuicn");
let nav = document.querySelector(".navcontainer");

menuicn.addEventListener("click", () => {
    nav.classList.toggle("navclose");
})


const descbox=document.querySelector(".description-box");

var totalRowCount = 0;
var rowCount = 0;
var table = document.getElementById("maintable");
var table = document.getElementById("maintable");
var rows = table.getElementsByTagName("tr");

for (var i = 0; i < rows.length; i++) {
    totalRowCount++;
    if (rows[i].getElementsByTagName("td").length > 0) {
        rowCount++;
    }
}
function showtask(row,btn){
    console.log(row);
    if(btn.textContent=="View"){
        descbox.style.display="flex";
    for(let j=1;j<=rowCount;j++){
            if(j==row)
            continue;
    const tablerow=document.getElementById(`tablerow${j}`);
    const btn2=tablerow.querySelector(".button-tag");
    btn2.textContent="View";
    }
    document.querySelector(".tasktitle1").textContent=`Task ${row}`;  
    btn.textContent="Hide";
    console.log(btn);
    }
    else{
        descbox.style.display="none";
        btn.textContent="View"; 
    }
}
 for(let j=1;j<=rowCount;j++){
    const tablerow=document.getElementById(`tablerow${j}`);
    const btn2=tablerow.querySelector(".button-tag");
    btn2.onclick=function() { console.log(tablerow); showtask(j,btn2);};
}


