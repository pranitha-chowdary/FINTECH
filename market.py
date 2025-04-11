from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")#decorator
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route("/about/<username>")
def about_page(username):
    return f'<h1>This is {username}</h1>'

@app.route('/market')
def market_page():
    items = [
        {"id": 1, "name": "Ledger Nano X", "price": 149.99},
        {"id": 2, "name": "Trezor Model T", "price": 219.00},
        {"id": 3, "name": "Square Reader", "price": 49.00},
        {"id": 4, "name": "NFC Payment Ring", "price": 79.99}
    ]

    return render_template('market.html',items=items)
