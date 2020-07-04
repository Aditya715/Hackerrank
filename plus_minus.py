"""
    Plus Minus Hackerrank
"""
import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    minus_count, plus_count, zero_count = 0, 0, 0
    for each in arr:
        if each < 0:
            minus_count += 1
        elif each > 0:
            plus_count += 1
        else:
            zero_count += 1
    print(round(plus_count/len(arr), 4))
    print(round(minus_count/len(arr), 4))
    print(round(zero_count/len(arr), 4))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
