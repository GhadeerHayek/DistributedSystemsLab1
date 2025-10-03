from flask import Flask, jsonify, request
from models import User
import uuid

app = Flask(__name__)

# users is a dict of dictionaries, each representing a user
users = {}


@app.route('/api/users', methods=['GET'])
def get_users():
    # Returns a list of all users
    return jsonify([user.to_dict() for user in users.values()])


@app.route('/api/users/<id>', methods=['GET'])
def get_user(id):
    # Returns a specific user
    # the id is key, so just get its corresponding value
    user = users.get(id)
    print("user:", user)
    return (jsonify({'error': 'User not found'}), 404) if not user else jsonify(user.to_dict())


@app.route('/api/users', methods=['POST'])
def create_user():
    # Create new user from request data
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({'error': 'Missing name or email'}), 400
    user = User(str(uuid.uuid4()), data['name'], data['email'])
    users[user.id] = user
    return jsonify(user.to_dict()), 201


@app.route('/api/users/<id>', methods=['PUT'])
def update_user(id):
    # Update existing user
    if id not in users:
        return jsonify({'error': 'User not found'}), 404
    data = request.get_json()
    user = users[id]
    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    return jsonify(user.to_dict())


@app.route('/api/users/<id>', methods=['DELETE'])
def delete_user(id):
    # Delete user
    if id not in users:
        return jsonify({'error': 'User not found'}), 404
    del users[id]
    return jsonify({'message': 'User deleted'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
