from flask import Flask, request
from db import GroceryDB

app = Flask(__name__)
db = GroceryDB()

@app.route('/')
def home_page():
    return "Assalomu aleykum. Sizga bu server, kerakli oziq - ovqat mahsulotlarini chiqarib beradi.Siz buning uchun so'rov yuborishingiz talab etiladi. "

@app.route('/grocery')
def all_grocery():
    return db.grocery_all()

@app.route('/grocery/add', methods = ["POST"])
def add_grocery():
    if request.method == "POST":
        data = request.get_json()
        db.grocery_add(data)
        return data

@app.route('/grocery/type/<type>')
def all_grocery_by_type(type: str):
    return db.get_by_type(type=type)

@app.route('/grocery/name/<name>')
def all_grocery_by_name(name: str):
    return db.get_by_name(name=name)

@app.route('/grocery/price/<float:price>')
def all_grocery_by_price(price: float):
    return db.get_by_price(price=price)

@app.route('/grocery/quantity/<int:quantity>')
def all_grocery_by_quantity(quantity: int):
    return db.get_by_quantity(quantity=quantity)

if __name__=="__main__":
    app.run(debug=True)