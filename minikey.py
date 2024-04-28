#!/usr/bin/python3

import random
import sys



all1 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
all2 = '23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'



#y=int(sys.argv[1])



if int(sys.argv[1]) == 22 :
    while True:
        length1 = 21
        password1 = "".join(random.sample(all1,length1))
        print ("S"+password1)
        print ("S"+password1 [::-1])




if int(sys.argv[1]) == 30 :
    while True:
        length2 = 29
        password2 = "".join(random.sample(all2,length2))
        print ("S"+password2)
        print ("S"+password2 [::-1])
