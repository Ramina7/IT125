let form = document.getElementById('contact-form');
let result = document.getElementById('form-result');

let nameRegex = /^[A-ZА-ЯЁ][a-zа-яё]+ [A-ZА-ЯЁ][a-zа-яё]+$/;

let phoneRegex = /(\+996|996|0)(312|50\d|55\d|70\d|75\d|77\d|99\d)\d{6}/;

let emailRegex = /\w+@\w+\.\w+/;

form.addEventListener('submit', function(event) {
    event.preventDefault();

    let name = document.getElementById('name').value;
    let phone = document.getElementById('phone').value;
    let email = document.getElementById('email').value;

    if (!nameRegex.test(name)) {
        result.textContent = 'Введите имя и фамилию правильно!';
        result.style.color = 'red';

    } else if (!phoneRegex.test(phone)) {
        result.textContent = 'Введите правильный номер Кыргызстана!';
        result.style.color = 'red';

    } else if (!emailRegex.test(email)) {
        result.textContent = 'Введите правильный email!';

        result.style.color = 'red';

    } else {
        result.textContent = 'Все данные введены правильно!';
        result.style.color = 'green';
    }
});