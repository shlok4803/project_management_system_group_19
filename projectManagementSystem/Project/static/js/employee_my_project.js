let menuicn = document.querySelector(".menuicn");
let nav = document.querySelector(".navcontainer");

menuicn.addEventListener("click", () => {
    nav.classList.toggle("navclose");
})

function myFunction(filter) {
  var table, tr, td, i, txtValue;
  // input = document.getElementById("myInput");
  // filter = input.value.toUpperCase();
  if(filter==="I"){
    filter="Pending";
  }
  if(filter==="C"){
    filter="Completed";
  }
  filter=filter.toUpperCase();
  if(filter==="SHOW ALL"){
    let filter1="PENDING";
    let filter2="COMPLETED";
    for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[1];
      if (td) {
        txtValue = td.textContent || td.innerText;
        if ((txtValue.toUpperCase().indexOf(filter1) > -1) || (txtValue.toUpperCase().indexOf(filter2)>-1)) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }       
    }
  }
  else{
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[1];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }       
  }
 }
}
function getOption() {
  selectElement = document.querySelector('#select1');
  output = selectElement.value;
  myFunction(output);
}