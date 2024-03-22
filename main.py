from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['electricity_database']
collection = db['registrations']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    collection.insert_one(data)
    return jsonify({'message': 'Data inserted successfully'})

@app.route('/users')
def users():
    users = list(collection.find({}, {'_id': 0}))  # Exclude _id field from response
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
