#!/usr/bin/python3
'''Flask'''
from flask import Flask, jsonify, request

app = Flask(__name__)
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}


@app.route('/')
def home():
    return 'Welcome to the Flask API!'


@app.route('/data')
def get_data():
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route('/status')
def get_status():
    return 'OK'


@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({'Error': 'User not found'}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    if data:
        username = data.get('username')
        if username:
            new_user = {
                "username": username,
                "name": data.get('name'),
                "age": data.get('age'),
                "city": data.get('city')
            }
            users[username] = new_user
            return jsonify({"message": "User added", "user": new_user}), 201
    return jsonify({"error": "Invalid data provided"}), 400


if __name__ == '__main__':
    app.run()
