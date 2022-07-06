from flask import Flask, render_template
from app import app
from models.orders import orders

@app.route('/orders')
def index():
    return render_template('index.html', orders=orders)




@app.route('/order/<order_number>')
def order(order_number):
    return render_template('order.html', order=orders[int(order_number)])




