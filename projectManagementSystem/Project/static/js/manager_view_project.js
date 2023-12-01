function deleteRow(r) {
  let taskId = r.getAttribute('data-task-id');
  let projectId = r.getAttribute('data-project-id');
  let text = "Press OK to delete the task!";
  if (confirm(text)) {
      // AJAX request
      fetch(`/dashboard/project/task-view/${projectId}/${taskId}/delete`, {
          method: 'DELETE',
          headers: {
              'X-CSRFToken': getCSRFToken()  // Ensure you have a function to retrieve the CSRF token
          },
      })
      .then(response => {
          if (response.ok) {
              // Handle success: remove row from the table
              let row = r.parentNode.parentNode;
              row.parentNode.removeChild(row);
              window.location.href = `/dashboard/project/task-view/${projectId}`;
          } else {
              // Handle error
              console.error('Error deleting task');
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
  
function accepttask(r) {
  let text = "Press OK to accept the task for review!";
  let projectId = r.getAttribute('data-project-id');
  let taskId = r.getAttribute('data-task-id');

  if (confirm(text)) {
    // Make an AJAX request to update the task status
    fetch(`/dashboard/project/task-view/${projectId}/task-details/${taskId}/accept`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCSRFToken()  // Ensure you have a function to retrieve the CSRF token
      },
      //body: JSON.stringify({ task_id: 'YOUR_TASK_ID', new_status: 'Submitted for review' }) // Send the task ID and new status
    })
    .then(response => {
      if (response.ok) {
        // Handle success: hide the submit button
        window.location.reload();
        document.querySelector(".submit-container").style.display = "none";
        
      } else {
        // Handle error
        console.error('Error submitting task');
      }
    })
    .catch(error => {
      console.error('Error:', error);
    });
  } else {
    text = "You canceled!";
  }
}
function declinetask(r) {
  let text = "Press OK to decline the task for review!";
  let projectId = r.getAttribute('data-project-id');
  let taskId = r.getAttribute('data-task-id');

  if (confirm(text)) {
    // Make an AJAX request to update the task status
    fetch(`/dashboard/project/task-view/${projectId}/task-details/${taskId}/decline`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCSRFToken()  // Ensure you have a function to retrieve the CSRF token
      },
      //body: JSON.stringify({ task_id: 'YOUR_TASK_ID', new_status: 'Submitted for review' }) // Send the task ID and new status
    })
    .then(response => {
      if (response.ok) {
        // Handle success: hide the submit button
        window.location.reload();
        document.querySelector(".submit-container").style.display = "none";
        
      } else {
        // Handle error
        console.error('Error submitting task');
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
  const cookieString = document.cookie;
  const csrfToken = cookieString
    .split(';')
    .find(cookie => cookie.trim().startsWith('csrftoken='));

  if (csrfToken) {
    return csrfToken.split('=')[1];
  } else {
    return null;
  }
}
function myFunction(filter) {
  var table, tr, td, i, txtValue;
  // input = document.getElementById("myInput");
  // filter = input.value.toUpperCase();
  table = document.querySelector(".main-table");
  tr = table.getElementsByTagName("tr");
  if(filter==="I"){
    filter="In Progress";
  }
  if(filter==="C"){
    filter="Completed";
  }
  if(filter==="R"){
    filter="Submitted for review";
  }
  filter=filter.toUpperCase();
  console.log(filter);
  if(filter==="SHOW ALL"){
    let filter1="IN PROGRESS";
    let filter2="COMPLETED";
    // console.log(filter1);
    let filter3="SUBMITTED FOR REVIEW";
    for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[1];
      if (td) {
        txtValue = td.textContent || td.innerText;
        if ((txtValue.toUpperCase().indexOf(filter1) > -1) || (txtValue.toUpperCase().indexOf(filter2)>-1))  {
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
  // console.log(output);
  myFunction(output);
}

