const DATA_URL = 'data.json';
const API_URL = 'https://jsonplaceholder.typicode.com/posts';

const productGrid = document.getElementById('product-grid');
const detailSection = document.getElementById('detail-section');
const detailCard = document.getElementById('detail-card');
const closeBtn = document.getElementById('close-btn');

const productForm = document.getElementById('productForm');
const productIdInput = document.getElementById('productId');
const productNameInput = document.getElementById('productName');
const productPriceInput = document.getElementById('productPrice');
const productCategoryInput = document.getElementById('productCategory');
const productImageInput = document.getElementById('productImage');
const productDescriptionInput = document.getElementById('productDescription');
const submitBtn = document.getElementById('submitBtn');
const cancelBtn = document.getElementById('cancelBtn');

let productsData = [];

// READ - загрузка товаров из data.json
async function loadProducts() {
    try {
        const response = await fetch(DATA_URL);

        if (!response.ok) {
            throw new Error('Ошибка загрузки товаров');
        }

        const data = await response.json();

        productsData = data.products;

        renderProductsList(productsData);

    } catch (error) {
        console.error(error);
    }
}

// Отображение товаров
function renderProductsList(products) {
    productGrid.innerHTML = '';

    products.forEach(product => {
        const card = document.createElement('article');

        card.className = 'product';
        card.dataset.id = product.id;

        card.innerHTML = `
            <img src="${product.image}" alt="${product.name}">

            <p class="tag">${product.category}</p>

            <h3>${product.name}</h3>

            <p class="price">
                ${product.price.toLocaleString('ru-RU')} сом
            </p>

            <button class="button add-to-cart"
                data-id="${product.id}"
                data-name="${product.name}"
                data-price="${product.price}">
                В корзину
            </button>

            <a href="#" class="more">Подробнее</a>

            <div class="crud-buttons">
                <button type="button" data-action="edit" data-id="${product.id}">
                    Изменить
                </button>

                <button type="button" data-action="delete" data-id="${product.id}">
                    Удалить
                </button>
            </div>
        `;

        productGrid.appendChild(card);
    });
}

// Обработка кнопок товаров
productGrid.addEventListener('click', function(event) {
    const actionButton = event.target.closest('[data-action]');

    if (actionButton) {
        const productId = Number(actionButton.dataset.id);

        if (actionButton.dataset.action === 'edit') {
            editProduct(productId);
        }

        if (actionButton.dataset.action === 'delete') {
            deleteProduct(productId);
        }

        return;
    }

    if (event.target.closest('.add-to-cart')) {
        return;
    }

    const card = event.target.closest('.product');

    if (card) {
        event.preventDefault();
        showProductDetail(Number(card.dataset.id));
    }
});

// CREATE и UPDATE
productForm.addEventListener('submit', async function(event) {
    event.preventDefault();

    const productId = productIdInput.value;

    const product = {
        title: productNameInput.value,
        body: productDescriptionInput.value,
        userId: 1
    };

    try {
        let response;

        if (productId) {
            response = await fetch(`${API_URL}/${productId}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(product)
            });

        } else {
            response = await fetch(API_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(product)
            });
        }

        if (!response.ok) {
            throw new Error('Ошибка отправки данных');
        }

        const result = await response.json();

        console.log('Ответ сервера:', result);

        if (productId) {
            const index = productsData.findIndex(
                item => item.id === Number(productId)
            );

            if (index !== -1) {
                productsData[index].name = productNameInput.value;
                productsData[index].price = Number(productPriceInput.value);
                productsData[index].category = productCategoryInput.value;
                productsData[index].image = productImageInput.value;
                productsData[index].description = productDescriptionInput.value;
            }

        } else {
            productsData.push({
                id: Date.now(),
                name: productNameInput.value,
                price: Number(productPriceInput.value),
                category: productCategoryInput.value,
                image: productImageInput.value,
                description: productDescriptionInput.value,
                specs: {}
            });
        }

        renderProductsList(productsData);
        resetForm();

    } catch (error) {
        console.error(error);
    }
});

// UPDATE - заполнение формы
function editProduct(productId) {
    const product = productsData.find(p => p.id === productId);

    if (!product) {
        return;
    }

    productIdInput.value = product.id;
    productNameInput.value = product.name;
    productPriceInput.value = product.price;
    productCategoryInput.value = product.category;
    productImageInput.value = product.image;
    productDescriptionInput.value = product.description;

    submitBtn.textContent = 'Сохранить изменения';

    productForm.scrollIntoView({ behavior: 'smooth' });
}

// DELETE - удаление товара
async function deleteProduct(productId) {
    try {
        const response = await fetch(`${API_URL}/${productId}`, {
            method: 'DELETE'
        });

        if (!response.ok) {
            throw new Error('Ошибка удаления товара');
        }

        productsData = productsData.filter(p => p.id !== productId);

        renderProductsList(productsData);
        resetForm();

        detailSection.classList.add('hidden');

    } catch (error) {
        console.error(error);
    }
}

// Сброс формы
function resetForm() {
    productForm.reset();
    productIdInput.value = '';
    submitBtn.textContent = 'Добавить товар';
}

cancelBtn.addEventListener('click', resetForm);

// Подробная информация о товаре
function showProductDetail(productId) {
    const product = productsData.find(p => p.id === productId);

    if (!product) {
        return;
    }

    const specsList = Object.entries(product.specs || {})
        .map(([key, value]) =>
            `<li><strong>${key}:</strong> ${value}</li>`
        )
        .join('');

    detailCard.innerHTML = `
        <div class="detail-layout">

            <img src="${product.image}"
                alt="${product.name}"
                class="detail-img">

            <div class="detail-info">

                <p class="tag">${product.category}</p>

                <h2>${product.name}</h2>

                <p class="detail-desc">
                    ${product.description}
                </p>

                <h3>Характеристики</h3>

                <ul class="detail-specs">
                    ${specsList}
                </ul>

                <p class="product-price">
                    ${product.price.toLocaleString('ru-RU')} сом
                </p>

                <button class="button add-to-cart"
                    data-id="${product.id}"
                    data-name="${product.name}"
                    data-price="${product.price}">
                    В корзину
                </button>

            </div>
        </div>
    `;

    detailSection.classList.remove('hidden');
}

// Закрытие подробной информации
closeBtn.addEventListener('click', function() {
    detailSection.classList.add('hidden');
});

detailSection.addEventListener('click', function(event) {
    if (event.target === detailSection) {
        detailSection.classList.add('hidden');
    }
});

// Загрузка товаров при открытии страницы
loadProducts();
