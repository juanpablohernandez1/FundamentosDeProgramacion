import math
import os
import random
import re
import sys

def staircase(n):
    lista = []
    for x in range(0,n):
        escalon = " "*(n - x) + "#"*(x+1)
        lista.append(escalon)
        print(lista[x])
staircase(12)
    
