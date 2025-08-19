import math
import os
import random
import re
import sys

def missingNumbers(arr, brr):
    lista = []
    for x in range (0,len(brr)):
        if brr[x] in arr:
            pass
        else:
            lista.append(brr[x])
    print(*lista)
arr1 = list(map(int, input("Escribe la primera lista a comparar ").split()))
brr1 = list(map(int, input("Escribe la segunda lista a comparar ").split()))
missingNumbers(arr1, brr1)
    