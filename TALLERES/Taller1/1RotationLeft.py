import math
import os
import random
import re
import sys

def rotateLeft(d, arr):
    n = len(arr)
    arr1 = arr[d:n]
    for x in range (0,d):
        arr1.append(arr[x])
    print(" ".join(map(str, arr1)))
d1 = int(input("Escribe el número de rotaciones a la izquierda: "))
arr11 = list(map(int, input("Escribe la lista: ").split()))
rotateLeft(d1,arr11)