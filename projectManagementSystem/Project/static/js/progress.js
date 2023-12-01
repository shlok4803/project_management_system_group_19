menuicn.addEventListener("click", () => {
    nav.classList.toggle("navclose");
})

document.addEventListener("DOMContentLoaded", function () {
    // Get the progress element
    var progressElement = document.querySelector(".progress");

    // Get the value of variable i
    var iValue = parseFloat(progressElement.style.getPropertyValue("--i"));

    // Check if iValue is less than 50
    if (iValue < 50) {
        // If less than 50, add the "less" class
        progressElement.classList.add("less");
    }
});