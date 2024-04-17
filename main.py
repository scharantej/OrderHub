
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(80))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)

@app.route('/')
def index():
    orders = Order.query.all()
    return render_template('index.html', orders=orders)

@app.route('/order', methods=['POST'])
def create_order():
    product_name = request.form['product_name']
    quantity = request.form['quantity']
    price = request.form['price']
    order = Order(product_name=product_name, quantity=quantity, price=price)
    db.session.add(order)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/order/<int:order_id>', methods=['GET', 'PUT', 'DELETE'])
def order(order_id):
    order = Order.query.get_or_404(order_id)
    if request.method == 'GET':
        return render_template('order.html', order=order)
    elif request.method == 'PUT':
        product_name = request.form['product_name']
        quantity = request.form['quantity']
        price = request.form['price']
        order.product_name = product_name
        order.quantity = quantity
        order.price = price
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'DELETE':
        db.session.delete(order)
        db.session.commit()
        return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
