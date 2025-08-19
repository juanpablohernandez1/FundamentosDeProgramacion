import math
import os
import random
import re
import sys

# 1 ≤ n ≤ 10**5 
# 1 ≤ d ≤ n 
# 1 ≤ a[i] ≤ 10**6

# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def rotateLeft(d, arr):
    n = len(arr)
    arr1 = arr[d:n]
    for x in range (0,d):
        arr1.append(arr[x])
    print(" ".join(map(str, arr1)))
d1 = int(input("Escribe el número de rotaciones a la izquierda: "))
arr11 = list(map(int, input("Escribe la lista: ").split()))
rotateLeft(d1,arr11)
    # Write your code here