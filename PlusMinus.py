#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    posCount = 0
    negCount = 0
    zeroCount = 0
    for x in arr:
        if (x >0):
            posCount+= 1
        elif (x < 0):
            negCount += 1
        elif (x == 0):
            zeroCount += 1
    print (posCount/ len(arr))
    print (negCount / len(arr))
    print (zeroCount / len(arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
