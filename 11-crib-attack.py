import numpy as np
from xgcd import xgcd
from fractions import gcd
import sys

###ONLY WORKS FOR 2X2 MATRICES###

##NOT MINE##
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return 0
        #raise Exception('modular inverse does not exist')
    else:
        return x % m
##END NOT MINE##

##FUNCTIONS##    

def setCrib(crib,size):
    a1 = ord(crib[0])-65
    a2 = ord(crib[2])-65
    b1 = ord(crib[1])-65
    b2 = ord(crib[3])-65
    return np.matrix( ((a1,a2), (b1,b2)) )

def setCipher(cipher, i):
    a1 = ord(cipher[i])-65
    a2 = ord(cipher[i+2])-65
    b1 = ord(cipher[i+1])-65
    b2 = ord(cipher[i+3])-65
    return np.matrix( ((a1,a2), (b1,b2)) )

def matrixInverseMod(X):
    ##hard coded the adjoint:
    adjX = np.matrix( ((X.item((1,1)),-X.item((0,1))),
                       (-X.item((1,0)),X.item(0,0))) )

    #print adjX
        
    det = np.linalg.det(X.copy()) % 26
    invDet = modinv(int(round(det)),26)
    return (invDet*adjX)%26

def computeKeyMod(Y, invX):
    return (Y*invX) % 26

def decrypt(invK, cipher):
    plaintext = ""
    for i in xrange(0, len(cipher)-1, 2):
        #Y = np.matrix( [[1], [2]] )
        Y = np.matrix( [[ord(cipher[i])-65],[ord(cipher[i+1])-65]] )
        #print Y
        X = (invK*Y) % 26
        plaintext += chr(X.item(0,0)+65)
        plaintext += chr(X.item(1,0)+65)
        
    return plaintext

##END FUNCTIONS##



### MAIN ###
blocksize = 2
cipher = "OVNADGTRUUNFGWGLMO"
crib = "ATTACK"

X = setCrib(crib, blocksize*blocksize)
#print X

for i in xrange(0, len(cipher)-(blocksize*blocksize+1), 1):
    Y = setCipher(cipher, i)
    #print Y

    invX = matrixInverseMod(X)
    #print invX

    K = computeKeyMod(Y,invX)
    #print K

    invK = matrixInverseMod(K)
    #print invK

    print decrypt(invK,cipher)
    print
