from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    bakery_name = "Delicious Bakery"
    bakery_description = "Welcome to Delicious Bakery, where we create delicious and mouthwatering treats to satisfy your cravings. We take pride in our passion for baking and use only the finest ingredients to craft a wide variety of delectable pastries, cakes, bread, and more."
    opening_hours = "7:00 AM - 6:00 PM"
    location_photo_link = "https://example.com/location-photo"

    return render_template('index.html',
                           bakery_name=bakery_name,
                           bakery_description=bakery_description,
                           opening_hours=opening_hours,
                           location_photo_link=location_photo_link)

@app.route('/products')
def product_list():
    products = [
        {'name': 'Product 1', 'description': 'Description of Product 1', 'price': 10.99},
        {'name': 'Product 2', 'description': 'Description of Product 2', 'price': 19.99},
        {'name': 'Product 3', 'description': 'Description of Product 3', 'price': 5.99}
    ]

    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
