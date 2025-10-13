# 代码生成时间: 2025-10-13 21:41:38
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Inventory Management System using Bottle framework.
"""

from bottle import Bottle, run, request, response, redirect
import json

# Initialize the Bottle application
app = Bottle()

# In-memory storage for simplicity, in a real-world scenario use a database
inventory = {}

# Home page - List all products
@app.route('/')
def list_products():
    return json.dumps(inventory, indent=4)

# Add a new product to the inventory
@app.route('/add', method='POST')
def add_product():
    try:
        product_data = request.json
        product_id = product_data.get('id')
        if not product_id:
            response.status = 400
            return json.dumps({'error': 'Product ID is required'})
        if product_id in inventory:
            response.status = 400
            return json.dumps({'error': 'Product already exists'})
        inventory[product_id] = product_data
        response.status = 201
        return json.dumps({'message': 'Product added successfully'})
    except Exception as e:
        response.status = 500
        return json.dumps({'error': str(e)})

# Update an existing product in the inventory
@app.route('/update/<product_id>', method='PUT')
def update_product(product_id):
    try:
        product_data = request.json
        if product_id not in inventory:
            response.status = 404
            return json.dumps({'error': 'Product not found'})
        inventory[product_id] = product_data
        return json.dumps({'message': 'Product updated successfully'})
    except Exception as e:
        response.status = 500
        return json.dumps({'error': str(e)})

# Delete a product from the inventory
@app.route('/delete/<product_id>', method='DELETE')
def delete_product(product_id):
    try:
        if product_id not in inventory:
            response.status = 404
            return json.dumps({'error': 'Product not found'})
        del inventory[product_id]
        return json.dumps({'message': 'Product deleted successfully'})
    except Exception as e:
        response.status = 500
        return json.dumps({'error': str(e)})

if __name__ == '__main__':
    run(app, host='localhost', port=8080)
