**HTML Files**

- **index.html**: The main landing page of the application, providing an interface for the user to create and manage orders.
- **order.html**: A template for individual order details, accessible when the user clicks on an order from the index page.

**Routes**

- **@app.route('/')**: The index page, displays a list of orders.
- **@app.route('/order', methods=['POST'])**: Creates a new order, taking user-provided data from the index page.
- **@app.route('/order/<int:order_id>', methods=['GET', 'PUT', 'DELETE'])**:
  - GET: Displays the order details, accessible via the index page.
  - PUT: Updates the order details, taking user-provided data from the order page.
  - DELETE: Deletes the order, accessible via the order page.