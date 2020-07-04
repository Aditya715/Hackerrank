#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    def find_sum(array):
        total = 0
        for item in array:
            total += item
        return total

    arr.sort()
    print(find_sum(arr[:-1]), find_sum(arr[1:]))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
