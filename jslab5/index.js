// Авторизация
let users = [
    {
        login: "ramina",
        password: "1111",
        name: "Рамина"
    },
    {
        login: "radomir",
        password: "2121",
        name: "Радомир"
    },
    {
        login: "samina",
        password: "4352",
        name: "Самина"
    },
    {
        login: "rufina",
        password: "5783",
        name: "Руфина"
    },
    {
        login: "sezim",
        password: "4545",
        name: "Сезим"
    }
];

let login = document.querySelector("#login");
let password = document.querySelector("#password");
let loginButton = document.querySelector("#loginButton");
let message = document.querySelector("#message");

let authorization = () => {

    let userLogin = login.value;
    let userPassword = password.value;

    let user = users.find(user =>
        user.login === userLogin &&
        user.password === userPassword
    );

    if (user) {
        message.textContent = `Добро пожаловать, ${user.name}!`;
    } else {
        message.textContent = " Неверный логин или пароль!";
    }
};

loginButton.addEventListener("click", authorization);



// сумма чисел
let sumAll = (...numbers) => {

    let sum = 0;

    numbers.map(number => {
        sum = sum + number;
    });

    return sum;
};

let numbers = document.querySelector("#numbers");
let sumButton = document.querySelector("#sumButton");
let sumResult = document.querySelector("#sumResult");


let calculateSum = () => {

    let numbersArray = numbers.value.split(",").map(Number);

    let result = sumAll(...numbersArray);

    sumResult.textContent = `Сумма: ${result}`;
};

sumButton.addEventListener("click", calculateSum);