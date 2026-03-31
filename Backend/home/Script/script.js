function updateTemperature() {
    fetch("/temperature")
        .then(response => response.json())
        .then(data => {
            const temp = data.temperature;
            const emoji = temp < 10 ? "❄️" : temp < 20 ? "🧥" : "☀️";

            document.getElementById("emoji").innerText = emoji;
            document.getElementById("temp").innerText = temp + "°C";
        })
        .catch(error => console.error("Error fetching temperature:", error));
}


// Fetch every 5 seconds automatically
setInterval(updateTemperature, 5000);

// Run immediately on page load
updateTemperature();