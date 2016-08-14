import sys
from fractions import gcd

keyA = int(sys.argv[1])
keyB = int(sys.argv[2])
message = sys.argv[3]

for m in message:
    m = ord(m)-65
    d = keyA*(m-keyB) % 26
    if d > 25:
        d -= 25
    d += 65
    print chr(d)
