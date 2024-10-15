#!/usr/bin/python3
from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, JWTManager
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password1"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password2"), "role": "admin"}
}


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if "username" not in data or "password" not in data:
        return jsonify({"error": "Username and password required"}), 400

    username = data["username"]
    password = data["password"]

    if username not in users or not check_password_hash(users[username]["password"], password):
        return jsonify({"error": "Invalid username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return jsonify({"message": "Basic Auth: Access Granted"})


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    current_user = get_jwt_identity()
    return jsonify(message="JWT Auth: Access Granted", user=current_user)


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if users[current_user]["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    else:
        return jsonify(message="Admin Access: Granted")


if __name__ == "__main__":
    app.run(debug=True)
