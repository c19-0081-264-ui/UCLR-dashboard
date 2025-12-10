document.addEventListener("DOMContentLoaded", function() {
            const randomNum = Math.floor(100000 + Math.random() * 900000);
            document.getElementById("Email").value = randomNum + "@school.edu.ph";
});

function togglePassword() {
            var passContainer = document.getElementById("password_container");
            if (passContainer.style.display === "none") {
                passContainer.style.display = "block";
            } else {
            passContainer.style.display = "none";
        }
    }