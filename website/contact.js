
let form = document.getElementById('contact-form');
let result = document.getElementById('form-result');

let nameRegex = /^[А-ЯЁA-Z][а-яёa-z]+(?:[ -][А-ЯЁA-Z][а-яёa-z]+){1,2}$/;

let phoneRegex = /^(?:\+996|996|0)(?:312|50\d|55\d|70\d|75\d|77\d|99\d)\d{6}$/;

let emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

form.addEventListener('submit', function(event) {

    event.preventDefault();

    let name = document.getElementById('name').value.trim();
    let phone = document.getElementById('phone').value.trim();
    let email = document.getElementById('email').value.trim();

    let cleanPhone = phone.replace(/[\s()-]/g, '');

    if (!nameRegex.test(name)) {
        result.textContent =
            'Введите ФИО правильно!';
        result.style.color = 'red';

    } else if (!phoneRegex.test(cleanPhone)) {
        result.textContent =
            'Введите правильный номер Кыргызстана!';
        result.style.color = 'red';

    } else if (!emailRegex.test(email)) {
        result.textContent =
            'Введите правильный email!';
        result.style.color = 'red';

    } else {
        result.textContent =
            'Все данные введены правильно!';
        result.style.color = 'green';
    }

});
