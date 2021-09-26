
import numpy
import hashlib
import math
from fraction import Fraction

SECRET = "thisissecret"
PI = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
def key_256(key):
    return hashlib.sha256((key + SECRET).encode("utf-8")).hexdigest()[:4]

def scramble(x, k):
    k = stobin(k)    
    x = stobin(x)
    k = bintoint(k)
    x = bintoint(x)
    x = numpy.float128(x)    
    x = x*(x % (2*PI))
    res = (numpy.power(2, 64, dtype= numpy.float128)-1)*\
        abs(abs(numpy.cos(x, dtype=numpy.float128)) + \
            numpy.power(5, -abs(k), dtype= numpy.float128) -1)
    res = int(res) 
       
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
    return "".join(chr(int(b[i: i + 8], 2)) for i in range(0, len(b), 8))
