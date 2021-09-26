import json
import string
import random

def encrypt(file = "book/book.json"):
    text = str(input("Enter your text: "))
    with open(file) as f:
        book = json.load(f)
    print(book)
    book = {ord(x): y for (x, y) in book.items()}
    print(f"Cryptotext is : {text.translate(book)}")
    
def analys(file = "book/book.json"):
    text = str(input("Enter your text: "))
    with open(file) as f:
        book = json.load(f)
    
    book = {ord(x): y for (x, y) in book.items()}
    crypto = text.translate(book)
    print(f"Cryptotext is : {crypto}")
    
    abc = "abcdefghijklmnopqrstuvwxyz"  
    # book = {ord(x): y for (x, y) in book.items()}
    # key = list(abc)
    # crypto = []
    # for i in range(1000):
    #     random.shuffle(key)
    #     text = "".join(key)
    #     crypto.append(text.translate(book))
    key = list(abc)
    stat = dict(zip(key, [0]*len(key)))
    for st in crypto:
        if st != ' ':
            stat[st] +=1
    print(stat)
            
    
