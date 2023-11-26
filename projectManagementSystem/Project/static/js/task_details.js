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