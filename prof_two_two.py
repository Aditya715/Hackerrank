#!/bin/python3

import os
import sys
import math

"""strength(i , j)
{
    if a[i] = 0
        return 0; //If first child has value 0 in the group, strength of group is zero
    value = 0;
    for k from i to j
        value = value*10 + a[k]
    return value;
}"""

#
# Complete the twoTwo function below.
#
def twoTwo(a):
    def strength(i, j):
        global a
        if a[i] == 0:
            return 0
        value = 0
        # convert string to list and make all as integer
        a = list(map(int, a))
        for k in range(i, j):
            value = value*10 + a[k]
        return value
    
    count = 0
    for i in range(len(a)):
        j = i + 1
        while j <= len(a):
            strength_value = strength(i , j)
            if strength_value != 0:
                check_flag = math.log2(strength_value)
                if math.ceil(check_flag) == math.floor(check_flag):
                    count += 1
            j += 1
    return count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        a = input()

        result = twoTwo(a)
        print(result)
        # fptr.write(str(result) + '\n')

    # fptr.close()
