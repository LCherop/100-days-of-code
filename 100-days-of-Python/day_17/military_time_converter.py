#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    splited = s.split(':')
    hr = int(splited[0])

    if 'PM' in s:
        if hr == 12:
            hr24 = 12
        else: 
            hr24 = hr+12
            if hr24 == 24:
                hr24 = 0
    if 'AM' in s:
        if hr == 12:
            hr24 = 0
        else:
            hr24 = hr
                
    last = splited[2]
    new_s = str(hr24).zfill(2) + ':'+ splited[1] + ':'+ last[:2] 
    return new_s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
