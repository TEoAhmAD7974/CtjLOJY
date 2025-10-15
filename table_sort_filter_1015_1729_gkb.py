# 代码生成时间: 2025-10-15 17:29:47
#!/usr/bin/env python

# table_sort_filter.py - Bottle web application for sorting and filtering table data

from bottle import Bottle, request, run
import json

# Initialize Bottle app
app = Bottle()

# Dummy data for demonstration purposes
SAMPLE_DATA = [
    {'name': 'Alice', 'age': 30, 'city': 'New York'},
    {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'},
    {'name': 'Charlie', 'age': 35, 'city': 'Chicago'},
]

# Route for sorting and filtering data
@app.route('/filter_sort', method=['GET'])
def filter_sort():
    # Get query parameters
    sort_key = request.query.sort_key or 'name'
    sort_order = request.query.sort_order or 'asc'
    filter_key = request.query.filter_key or 'city'
    filter_value = request.query.filter_value

    # Validate and prepare the query parameters
    sort_key = str(sort_key)
    sort_order = sort_order.lower()
    filter_key = str(filter_key)

    # Define the sort function
    def sort_data(item):
        if sort_order == 'desc':
            return -1 * (item[sort_key] > item.get('name', 'z'))
        else:
            return item[sort_key] > item.get('name', 'z')

    # Filter the data based on the query parameters
    filtered_data = [
        item for item in SAMPLE_DATA 
        if item.get(filter_key) == filter_value
    ]

    # Sort the filtered data
    sorted_data = sorted(filtered_data, key=lambda x: x[sort_key], reverse=(sort_order == 'desc'))

    # Return the sorted and filtered data as JSON
    return json.dumps(sorted_data, indent=4)

# Run the Bottle app
run(app, host='localhost', port=8080, debug=True)
