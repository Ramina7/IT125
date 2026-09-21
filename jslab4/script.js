// COUNTER

let count = 0;

let counter = document.getElementById("counter");

function updateCounter() {
    counter.textContent = count;

    if (count > 0) {
        counter.style.color = "green";
    } else if (count < 0) {
        counter.style.color = "red";
    } else {
        counter.style.color = "gray";
    }
}

function increase() {
    count++;
    updateCounter();
}

function decrease() {
    count--;
    updateCounter();
}

function resetCounter() {
    count = 0;
    updateCounter();
}


// ЛОТО

function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);

    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function generateNumbers() {
    let numbers = document.getElementById("numbers");

    numbers.innerHTML = "";

    for (let i = 0; i < 6; i++) {
        let number = getRandomInt(1, 99);

        let ball = document.createElement("div");

        ball.className = "ball";

        ball.textContent = String(number).padStart(2, "0");

        numbers.appendChild(ball);
    }
}