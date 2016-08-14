import sys
from fractions import gcd
from xgcd import xgcd
a = int(sys.argv[1])

for i in xrange(0,a):
    if(gcd(i, a) == 1):
        print xgcd(i,
a);
        print i;
