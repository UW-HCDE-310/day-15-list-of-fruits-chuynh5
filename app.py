from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
    fruits = [
        {"name": "apples", "quantity": 3},
            {"name": "oranges", "quantity": 2},
            {"name": "strawberries", "quantity": 6}
    ]

    new_fruits = [fruit for fruit in fruits if 'o' in fruit['name'].lower() and fruit['quantity'] < 3]

    return render_template("index.html", fruits=new_fruits)