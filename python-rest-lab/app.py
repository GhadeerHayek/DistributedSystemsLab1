from flask import Flask, jsonify, request
from models import User


app = Flask(__name__)
@app.route('/api/users', methods=['GET'])
def get_users():
# Return list of all users
    pass
@app.route('/api/users/<id>', methods=['GET'])
def get_user(id):
# Return specific user
    pass
@app.route('/api/users', methods=['POST'])
def create_user():
# Create new user from request data
    pass
@app.route('/api/users/<id>', methods=['PUT'])
def update_user(id):
# Update existing user
    pass
@app.route('/api/users/<id>', methods=['DELETE'])
def delete_user(id):
# Delete user
    pass

