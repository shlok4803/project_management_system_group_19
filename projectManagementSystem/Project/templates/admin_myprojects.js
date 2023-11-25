let menuicn = document.querySelector(".menuicn");
let nav = document.querySelector(".navcontainer");

menuicn.addEventListener("click", () => {
    nav.classList.toggle("navclose");
})

document.querySelector(".statuscheck").addEventListener('click',()=>{
    if(document.querySelector(".statuscheck").textContent=="Submitted for review"){
        document.querySelector(".confirmation").style.display="flex";
    }
})
document.querySelector(".confirmation-btn1").addEventListener('click',()=>{
    document.querySelector(".statuscheck").textContent="Completed";
    document.querySelector(".confirmation").style.display="none";
});
document.querySelector(".confirmation-btn2").addEventListener('click',()=>{
    document.querySelector(".statuscheck").textContent="Inprogress";
    document.querySelector(".confirmation").style.display="none";
});


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
    if(filter=="Show all" || filter=="#"){
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
    console.log(output);
    myFunction(output);
}