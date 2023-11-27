document.addEventListener('DOMContentLoaded', () => {
  const statusDetail = document.querySelector("#statusdetail");
  const submitButton = document.getElementById('submitButton');

  if (statusDetail && statusDetail.textContent === "In Progress") {
    submitButton.style.display = "flex";
  } else {
    submitButton.style.display = "none";
  }

  submitButton.addEventListener('click', async () => {
    if (statusDetail.textContent === "In Progress") {
      const confirmation = confirm('Do you want to submit?');

      if (confirmation) {
        // Redirect to Django view
        window.location.href = '/your-django-view-url';
      }
    }
  });
});
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

/*function submittask() {
  let text = "Press a OK for Submit task!";
  if (confirm(text) == true) {
    document.getElementById("statusdetail").textContent="Submitted for review";
    document.querySelector(".submit-container").style.display="none";
  } else {
  text = "You canceled!";
  }
}*/
function submittask(r) {
  let text = "Press OK to Submit the task for review!";
  let projectId = r.getAttribute('data-project-id');
  let taskId = r.getAttribute('data-task-id');

  if (confirm(text)) {
    // Make an AJAX request to update the task status
    fetch(`/dashboard/project/task-view/${projectId}/task-details/${taskId}/submit/`, {
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