import json
import string

def decrypt(file = "book/book.json"):
    text = str(input("Enter your cryptotext: "))
    with open(file) as f:
        book = json.load(f)
    book = {ord(v): k for k, v in book.items()}
    print(f"Origin text is : {text.translate(book)}")
