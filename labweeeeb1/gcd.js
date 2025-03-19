// Функція знаходження НСД (загальна для всіх)
function gcd(a, b) {
    while (b !== 0) {
        let temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

// Функція для обробки введення користувача
function findGCD() {
    let num1 = parseInt(document.getElementById("num1").value);
    let num2 = parseInt(document.getElementById("num2").value);

    if (!isNaN(num1) && !isNaN(num2) && num1 > 0 && num2 > 0) {
        document.getElementById("gcdResult").textContent = "НСД: " + gcd(num1, num2);
    } else {
        document.getElementById("gcdResult").textContent = "Будь ласка, введіть натуральні числа.";
    }
}
