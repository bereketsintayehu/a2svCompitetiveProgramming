#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    swapCount = 0
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j] > a[j+1]:
                swapCount+=1
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
    return print('Array is sorted in {} swaps.\nFirst Element: {}\nLast Element: {}'.format(swapCount, a[0], a[len(a)-1]))

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
