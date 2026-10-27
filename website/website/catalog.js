const DATA_URL = 'data.json';

const productGrid = document.getElementById('product-grid');
const detailSection = document.getElementById('detail-section');
const detailCard = document.getElementById('detail-card');
const closeBtn = document.getElementById('close-btn');

let productsData = [];

async function loadProducts() {
    try {
        const response = await fetch(DATA_URL);

        if (!response.ok) {
            throw new Error('Ошибка загрузки JSON');
        }

        productsData = await response.json();
        renderProductsList(productsData);

    } catch (error) {
        console.error('Ошибка JSON:', error);
        productGrid.innerHTML = '<p>Не удалось загрузить товары.</p>';
    }
}

function renderProductsList(products) {
    productGrid.innerHTML = '';

    products.forEach(product => {
        const card = document.createElement('article');

        card.className = 'product';

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
        `;

        card.addEventListener('click', function(event) {
            if (event.target.closest('.add-to-cart')) {
                return;
            }

            event.preventDefault();
            showProductDetail(product.id);
        });

        productGrid.appendChild(card);
    });
}

function showProductDetail(productId) {
    const product = productsData.find(p => p.id === productId);

    if (!product) {
        return;
    }

    const specsList = Object.entries(product.specs)
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

closeBtn.addEventListener('click', function() {
    detailSection.classList.add('hidden');
});

detailSection.addEventListener('click', function(event) {
    if (event.target === detailSection) {
        detailSection.classList.add('hidden');
    }
});

loadProducts();