import json
import string

def encrypt(file = "book/book.json"):
    text = str(input("Enter your text: "))
    with open(file) as f:
        book = json.load(f)
    print(book)
    book = {ord(x): y for (x, y) in book.items()}
    print(f"Cryptotext is : {text.translate(book)}")
    