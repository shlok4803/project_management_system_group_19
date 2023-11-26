function deleteRow(r) {
    //let projectId = r.getAttribute('data-project-id');
    let text = "Press OK to delete the project!";
    if (confirm(text)) {
      // AJAX request
      fetch(`/dashboard/manage-employees/delete`, {
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
