from sqrtmod import jacobi
from random import randrange

n = int(input("Enter your number: "))
a = randrange(1,n)
x = jacobi(a, n)
if(x == 0):
    print str(n) + " is composite."
    exit()
y = pow(a,(n-1)/2) % n
if y==(n-1):
    y = -1
if x==y:
    print str(n) + " is prime."
else:
    print str(n) + " is composite."
