from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = 'books.json'

# Load data from JSON file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

# Save data to JSON file
def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# Initialize data
books = load_data()

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<isbn>', methods=['GET'])
def get_book(isbn):
    book = next((book for book in books if book['isbn'] == isbn), None)
    if book:
        return jsonify(book)
    return jsonify({'error': 'Book not found'}), 404

@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    if any(book['isbn'] == new_book['isbn'] for book in books):
        return jsonify({'error': 'Book already exists'}), 400
    books.append(new_book)
    save_data(books)
    return jsonify(new_book), 201

@app.route('/books/<isbn>', methods=['PUT'])
def update_book(isbn):
    updated_book = request.get_json()
    for book in books:
        if book['isbn'] == isbn:
            book.update(updated_book)
            save_data(books)
            return jsonify(book)
    return jsonify({'error': 'Book not found'}), 404

@app.route('/books/<isbn>', methods=['DELETE'])
def delete_book(isbn):
    global books
    books = [book for book in books if book['isbn'] != isbn]
    save_data(books)
    return jsonify({'message': 'Book deleted'})

if __name__ == '__main__':
    app.run(debug=True)assa