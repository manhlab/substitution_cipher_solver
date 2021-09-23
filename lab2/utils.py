
import hashlib
SECRET = "thisissecret"

def key_256(key):
    return hashlib.sha256((key + SECRET).encode("utf-8")).hexdigest()


def subkeygen(s1, s2, i):
    # print ("GENERATING KEY #" + str(i))
    # print ("S1: " + s1)
    # print ("S2: " + s2)
    result = hashlib.sha256((s1 + s2).encode("utf-8")).hexdigest()
    # print ("RESULT: " + result)
    return result


def scramble(x, i, k):
    k = stobin(k)
    x = stobin(str(x))
    k = bintoint(k)
    x = bintoint(x)
    res = pow((x * k), i)
    res = itobin(res)
    return bintostr(res)


# xor two strings
def xor(s1, s2):
    return "".join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))


# string to binary
def stobin(s):
    return "".join("{:08b}".format(ord(c)) for c in s)


# binary to int
def bintoint(s):
    return int(s, 2)


# int to binary
def itobin(i):
    return bin(i)


# binary to string
def bintostr(b):
    return "".join(chr(int(b[i : i + 8], 2)) for i in range(0, len(b), 8))