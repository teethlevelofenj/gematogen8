function countWords() {
    let text = document.getElementById("textInput").value.trim();
    let words = text.split(/\s+/).filter(word => word.length > 0);

    document.getElementById("wordCountResult").textContent = "Кількість слів: " + words.length;
}