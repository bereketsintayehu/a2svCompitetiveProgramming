#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    roundedGrade = []
    for i in range (len(grades)):
        if grades[i] < 37:
            roundedGrade.append(grades[i])
        elif grades[i]%5 >= 3:
            roundedGrade.append(grades[i]+5-(grades[i]%5))
        else:
            roundedGrade.append(grades[i])
    return roundedGrade

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
