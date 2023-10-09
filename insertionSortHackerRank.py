#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    e = arr[-1]
    sr = arr[:-1]
    rsr = []
    for i in range(n - 2, -1, -1):
        if arr[i] < e:
            print(*sr, e, *rsr)
            return
        print(*sr, arr[i], *rsr)
        rsr.insert(0, sr.pop())
    print(*sr, e, *rsr)
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
