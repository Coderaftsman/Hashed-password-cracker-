from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import hashlib

app = Flask(__name__)
CORS(app)  # Allow frontend and backend to communicate

# Sample wordlist for dictionary attack
WORDLIST = ["password", "123456", "qwerty", "letmein", "welcome", "admin", "kutty"]


# Function to attempt cracking the hash
def crack_hash(hash_value, hash_type):
    try:
        hash_function = getattr(hashlib, hash_type, None)
        if not hash_function:
            return "Unsupported hash type"

        for word in WORDLIST:
            if hash_function(word.encode()).hexdigest() == hash_value:
                return word  # Found matching password

        return "Password not found in wordlist"
    except Exception as e:
        return str(e)

@app.route("/")
def index():
    return render_template("index.html")  # Load the frontend

@app.route("/crack", methods=["POST"])
def crack():
    data = request.get_json()
    hash_value = data.get("hash_value")
    hash_type = data.get("hash_type")

    if not hash_value or not hash_type:
        return jsonify({"error": "Missing required fields"}), 400

    password = crack_hash(hash_value, hash_type)
    return jsonify({"password": password})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
