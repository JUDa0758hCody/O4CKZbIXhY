# 代码生成时间: 2025-09-18 01:31:13
import gr
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Define a simple user database for demonstration purposes
USER_DB = {
    "user1": "password1",
    "user2": "password2"
}

# Define a function to authenticate users
def authenticate(username, password):
    """
    Check if the username and password match the user database.
    """
    if username in USER_DB and USER_DB[username] == password:
        return True
    else:
        return False

# Define the login endpoint
@app.route("/login", methods=["POST"])
def login():
    """
    Handle login requests. Expects a JSON payload with 'username' and 'password'.
    """
    data = request.get_json()
    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Missing credentials"}), 400

    username = data["username"]
    password = data["password"]
    if authenticate(username, password):
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

# Define a protected endpoint that requires authentication
@app.route("/protected")
def protected():
    """
    Protect this endpoint and require authentication to access it.
    """
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return jsonify({"error": "Missing Authorization header"}), 401

    # For simplicity, assume the Authorization header is the username
    # In a real-world scenario, you would use a token (e.g., JWT)
    username = auth_header
    if username in USER_DB:
        return jsonify({"message": "Access granted"}), 200
    else:
        return jsonify({"error": "Unauthorized access"}), 403

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
