# 代码生成时间: 2025-10-23 17:41:43
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Game Resource Manager using the Bottle framework.
This application allows to manage game resources through a web interface.
"""

from bottle import Bottle, request, run, template, redirect
import json

# Initialize the Bottle application
app = Bottle()

# In-memory resource storage (for simplicity; in production, use a database)
resources = {}

# Home page route
@app.route('/')
def home():
    return template('index', resources=resources)

# Route to create a new resource
@app.route('/resource', method='POST')
def create_resource():
    """Create a new game resource."""
    data = request.json
    if not data:
        return {'error': 'No data provided'}, 400
    if 'name' not in data or 'type' not in data:
        return {'error': 'Name and type are required'}, 400
    if data['name'] in resources:
        return {'error': 'Resource with the same name already exists'}, 409
    resources[data['name']] = data['type']
    return {'message': 'Resource created successfully'}, 201

# Route to retrieve a resource by name
@app.route('/resource/<name>')
def get_resource(name):
    """Get a game resource by its name."""
    resource = resources.get(name)
    if not resource:
        return {'error': 'Resource not found'}, 404
    return {'name': name, 'type': resource}

# Route to update an existing resource
@app.route('/resource/<name>', method='PUT')
def update_resource(name):
    """Update an existing game resource."""
    if name not in resources:
        return {'error': 'Resource not found'}, 404
    data = request.json
    if not data or 'type' not in data:
        return {'error': 'Type is required'}, 400
    resources[name] = data['type']
    return {'message': 'Resource updated successfully'}, 200

# Route to delete a resource
@app.route('/resource/<name>', method='DELETE')
def delete_resource(name):
    """Delete a game resource."""
    if name not in resources:
        return {'error': 'Resource not found'}, 404
    del resources[name]
    return {'message': 'Resource deleted successfully'}, 200

# Start the server if this file is executed directly
if __name__ == '__main__':
    run(app, host='localhost', port=8080)
