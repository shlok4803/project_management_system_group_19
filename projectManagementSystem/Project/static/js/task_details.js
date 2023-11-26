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

function submittask() {
  let text = "Press a OK for Submit task!";
  if (confirm(text) == true) {
    document.getElementById("statusdetail").textContent="Submitted for review";
    document.querySelector(".submit-container").style.display="none";
  } else {
  text = "You canceled!";
  }
}