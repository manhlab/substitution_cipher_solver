import sys, getopt, hashlib
from math import exp, expm1
import argparse
from utils import key_256, subkeygen, scramble, xor
ROUNDS = 4
BLOCKSIZE = 8
BLOCKSIZE_BITS = 64


def main(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str)
    parser.add_argument("--output", type=str)
    parser.add_argument("--key", type=str)
    parser.add_argument('--dec', default=False, action='store_true')
    parser.add_argument('--enc', default=False, action='store_true')
    args = parser.parse_args(args)
    filename = args.input
    key = args.key
    outfilename = args.output
    decrypt  = args.dec
    encrypt = args.enc
    with open(filename, "r") as f:
        input = f.read()
    # call the crypto function
    if encrypt:
        output = encryptMessage(key, input)
        print("Encrypt: Success run the operation!")
    elif decrypt:
        output = decryptCipher(key, input)
        print("Decrypt: Success run the operation!")

    with open(outfilename, "w+") as fw:
        fw.write(output)
    


def encryptMessage(key, message):
    ciphertext = ""
    n = BLOCKSIZE  # 8 bytes (64 bits) per block

    # Split mesage into 64bit blocks
    message = [message[i : i + n] for i in range(0, len(message), n)]
    lengthOfLastBlock = len(message[len(message) - 1])

    if lengthOfLastBlock < BLOCKSIZE:
        for i in range(lengthOfLastBlock, BLOCKSIZE):
            message[len(message) - 1] += " "
    # generate a 256 bit key based of user inputted key
    key = key_256(key)
    for block in message:
        L = [""] * (ROUNDS + 1)
        R = [""] * (ROUNDS + 1)
        L[0] = block[0 : int(BLOCKSIZE / 2)]
        R[0] = block[int(BLOCKSIZE / 2) :]
        for i in range(1, ROUNDS + 1):
            L[i] = R[i - 1]
            R[i] = xor(L[i - 1], scramble(R[i - 1], i, key))

        ciphertext += L[ROUNDS] + R[ROUNDS]

    return ciphertext


def decryptCipher(key, ciphertext):
    message = ""
    n = BLOCKSIZE  # 8 bytes (64 bits) per block
    # Split message into 64bit blocks
    ciphertext = [ciphertext[i : i + n] for i in range(0, len(ciphertext), n)]
    lengthOfLastBlock = len(ciphertext[len(ciphertext) - 1])
    if lengthOfLastBlock < BLOCKSIZE:
        for i in range(lengthOfLastBlock, BLOCKSIZE):
            ciphertext[len(ciphertext) - 1] += " "

    # generate a 256 bit key based off the user inputted key
    key = key_256(key)
    for block in ciphertext:
        # print ("Block: " + block)
        L = [""] * (ROUNDS + 1)
        R = [""] * (ROUNDS + 1)
        L[ROUNDS] = block[0 : int(BLOCKSIZE / 2)]
        R[ROUNDS] = block[int(BLOCKSIZE / 2) :]
        for i in range(ROUNDS, 0, -1):
            R[i - 1] = L[i]
            L[i - 1] = xor(R[i], scramble(L[i], i, key))

        message += L[0] + R[0]

    return message




if __name__ == "__main__":
    main()
