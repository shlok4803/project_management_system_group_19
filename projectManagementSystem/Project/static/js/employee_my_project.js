let menuicn = document.querySelector(".menuicn");
let nav = document.querySelector(".navcontainer");

menuicn.addEventListener("click", () => {
    nav.classList.toggle("navclose");
})

function myFunction(filter) {
  var table, tr, td, i, txtValue;
  // input = document.getElementById("myInput");
  // filter = input.value.toUpperCase();
  if(filter=="I"){
    filter="Pending";
  }
  if(filter=="C"){
    filter="Completed";
  }
  if(filter=="S"){
    filter="Submitted for review";
  }
  filter=filter.toUpperCase();
  if(filter=="SHOW ALL" || filter=='#'){
    filter="";
  }
  table = document.querySelector(".main-table");
  tr = table.getElementsByTagName("tr");
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
function getOption() {
  selectElement = document.querySelector('#select1');
  output = selectElement.value;
  myFunction(output);
}