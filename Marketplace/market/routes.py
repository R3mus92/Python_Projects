from market import app
from flask import render_template
from market.models import Item

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route("/products")
def products():
    items = Item.query.all()
    return render_template('products.html', items=items)

if __name__ == "__main__":
    app.run()

