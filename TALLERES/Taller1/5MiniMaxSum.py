import math
import os
import random
import re
import sys
from itertools import combinations

def miniMaxSum(arr):
    lista = []
    for comb in combinations(arr, 4):
        lista.append(comb[0] + comb[1] + comb[2] + comb[3])
    print(min(lista),max(lista))
valor = list(map(int, input("Escribe los números (mínimo 5): ").split()))
miniMaxSum(valor)