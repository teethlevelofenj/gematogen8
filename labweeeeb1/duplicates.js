function countDuplicates() {
    let input = document.getElementById("numbersInput").value;
    let numbers = input.split(" ").map(Number);
    let counts = {};

    numbers.forEach(num => {
        if (counts[num] === undefined) {
            counts[num] = 0;
        }
        counts[num] += 1;
    });

    let result = Object.entries(counts)
        .map(([num, count]) => `${num} зустрічається ${count} раз(и)`).join("<br>");

    document.getElementById("duplicatesResult").innerHTML = result || "Будь ласка, введіть числа.";
}