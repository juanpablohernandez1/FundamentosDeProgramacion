import math
import os
import random
import re
import sys
from itertools import combinations

def maximumPerimeterTriangle(sticks):
    lista = []
    sticks_orden = sorted(sticks)
    for triangulo in combinations(sticks_orden, 3):
        if triangulo[0] + triangulo[1] <= triangulo[2]:
            pass
        else:
            suma = triangulo[0] + triangulo[1] + triangulo[2]
            lista.append(suma)
    if not lista:
        print(-1)
    else:
        print(max(lista))
medidas_triangulo = list(map(int, input("Escribe las medidas del triangulo: ").split()))
maximumPerimeterTriangle(medidas_triangulo)
