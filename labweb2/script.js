let modal = document.getElementById("myModal");
let span = document.getElementsByClassName("close")[0];

let products = [
    { image: 'img1_1.png', description: '+10 strg; +572 hp; +35 dmg;', tag: '1' },
    { image: 'img2_1.png', description: '20 strg; +100 hp; +60 dmg', tag: '1' },
    { image: 'img1_2.png', description: '+40 Strg +1.4% Max HP Health Regen', tag: '2' },
    { image: 'img2_2.png', description: '+10 Strg +24 S Dmg', tag: '2' },
    { image: 'img1_3.png', description: '12 Intelligence +1.5 Mana Regeneration +6 Armor +40 Attack Speed  +300 Projectile Speed', tag: '3' },
    { image: 'img2_3.png', description: '+30 Intelligence +8.5 Mana Regeneration', tag: '3' },
    { image: 'img1_4.png', description: '+55 Melee Move Speed +45 Ranged Move Speed +25 Attack Speed', tag: '4' },
    { image: 'img2_4.png', description: '+5 Strength +2 Agility +2 Intelligen +50 Health +0.75 Health Regeneration', tag: '4' },
];

function filterProductsByTag(tag) {
    let filtered = tag === 'all' ? products : products.filter(p => p.tag === tag);
    let container = document.getElementById('product-container');
    container.innerHTML = '';

    filtered.forEach(p => {
        let div = document.createElement('div');
        div.className = 'product-card';

        let img = document.createElement('img');
        img.src = p.image;

        let desc = document.createElement('p');
        desc.textContent = p.description;

        div.appendChild(img);
        div.appendChild(desc);
        container.appendChild(div);
    });
}

function showModal() {
    modal.style.display = "block";
}

span.onclick = function () {
    modal.style.display = "none";
}

window.onload = function () {
    filterProductsByTag('all');
    setTimeout(showModal, 10000); // показати модальне через 10 секунд
};
