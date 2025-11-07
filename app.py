from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

MONGO_URL = os.environ.get("MONGO_URL", "mongodb://mongo:27017/devopsdb")
client = MongoClient(MONGO_URL)
db = client.devopsdb
users_collection = db.users

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/api/users', methods=['GET'])
def get_users():
    users = list(users_collection.find({}, {"_id": 0, "name": 1}))
    return jsonify(users)

@app.route('/api/users', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": "Name is required"}), 400
    users_collection.insert_one({"name": data['name']})
    return jsonify({"message": "User added"}), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

