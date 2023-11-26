function deleteRow(r) {
  let projectId = r.getAttribute('data-project-id');
  let text = "Press OK to delete the project!";
  if (confirm(text)) {
    // AJAX request
    fetch(`/dashboard/project/view-details/${projectId}/delete`, {
      method: 'DELETE',
      headers: {
        'X-CSRFToken': getCSRFToken()  // Ensure you have a function to retrieve the CSRF token
      },
    })
    .then(response => {
      if (response.ok) {
        // Handle success: redirect or display a message
        window.location.href = `/dashboard/project/`; // Redirect to project list or dashboard
      } else {
        // Handle error
        console.error('Error deleting project');
      }
    })
    .catch(error => {
      console.error('Error:', error);
    });
  } else {
    text = "You canceled!";
  }
}

function getCSRFToken() {
  const cookies = document.cookie.split(';');
  for (let cookie of cookies) {
      const [name, value] = cookie.trim().split('=');
      if (name === 'csrftoken') {
          return value;
      }
  }
  return null;
}
// const descbox2=document.querySelector(".description-box");

// function showtask2(row){
//   if(descbox2.style.display=="none"){
//       descbox2.style.display="flex";
//       document.querySelector(".tasktitle1").textContent=`Task ${row}`;
//       document.querySelector("#taskdetails").textContent="Hide Details";
//       document.querySelector(".desc-box").style.justifyContent="space-between";
//   }
//   else{
//       descbox2.style.display="none";
//       document.querySelector(".desc-box").style.justifyContent="center";
//       document.querySelector("#taskdetails").textContent="Task Details";
//   }
// }

// const descbox=document.querySelector(".details-container");

// var totalRowCount = 0;
// var rowCount = 0;
// var table = document.getElementById("maintable");
// var table = document.getElementById("maintable");
// var rows = table.getElementsByTagName("tr");

// for (var i = 0; i < rows.length; i++) {
//     totalRowCount++;
//     if (rows[i].getElementsByTagName("td").length > 0) {
//         rowCount++;
//     }
// }
// function showtask(row,btn){
//     // console.log(row);
//     descbox2.style.display="none";
//      if(btn.textContent=="View"){
//         document.querySelector(".desc-box").style.justifyContent="center";
//         document.querySelector("#taskdetails").textContent="Task Details";
//          descbox.style.display="flex";
//     for(let j=1;j<=rowCount;j++){
//             if(j==row)
//             continue;
//     const tablerow=document.getElementById(`tablerow${j}`);
//     const btn2=tablerow.querySelector(".button-tag");
//     btn2.textContent="View";
//     }
//     btn.textContent="Hide";
//     // console.log(btn);
// }

// else{
//     descbox.style.display="none";
//     btn.textContent="View";
// }
// }
// document.querySelector("#taskdetails").addEventListener('click',()=>{
//     for(let j=1;j<=rowCount;j++){
//         const tablerow=document.getElementById(`tablerow${j}`);
//         const btn2=tablerow.querySelector(".button-tag");
//         if(btn2.textContent=="Hide"){
//             showtask2(j);
//         }
//     }
// });
// document.querySelector("#deletebtn").addEventListener('click',()=>{
//     for(let j=1;j<=rowCount;j++){
//         const tablerow=document.getElementById(`tablerow${j}`);
//         const btn2=tablerow.querySelector(".button-tag");
//         if(btn2.textContent=="Hide"){
//             deleteRow(btn2);
//             descbox.style.display="none";
//             descbox2.style.display="none";

//         }
//     }
// });
//  for(let j=1;j<=rowCount;j++){
//     const tablerow=document.getElementById(`tablerow${j}`);
//     const btn2=tablerow.querySelector(".button-tag");
//     btn2.onclick=function() { console.log(tablerow); showtask(j,btn2);};
// }

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
  if(filter==="I"){
      filter="Pending";
  }
  if(filter==="C"){
      filter="Completed";
  }
  if(filter==="R"){
      filter="Submitted for review";
  }
  filter=filter.toUpperCase();
  if(filter==="SHOW ALL"){
    let filter1="PENDING";
    let filter2="COMPLETED";
    let filter3="SUBMITTED FOR REVIEW";
    for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[1];
      if (td) {
        txtValue = td.textContent || td.innerText;
        if ((txtValue.toUpperCase().indexOf(filter1) > -1) || (txtValue.toUpperCase().indexOf(filter2)>-1) || (txtValue.toUpperCase().indexOf(filter3)>-1)) {
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
  console.log(output);
  myFunction(output);
}