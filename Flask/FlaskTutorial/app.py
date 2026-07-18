from flask import Flask,jsonify,request

app=Flask(__name__)

books=[
    {'id':1, 'title':'book1', 'author':'author1'},
    {'id':2, 'title':'book2', 'author':'author2'},
    {'id':3, 'title':'book3', 'author':'author3'},
    {'id':4, 'title':'book4', 'author':'author4'},
]

# create a home route
@app.route('/')
def home():
    return 'home page'

# route to get all books
@app.route('/books',methods=['GET'])
def get_books():
    return jsonify(books)

#  route to get a specific book bu id

@app.route('/books/<int:book_id>',methods=['GET'])
def get_book(book_id):
    for book in books:
        if book['id']==book_id:
            return jsonify(book)
    return jsonify({'error':'book not found'}) 

@app.route('/books',methods=['POST']) 
def add_book():
   
    data = request.get_json() or {}
    
   
    new_book = {
        "id": data.get('id'),
        "title": data.get('title'),
        "author": data.get('author')
    }
    
    
    if not new_book['id'] or not new_book['title']:
        return jsonify({'error': 'Missing id or title'}), 400
        
    books.append(new_book)
    
    return jsonify({'message': 'book added successfully'}), 201

    
        
if __name__=='__main__':
     app.run(debug=True)
