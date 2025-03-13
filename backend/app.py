from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection
db_config = {
    "host": "db",
    "user": "root",
    "password": "rootpassword",
    "database": "userdb"
}

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (data['username'], data['password']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "User signed up successfully!"})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (data['username'], data['password']))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    if user:
        return jsonify({"message": "Login successful!"})
    else:
        return jsonify({"message": "Invalid credentials!"}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
