#!/usr/bin/python3

from bit import *
from bit.format import bytes_to_wif
import random
import sys

y = int(sys.argv[1])

b = 2**y
a = 2**(y-1)

count = 0
while (count == 0):
    ran = random.randrange(a,b)
    seed = str(ran)
    key = Key.from_int(ran)
    print (key.to_hex())
