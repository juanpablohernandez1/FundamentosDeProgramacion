import math
from typing import List, Union, Tuple, Optional

class Vector:
    """
    Clase para representar y manipular vectores.
    
    Un vector es una lista de números que puede representar
    puntos en el espacio, direcciones, o cualquier secuencia ordenada de valores.
    """
    
    def __init__(self, components: List[Union[int, float]]):
        self.values = components
        """Inicializa un vector con sus componentes"""
    
    def __str__(self) -> str:
        return f"Vector con componentes: {self.values}"
        """Representación en string del vector."""
    
    def __repr__(self) -> str:
        return f"Vector({self.values})"
        """Representación detallada del vector."""
    
    def __len__(self) -> int:
        return len(self.values)        
    """Retorna la dimensión del vector."""
    
    
    def magnitude(self) -> float:
        suma = 0
        for x in self.values:
            suma = x**2
        return suma**(1/2)


def zeros(size):
    return Vector([0] * size)

prueba = zeros(7)
print(prueba)
