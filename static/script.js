document.addEventListener("DOMContentLoaded", function () {

    console.log("Titanic Survival Prediction System Loaded");

    const form = document.querySelector("form");
    const button = document.querySelector(".predict-btn");

    if (form && button) {
        form.addEventListener("submit", function () {
            button.innerHTML = "⏳ Predicting...";
            button.disabled = true;
        });
    }

});