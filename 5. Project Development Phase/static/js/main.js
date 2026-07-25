
document.addEventListener("DOMContentLoaded", () => {
    fetchStats();
    fetchProducts();

    document.getElementById("filter-btn").addEventListener("click", () => {
        const cat = document.getElementById("cat-select").value;
        const skin = document.getElementById("skin-select").value;
        fetchProducts(cat, skin);
    });
});

async function fetchStats() {
    try {
        const res = await fetch("/api/stats");
        const data = await res.json();
        document.getElementById("total-products").textContent = data.total_products.toLocaleString();
        document.getElementById("total-brands").textContent = data.total_brands;
        document.getElementById("avg-price").textContent = "$" + data.avg_price.toFixed(2);
        document.getElementById("all-skin-count").textContent = data.all_skin_products;
    } catch(e) {
        console.log("Stats fetch error", e);
    }
}

async function fetchProducts(category = "", skinType = "") {
    const tbody = document.getElementById("product-list");
    tbody.innerHTML = "<tr><td colspan='6'>Loading products...</td></tr>";
    
    try {
        const url = `/api/products?category=${encodeURIComponent(category)}&skin_type=${encodeURIComponent(skinType)}`;
        const res = await fetch(url);
        const data = await res.json();
        
        if(data.products.length === 0) {
            tbody.innerHTML = "<tr><td colspan='6'>No products match the selected criteria.</td></tr>";
            return;
        }

        tbody.innerHTML = data.products.map(p => `
            <tr>
                <td><span class="badge">${p.Label}</span></td>
                <td><strong>${p.Brand}</strong></td>
                <td>${p.Name}</td>
                <td>$${p.Price.toFixed(2)}</td>
                <td>⭐ ${p.Rank.toFixed(1)}</td>
                <td>${p.ALL_SKIN_TYPES_COUNT}/5</td>
            </tr>
        `).join("");
    } catch(e) {
        tbody.innerHTML = "<tr><td colspan='6'>Failed to load data. Please run backend server.</td></tr>";
    }
}
