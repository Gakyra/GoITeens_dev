function updateClock() {
    fetch('/ajax_demo/get-time/')
        .then(response => response.json())
        .then(data => {
            document.getElementById('clock').textContent = data.time;
        });
}

setInterval(updateClock, 1000);
updateClock();
