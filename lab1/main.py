import json
import string
from encrypt import encrypt, analys
from decrypt import decrypt
import random
import string

def new_book():
    debug = True
    alpha = "abcdefghijklmnopqrstuvwxyz"  
    key = list(alpha)
    if debug:
        
        random.shuffle(key)
        key = "".join(key) 
        # trans = str.maketrans(alpha, key)
        trans = dict(zip(alpha, key))
        with open('book/book.json', 'w') as fp:
            json.dump(trans, fp)
    else:
        book = {}
        value = []
        for item in key:
            while True:
                sd = str(input(f"Character encode for {item}: "))
                
                if sd in value:
                    print("Value already in book, please choose anorther!")
                else:
                    book[item] = sd
                    value.append(sd)
                    break
            
        with open('book/book.json', 'w') as fp:
            json.dump(book, fp)

if __name__ == "__main__":
    print("-"*25)
    print("Press 1: Setup new book")
    print("Press 2: Encrypt new text")
    print("Press 3: Decrypt cryptotext")
    print("Press 4: Cryptoanalys")
    print("-"*25)
    while True:
        option = int(input("Enter your option: "))
        if option==1:
            new_book()
            break
        elif option==2:
            encrypt()
            break
        elif option==3:
            decrypt()
            break
        elif option==4:
            analys()
            break
        else:
            print("Operattor now permited!")
    