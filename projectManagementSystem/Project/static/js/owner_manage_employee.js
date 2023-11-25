function deleteRow(r) {
    i=r.parentNode.parentNode.rowIndex;
   let text = "Press a OK for Delete Task!";
   if (confirm(text) == true) {
       document.getElementById("maintable").deleteRow(i);
   } else {
       text = "You canceled!";
   }
}
function Confirmrole(r) {
    i=r.parentNode.parentNode.rowIndex;
   let text = "Press a OK for Change Role";
   if (confirm(text) == true) {
     const managertablerow=document.getElementById(`managertablerow${i}`);
     const btn2=managertablerow.querySelector(".button-tag");
     if (btn2.textContent==="Manager") {
        btn2.textContent="Employee"; 
     } 
     else if (btn2.textContent==="Employee") {
        btn2.textContent="Manager"; 
     } 
   } else {
       text = "You canceled!";
   }
}
function Confirmrole2(r) {
    i=r.parentNode.parentNode.rowIndex;
   let text = "Press a OK for Change Role";
   if (confirm(text) == true) {
     const employeetablerow=document.getElementById(`employeetablerow${i}`);
     const btn2=employeetablerow.querySelector(".button-tag");
     if (btn2.textContent==="Manager") {
        btn2.textContent="Employee"; 
     } 
     else if (btn2.textContent==="Employee") {
        btn2.textContent="Manager"; 
     } 
   } else {
       text = "You canceled!";
   }
}

let menuicn = document.querySelector(".menuicn");
let nav = document.querySelector(".navcontainer");

menuicn.addEventListener("click", () => {
	nav.classList.toggle("navclose");
})
