from flask import Flask, request, jsonify

app = Flask(_name_)

# Store for orders
orders = []

@app.route('/place_order', methods=['POST'])
def place_order():
    order = request.json
    orders.append(order)
    return jsonify({"message": "Order placed successfully!"}), 200

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders), 200

if _name_ == '_main_':
    app.run(debug=True)