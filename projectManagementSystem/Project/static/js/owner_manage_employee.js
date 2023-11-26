function deleteRow(r) {
  let i = r.parentNode.parentNode.rowIndex;
  let email = r.getAttribute('data-email');
  let text = "Press OK to delete the user! Note corresponding projects and tasks will also be deleted";
  
  if (confirm(text)) {
      // AJAX request
      fetch(`/dashboard/manage-employees/delete/?email=${email}`, {
          method: 'DELETE',
          headers: {
            'X-CSRFToken': getCSRFToken()  // Ensure you have a function to retrieve the CSRF token
        },
          body: JSON.stringify({ email: email }) // Pass the user's email for identification
      })
      .then(response => {
          if (response.ok) {
              // Handle success: redirect or display a message
              window.location.reload(); // Refresh the page after successful deletion
          } else {
              // Handle error
              console.error('Error deleting user');
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

function changeRole(r) {
  let email = r.getAttribute('data-email');
  let text = "Press OK to change the role of user! Note corresponding projects and tasks will also be deleted";

  if (confirm(text)) {
      fetch(`/dashboard/manage-employees/change-role/?email=${email}`, {
          method: 'POST',
          headers: {
              'X-CSRFToken': getCSRFToken()
          },
          body: JSON.stringify({ email: email }) // Sending only email for identification
      })
      .then(response => {
          if (response.ok) {
              // Handle success: Display a message or perform additional actions
              console.log('Role changed successfully');
              // Optionally reload the page after a delay or conditionally
              window.location.reload();
          } else {
              // Handle error
              console.error('Error changing role of user');
          }
      })
      .catch(error => {
          console.error('Error:', error);
      });
  } else {
      console.log("Role change canceled!");
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
