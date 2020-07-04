import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    right_diagonal = 0
    left_diagonal = 0
    get_length = len(arr)
    start_panel_left = 0
    start_panel_right = get_length - 1
    for each in arr:
        print(each[start_panel_right])
        print(each[start_panel_left])
        left_diagonal += each[start_panel_left]
        right_diagonal += each[start_panel_right]
        start_panel_left += 1
        start_panel_right -= 1
    return abs(right_diagonal-left_diagonal) 

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    # fptr.write(str(result) + '\n')

    # fptr.close()
