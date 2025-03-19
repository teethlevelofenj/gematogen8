function convertTemperature() {
    let celsius = parseFloat(document.getElementById("celsiusInput").value);

    if (!isNaN(celsius)) {
        let kelvin = celsius + 273.15;
        document.getElementById("temperatureResult").textContent = "Температура в К: " + kelvin.toFixed(2);
    } else {
        document.getElementById("temperatureResult").textContent = "Будь ласка, введіть коректне число.";
    }
}