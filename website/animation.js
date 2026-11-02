let cards = document.querySelectorAll(
    '.product, .category, .info-card, .image-animation'
);

cards.forEach(function(card) {

    card.addEventListener('mouseenter', function() {
        card.style.transform = 'scale(1.03)';
        card.style.transition = 'transform 0.3s';
    });

    card.addEventListener('mouseleave', function() {
        card.style.transform = 'scale(1)';
    });

});

function showMessage() {

    let message = document.createElement('div');

    message.textContent = '♡ Товар добавлен в корзину!';

    message.classList.add('animation-message');

    document.body.appendChild(message);

    setTimeout(function() {
        message.remove();
    }, 2000);
}

document.addEventListener('click', function(event) {

    if (event.target.closest('.add-to-cart')) {
        showMessage();
    }

});

let elements = document.querySelectorAll(
    '.banner, .page-intro, .section, .split, .info-grid'
);

elements.forEach(function(element) {
    element.style.opacity = '0';
    element.style.transform = 'translateY(30px)';
    element.style.transition = 'opacity 0.7s, transform 0.7s';
});

function showElements() {

    elements.forEach(function(element) {

        let position = element.getBoundingClientRect().top;

        if (position < window.innerHeight - 80) {
            element.style.opacity = '1';
            element.style.transform = 'translateY(0)';
        }

    });

}

window.addEventListener('scroll', showElements);

showElements();
