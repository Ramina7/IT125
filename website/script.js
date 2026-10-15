
"use strict";

// Загружаем сохранённую корзину
let cart = JSON.parse(localStorage.getItem("lumeaCart")) || [];

// Сохраняем корзину в браузере
function saveCart() {
    localStorage.setItem("lumeaCart", JSON.stringify(cart));
}

// Показываем количество товаров в меню
function updateCartCount() {
    let count = 0;

    cart.forEach(function(item) {
        count = count + item.quantity;
    });

    let element = document.getElementById("cart-count");

    if (element) {
        element.textContent = count;
    }
}

// Добавляем товар
function addToCart(id, name, price) {
    let product = cart.find(function(item) {
        return item.id === id;
    });

    if (product) {
        product.quantity++;
    } else {
        cart.push({
            id: id,
            name: name,
            price: price,
            quantity: 1
        });
    }

    saveCart();
    updateCartCount();
    alert("Товар добавлен в корзину!");
}

// Кнопки добавления товара
document.querySelectorAll(".add-to-cart").forEach(function(button) {
    button.addEventListener("click", function() {
        addToCart(
            button.dataset.id,
            button.dataset.name,
            Number(button.dataset.price)
        );
    });
});

// Показываем содержимое корзины
function showCart() {
    let list = document.getElementById("cart-items");
    let totalElement = document.getElementById("cart-total");

    if (!list || !totalElement) return;

    list.innerHTML = "";
    let total = 0;

    if (cart.length === 0) {
        list.textContent = "Корзина пока пуста.";
        totalElement.textContent = "0";
        return;
    }

    cart.forEach(function(item) {
        total += item.price * item.quantity;

        let row = document.createElement("div");
        row.className = "cart-row";

        let info = document.createElement("div");
        let title = document.createElement("strong");
        title.textContent = item.name;

        let details = document.createElement("p");
        details.textContent =
            item.price + " сом × " + item.quantity;

        info.appendChild(title);
        info.appendChild(details);

        let removeButton = document.createElement("button");
        removeButton.textContent = "Удалить";

        removeButton.addEventListener("click", function() {
            cart = cart.filter(function(product) {
                return product.id !== item.id;
            });

            saveCart();
            updateCartCount();
            showCart();
        });

        row.appendChild(info);
        row.appendChild(removeButton);
        list.appendChild(row);
    });

    totalElement.textContent = total;
}

// Очистка корзины
let clearButton = document.getElementById("clear-cart");

if (clearButton) {
    clearButton.addEventListener("click", function() {
        cart = [];
        saveCart();
        updateCartCount();
        showCart();
    });
}

// Демонстрационное оформление заказа
let checkoutButton = document.getElementById("checkout");

if (checkoutButton) {
    checkoutButton.addEventListener("click", function() {
        if (cart.length === 0) {
            alert("Сначала добавьте товары в корзину.");
        } else {
            alert("Спасибо за выбор LUMÉA Beauty! Это учебный сайт, заказ не отправлен.");
        }
    });
}

// Поиск в каталоге
let search = document.getElementById("search");

if (search) {
    search.addEventListener("input", function() {
        let text = search.value.toLowerCase();
        let products = document.querySelectorAll(".product[data-name]");
        let found = 0;

        products.forEach(function(product) {
            let name = product.dataset.name.toLowerCase();

            if (name.includes(text)) {
                product.style.display = "";
                found++;
            } else {
                product.style.display = "none";
            }
        });

        let message = document.getElementById("no-results");

        if (message) {
            message.hidden = found > 0;
        }
    });
}

// Проверка контактной формы
let form = document.getElementById("contact-form");

if (form) {
    form.addEventListener("submit", function(event) {
        event.preventDefault();

        let name = document.getElementById("name").value.trim();
        let result = document.getElementById("form-result");

        result.textContent = "Спасибо, " + name + "! Форма заполнена успешно.";
        form.reset();
    });
}

// Запускаем функции при открытии страницы
updateCartCount();
showCart();

console.log("LUMÉA Beauty is working!");
