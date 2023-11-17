function deleteRow(r) {
     i=r.parentNode.parentNode.rowIndex;
    let text = "Press a OK for Delete Task!";
    if (confirm(text) == true) {
        document.getElementById("maintable").deleteRow(i);
    } else {
        text = "You canceled!";
    }
}

const descbox2=document.querySelector(".description-box");

function showtask2(row){
  if(descbox2.style.display=="none"){
      descbox2.style.display="flex";
      document.querySelector(".tasktitle1").textContent=`Task ${row}`;      
      document.querySelector("#taskdetails").textContent="Hide Details";
      document.querySelector(".desc-box").style.justifyContent="space-between";
  }  
  else{
      descbox2.style.display="none";    
      document.querySelector(".desc-box").style.justifyContent="center";
      document.querySelector("#taskdetails").textContent="Task Details";
  }
}

const descbox=document.querySelector(".details-container");

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
    // console.log(row);
    descbox2.style.display="none"; 
     if(btn.textContent=="View"){
        document.querySelector(".desc-box").style.justifyContent="center";
        document.querySelector("#taskdetails").textContent="Task Details";
         descbox.style.display="flex";
    for(let j=1;j<=rowCount;j++){
            if(j==row)
            continue;
    const tablerow=document.getElementById(`tablerow${j}`);
    const btn2=tablerow.querySelector(".button-tag");
    btn2.textContent="View";
    }
    btn.textContent="Hide";
    // console.log(btn);
}

else{
    descbox.style.display="none";
    btn.textContent="View";
}
}
document.querySelector("#taskdetails").addEventListener('click',()=>{
    for(let j=1;j<=rowCount;j++){
        const tablerow=document.getElementById(`tablerow${j}`);
        const btn2=tablerow.querySelector(".button-tag");
        if(btn2.textContent=="Hide"){
            showtask2(j);
        }
    }
});
document.querySelector("#deletebtn").addEventListener('click',()=>{
    for(let j=1;j<=rowCount;j++){
        const tablerow=document.getElementById(`tablerow${j}`);
        const btn2=tablerow.querySelector(".button-tag");
        if(btn2.textContent=="Hide"){
            deleteRow(btn2);
            descbox.style.display="none";
            descbox2.style.display="none";

        }
    }
});
 for(let j=1;j<=rowCount;j++){
    const tablerow=document.getElementById(`tablerow${j}`);
    const btn2=tablerow.querySelector(".button-tag");
    btn2.onclick=function() { console.log(tablerow); showtask(j,btn2);};
}

document.querySelector(".statuscheck").addEventListener('click',()=>{
    if(document.querySelector(".statuscheck").textContent=="Submitted for review"){
        let text = "Press a OK for Submit Task!";
        if (confirm(text) == true) {
            document.querySelector(".statuscheck").textContent="Compeleted";
        } else {
            document.querySelector(".statuscheck").textContent="Pending";
        }
    }
});