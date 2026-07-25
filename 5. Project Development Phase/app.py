"""
Cosmetic Insights Web Application
Author: KADALI GEETHA SRAVYA
Project: Cosmetic Insights: Navigating Cosmetics Trends and Consumer Behavior with Tableau
"""

import os
import csv
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "cosmetics_clean.csv")

def load_data():
    products = []
    if not os.path.exists(DATA_PATH):
        return products
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['Price'] = float(row['Price']) if row['Price'] else 0.0
            row['Rank'] = float(row['Rank']) if row['Rank'] else 0.0
            row['Combination'] = int(row['Combination'])
            row['Dry'] = int(row['Dry'])
            row['Normal'] = int(row['Normal'])
            row['Oily'] = int(row['Oily'])
            row['Sensitive'] = int(row['Sensitive'])
            row['ALL_SKIN_TYPES_COUNT'] = int(row['ALL_SKIN_TYPES_COUNT'])
            products.append(row)
    return products

@app.route("/")
def index():
    return render_template("index.html", author="KADALI GEETHA SRAVYA", project_title="Cosmetic Insights: Navigating Cosmetics Trends and Consumer Behavior with Tableau")

@app.route("/api/stats")
def stats():
    data = load_data()
    total_products = len(data)
    total_brands = len(set(p['Brand'] for p in data))
    avg_price = round(sum(p['Price'] for p in data) / total_products, 2) if total_products > 0 else 0
    avg_rank = round(sum(p['Rank'] for p in data) / total_products, 2) if total_products > 0 else 0
    all_skin_products = sum(1 for p in data if p['ALL_SKIN_TYPES_COUNT'] == 5)
    
    categories = {}
    for p in data:
        cat = p['Label']
        categories[cat] = categories.get(cat, 0) + 1
        
    return jsonify({
        "total_products": total_products,
        "total_brands": total_brands,
        "avg_price": avg_price,
        "avg_rank": avg_rank,
        "all_skin_products": all_skin_products,
        "category_counts": categories
    })

@app.route("/api/products")
def products():
    data = load_data()
    category = request.args.get("category", "")
    skin_type = request.args.get("skin_type", "")
    max_price = request.args.get("max_price", type=float)
    
    filtered = data
    if category:
        filtered = [p for p in filtered if p['Label'].lower() == category.lower()]
    if skin_type:
        st_key = skin_type.capitalize()
        if st_key in ['Combination', 'Dry', 'Normal', 'Oily', 'Sensitive']:
            filtered = [p for p in filtered if p.get(st_key) == 1]
    if max_price:
        filtered = [p for p in filtered if p['Price'] <= max_price]
        
    return jsonify({
        "count": len(filtered),
        "products": filtered[:100]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
