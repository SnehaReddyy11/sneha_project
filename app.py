# app.py

from flask import Flask, render_template, url_for

app = Flask(__name__)

# app.py

@app.route('/')
def home():
    return render_template('home.html', products=products)

# app.py

@app.route('/product/<int:product_id>')
def product_details(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product is None:
        return "Product not found", 404
    return render_template('product_details.html', product=product)

# Product Model (Temporary - would be replaced by a database in production)
products = [
    {
        'id': 1,
        'name': 'Laptop',
        'description': 'A powerful laptop with 16GB RAM and 512GB SSD.',
        'price': 999.99,
        'image': 'laptop.jpg',
        'stock': 10
    },
    {
        'id': 2,
        'name': 'Smartphone',
        'description': 'A sleek smartphone with an excellent camera.',
        'price': 499.99,
        'image': 'smartphone.jpg',
        'stock': 25
    },
    {
        'id': 3,
        'name': 'Headphones',
        'description': 'Noise-cancelling over-ear headphones.',
        'price': 199.99,
        'image': 'headphones.jpg',
        'stock': 15
    }
]


if __name__ == '__main__':
    app.run(debug=True)

