document.addEventListener('DOMContentLoaded', function() {
    const statusDetail = document.querySelector("#statusdetail");
    const statusChanger = document.querySelector(".statuschanger");

    statusChanger.addEventListener('click', () => {
        const currentStatus = statusDetail.textContent.trim();
        if (currentStatus === "Pending") {
            document.querySelector(".confirmation").style.display = "flex";
        }
    });

    document.querySelector(".confirmation-btn1").addEventListener('click', () => {
        const currentStatus = statusDetail.textContent.trim();
        if (currentStatus === "Pending") {
            const projectId = statusChanger.getAttribute('data-project-id');
            fetch(`/dashboard/project/view-details/${projectId}/update-status`)
                .then(response => response.json())
                .then(data => {
                    if (data.message === 'Project completed successfully') {
                        statusDetail.textContent = "Completed";
                        statusChanger.style.display = "none";
                    } else {
                        console.log("Tasks are pending");
                        // Display a message indicating tasks are pending
                    }
                    document.querySelector(".confirmation").style.display = "none";
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        }
    });

    document.querySelector(".confirmation-btn2").addEventListener('click', () => {
        document.querySelector(".confirmation").style.display = "none";
    });
});
