from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    return ('Welcome to the Flask API!')


@app.route("/status")
def statu():
    return ("ok")


@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_users():
    if not request.json or "username" not in request.json:
        return jsonify({"error": "Username is required"}), 400

    username = request.json["username"]
    users[username] = {
        "username": username,
        "name": request.json.get("name", ""),
        "age": request.json.get("age", 0),
        "city": request.json.get("city", "")
    }

    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run(debug=True)
