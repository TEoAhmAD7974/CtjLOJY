# 代码生成时间: 2025-10-02 19:21:36
# test_case_manager.py

"""Test Case Manager using Python and Bottle Framework

This program allows the management of test cases.
It includes functionalities like adding, updating, deleting, and listing test cases."""

from bottle import route, run, request, response
from bottle.ext import sqlalchemy
import json
import sqlite3

# Database configuration
DATABASE_URI = 'sqlite:///test_cases.db'

# Set up Bottle app with SQLAlchemy
app = sqlalchemy.BottlePlugin(engine)(app)

# Test case model
class TestCase(db.Model):
    __tablename__ = 'test_cases'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(128), nullable=False)

    def __init__(self, name, description, status):
        self.name = name
        self.description = description
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "status": self.status
        }

# Initialize database tables
db.create_all()

# Route to list all test cases
@route('/test-cases', method='GET')
def list_test_cases():
    try:
        test_cases = TestCase.query.all()
        test_cases_list = [test_case.to_dict() for test_case in test_cases]
        return json.dumps(test_cases_list)
    except Exception as e:
        response.status = 500
        return json.dumps({"error": str(e)})

# Route to add a new test case
@route('/test-cases', method='POST')
def add_test_case():
    try:
        data = request.json
        new_test_case = TestCase(name=data['name'], description=data['description'], status=data['status'])
        db.session.add(new_test_case)
        db.session.commit()
        return json.dumps(new_test_case.to_dict()), 201
    except Exception as e:
        response.status = 400
        return json.dumps({"error": str(e)})

# Route to get a single test case
@route('/test-cases/<id:int>', method='GET')
def get_test_case(id):
    try:
        test_case = TestCase.query.get(id)
        if test_case:
            return json.dumps(test_case.to_dict())
        else:
            response.status = 404
            return json.dumps({"error": "Test case not found"})
    except Exception as e:
        response.status = 500
        return json.dumps({"error": str(e)})

# Route to update a test case
@route('/test-cases/<id:int>', method='PUT')
def update_test_case(id):
    try:
        data = request.json
        test_case = TestCase.query.get(id)
        if test_case:
            test_case.name = data.get('name', test_case.name)
            test_case.description = data.get('description', test_case.description)
            test_case.status = data.get('status', test_case.status)
            db.session.commit()
            return json.dumps(test_case.to_dict())
        else:
            response.status = 404
            return json.dumps({"error": "Test case not found"})
    except Exception as e:
        response.status = 400
        return json.dumps({"error": str(e)})

# Route to delete a test case
@route('/test-cases/<id:int>', method='DELETE')
def delete_test_case(id):
    try:
        test_case = TestCase.query.get(id)
        if test_case:
            db.session.delete(test_case)
            db.session.commit()
            return json.dumps({"message": "Test case deleted"})
        else:
            response.status = 404
            return json.dumps({"error": "Test case not found"})
    except Exception as e:
        response.status = 500
        return json.dumps({"error": str(e)})

# Run the application
run(app, host='localhost', port=8080)