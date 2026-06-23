let seconds = 5;

let countdownEl = document.getElementById("countdown");

let interval = setInterval(function () {
    seconds--;
    countdownEl.innerText = seconds;

    if (seconds <= 0) {
        clearInterval(interval);
        window.location.href = "/user/login/";
    }
}, 1000);