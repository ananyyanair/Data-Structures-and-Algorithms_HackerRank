#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'unboundedKnapsack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def unboundedKnapsack(k, arr):
    memo = [0] * (k + 1)
    for i in range(len(arr)):
        for j in range(arr[i], k + 1):
            memo[j] = max(memo[j], arr[i] + memo[j - arr[i]])
    return memo[k]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = unboundedKnapsack(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
