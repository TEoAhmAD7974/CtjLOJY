# 代码生成时间: 2025-10-06 22:34:50
# marketing_campaign_manager.py

# Bottle is a fast and simple WSGI micro web-framework for Python.
# It is distributed under the MIT license.
from bottle import route, run, request, response, HTTPResponse
from json import dumps

# Define a dictionary to store campaigns
campaigns = {}

# Define a route to create a new marketing campaign
@route('/campaigns', method='POST')
def create_campaign():
    try:
        # Get the JSON data from the request body
        data = request.json
        # Validate the data
        if 'name' not in data or 'description' not in data:
            response.status = 400
            return {'error': 'Missing campaign name or description'}
        # Create a new campaign with a unique ID
        campaign_id = len(campaigns) + 1
        campaigns[campaign_id] = data
        # Return the created campaign data
        response.status = 201
        return {'id': campaign_id, 'name': data['name'], 'description': data['description']}
    except Exception as e:
        # Handle any unexpected errors
        response.status = 500
        return {'error': 'Internal Server Error', 'details': str(e)}

# Define a route to get all campaigns
@route('/campaigns', method='GET')
def get_campaigns():
    try:
        # Return all campaigns as a JSON list
        return dumps(list(campaigns.values()))
    except Exception as e:
        # Handle any unexpected errors
        response.status = 500
        return {'error': 'Internal Server Error', 'details': str(e)}

# Define a route to get a specific campaign
@route('/campaigns/<id:int>', method='GET')
def get_campaign(id):
    try:
        # Check if the campaign exists
        if id in campaigns:
            # Return the specific campaign data
            return dumps(campaigns[id])
        else:
            # Return an error if the campaign does not exist
            response.status = 404
            return {'error': 'Campaign not found'}
    except Exception as e:
        # Handle any unexpected errors
        response.status = 500
        return {'error': 'Internal Server Error', 'details': str(e)}

# Define a route to update a specific campaign
@route('/campaigns/<id:int>', method='PUT')
def update_campaign(id):
    try:
        # Get the JSON data from the request body
        data = request.json
        # Check if the campaign exists
        if id in campaigns:
            # Update the campaign with new data
            campaigns[id].update(data)
            # Return the updated campaign data
            return dumps(campaigns[id])
        else:
            # Return an error if the campaign does not exist
            response.status = 404
            return {'error': 'Campaign not found'}
    except Exception as e:
        # Handle any unexpected errors
        response.status = 500
        return {'error': 'Internal Server Error', 'details': str(e)}

# Define a route to delete a specific campaign
@route('/campaigns/<id:int>', method='DELETE')
def delete_campaign(id):
    try:
        # Check if the campaign exists
        if id in campaigns:
            # Delete the campaign
            del campaigns[id]
            # Return a success message
            response.status = 200
            return {'message': 'Campaign deleted successfully'}
        else:
            # Return an error if the campaign does not exist
            response.status = 404
            return {'error': 'Campaign not found'}
    except Exception as e:
        # Handle any unexpected errors
        response.status = 500
        return {'error': 'Internal Server Error', 'details': str(e)}

# Run the Bottle application on port 8080
run(host='localhost', port=8080)