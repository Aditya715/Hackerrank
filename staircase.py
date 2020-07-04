#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    n = n-1
    num_of_hash = 1
    while n >= 0:
        print(" "*n + "#"*num_of_hash)
        n -= 1
        num_of_hash += 1

if __name__ == '__main__':
    n = int(input())

    staircase(n)