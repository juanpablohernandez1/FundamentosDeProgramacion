"""
Módulo principal de la librería de álgebra lineal
=================================================

Este módulo contiene las implementaciones de las clases Vector y Matrix,
así como las funciones de álgebra lineal asociadas.
"""

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
    
    def __getitem__(self, index: int) -> Union[int, float]:
        return self.values[index]
        """Permite acceder a los componentes del vector usando índices."""
    
    def __setitem__(self, index: int, value: Union[int, float]):
        self.values[index] = value
        """Permite modificar componentes del vector usando índices."""
    
    def __add__(self, other: 'Vector') -> 'Vector':
        if len(self.values) != len(other.values):
            raise ValueError("Los vectores no tienen la misma dimensión")
        
        result = []
        for i in range(len(self.values)):
            result.append(self.values[i] + other.values[i])
        return Vector(result)
        """Suma de vectores usando el operador +."""
    
    def __sub__(self, other: 'Vector') -> 'Vector':
        if len(self.values) != len(other.values):
            raise ValueError("Los vectores no tienen la misma dimensión")
        
        result = []
        for i in range(len(self.values)):
            result.append(self.values[i] - other.values[i])
        return Vector(result)
        """Resta de vectores usando el operador -."""
    
    def __mul__(self, scalar: Union[int, float]) -> 'Vector':
        return Vector([x * scalar for x in self.values])
        """Multiplicación por escalar usando el operador *."""
    
    def __rmul__(self, scalar: Union[int, float]) -> 'Vector':
        return self*scalar
        """Multiplicación por escalar (orden invertido)."""

    def __truediv__(self, scalar: Union[int, float]) -> 'Vector':
        if scalar == 0:
            raise ZeroDivisionError("indefinido")
        return Vector([x/scalar for x in self.values])
        """División por escalar usando el operador /."""
    
    def __eq__(self, other: 'Vector') -> bool:
        if self.values == other.values:
            return True
        else:
            return False
        """Igualdad entre vectores usando el operador ==."""
    
    def __ne__(self, other: 'Vector') -> bool:
        if self.values != other.values:
            return True
        else:
            return False
        """Desigualdad entre vectores usando el operador !=."""
    
    @property
    def magnitude(self) -> float:
        suma = 0
        for x in self.values:
            suma += x**2
        return suma**(1/2)
        """Calcula y retorna la magnitud (norma) del vector."""

    @property
    def unit_vector(self) -> 'Vector':
        if self.magnitude == 0:
            raise ValueError("Error")
        else:
            vector_normal = [x/self.magnitude for x in self.values]
            return Vector(vector_normal)
    """Retorna el vector unitario (normalizado)."""

    def dot(self, other: 'Vector') -> float:
        
        if len(self.values) != len(other.values):
            raise ValueError("Los vectores deben tener la misma dimensión")
        
        for x in range(len(self.values)):
            prod_punto += self.values[x] * other.values[x]
            return prod_punto
        """
        Calcula el producto punto con otro vector.
        
        Args:
            other: Otro vector para el producto punto
            
        Returns:
            El producto punto como un número
        """
    
    def cross(self, other: 'Vector') -> 'Vector':
        if len(self.values) != 3 or len(other.values) != 3:
            raise ValueError("Solo vectores 3D")
        
        x1, y1, z1 = self.values
        x2, y2, z2 = other.values
        
        result = [
            y1 * z2 - z1 * y2,
            z1 * x2 - x1 * z2,
            x1 * y2 - y1 * x2]
        
        return Vector(result)
        """
        Calcula el producto cruz con otro vector (solo para vectores 3D).
        
        Args:
            other: Otro vector para el producto cruz
            
        Returns:
            Un nuevo vector resultado del producto cruz
        """
        pass
    
    def angle_with(self, other: 'Vector') -> float:
        if self.magnitude or other.magnitude == 0:
            raise ValueError("Error")
        else:
            return math.acos((self.dot(other))/(self.magnitude*other.magnitude))
        """
        Calcula el ángulo entre este vector y otro.
        
        Args:
            other: Otro vector
            
        Returns:
            El ángulo en radianes
        """

class Matrix:
    """
    Clase para representar y manipular matrices.
    
    Una matriz es una colección rectangular de números organizados en filas y columnas.
    """
    
    def __init__(self, data: List[List[Union[int, float]]]):
        self.values = data
        """
        Inicializa una matriz con sus datos.
        
        Args:
            data: Lista de listas que representa las filas de la matriz
        """
    
    def __str__(self) -> str:
        return f"Matriz con componentes: {self.values}"
        """Representación en string de la matriz."""
    
    def __repr__(self) -> str:
        return f"Matriz({self.values})"
        """Representación detallada de la matriz."""
    
    def __getitem__(self, key: Union[int, Tuple[int, int]]) -> Union[List[Union[int, float]], Union[int, float]]:
        if isinstance(key, int):
            return self.values[key]
        elif isinstance(key, tuple) and len(key) == 2:
            i, j = key
            return self.values[i][j]
        else:
            raise TypeError("Error: no se puede considerar una matriz")
        """Permite acceder a filas o elementos específicos de la matriz."""

    def __setitem__(self, key: Union[int, Tuple[int, int]], value: Union[List[Union[int, float]], Union[int, float]]):
        if isinstance(key, int):
            if not isinstance(value, list):
                raise TypeError("No es una lista")
            
            if len(value) != len(self.values[0]):
                raise ValueError("La fila debe tener igual longitud que las demás")
            self.values[key] = value
            
        elif isinstance(key, tuple) and len(key) == 2:
            i, j = key
            
            if not isinstance(value, (int, float)):
                raise TypeError("Se debe introducir un número")
            self.values[i][j] = value
        
        else: 
            raise TypeError("El índice debe ser un entero o una tupla (i, j)")
        """Permite modificar filas o elementos específicos de la matriz."""

    
    def __add__(self, other: 'Matrix') -> 'Matrix':
        if len(self.values) != len(other.values) or len(self.values[0]) != len(other.values[0]):
            raise ValueError("Los vectores no tienen la misma dimensión")
        result = []
        for i in range(len(self.values)):
            fila = []
            for j in range(len(self.values[0])): 
                fila.append(self.values[i][j] + other.values[i][j])
            result.append(fila)
        return Matrix(result)
        """Suma de matrices usando el operador +."""
    
    def __sub__(self, other: 'Matrix') -> 'Matrix':
        if len(self.values) != len(other.values) or len(self.values[0]) != len(other.values[0]):
            raise ValueError("Los vectores no tienen la misma dimensión")
        result = []
        for i in range(len(self.values)):
            fila = []
            for j in range(len(self.values[0])): 
                fila.append(self.values[i][j] - other.values[i][j])
            result.append(fila)
        return Matrix(result)
        """Resta de matrices usando el operador -."""
    
    def __mul__(self, other: Union['Matrix', 'Vector', int, float]) -> Union['Matrix', 'Vector']:
        if isinstance(other, (int, float)):
            resultado = [[elemento * other for elemento in fila] for fila in self.values]
            return Matrix(resultado)
        
        elif isinstance(other, Vector):
            if len(self.values[0]) != len(other.values):
                raise ValueError("Error de multiplicación")
            else:
                resultado = []
                for x in range(len(self.values)):
                    fila = 0
                    for y in range(len(self.values[0])):
                        fila += self.values[x][y]*other.values[y]
                    resultado.append(fila)
                return Vector(resultado)
            
        elif isinstance(other, Matrix):
            if len(self.values[0]) != len(other.values):
                raise ValueError("Error de multiplicación")
            
            result = []
            for i in range(len(self.values)):
                fila = []
                for j in range(len(other.values[0])):  
                    suma = 0
                    for k in range(len(other.values)):  
                        suma += self.values[i][k] * other.values[k][j]
                        fila.append(suma)
                    result.append(fila)
            return Matrix(result)
        
        else:
            raise TypeError("Error de multiplicación")

    
    def __rmul__(self, scalar: Union[int, float]) -> 'Matrix':
        return self*scalar
        """Multiplicación por escalar (orden invertido)."""
    
    def __eq__(self, other: 'Matrix') -> bool:
        if len(self.values) != len(other.values) or len(self.values[0]) != len(other.values[0]):
            return False
        else:
            for i in range(len(self.values)):
                for j in range(len(self.values[0])):
                    if self.values[i][j] != other.values[i][j]:
                        return False
            return True
        """Igualdad entre matrices usando el operador ==."""
        pass
    
    def __ne__(self, other: 'Matrix') -> bool:
        if len(self.values) != len(other.values) or len(self.values[0]) != len(other.values[0]):
            return True
        else:
            for i in range(len(self.values)):
                for j in range(len(self.values[0])):
                    if self.values[i][j] != other.values[i][j]:
                        return True
            return False
        """Desigualdad entre matrices usando el operador !=."""
        pass
    
    @property
    def num_rows(self) -> int:
        return len(self.values)
        """Retorna el número de filas de la matriz."""
    
    @property
    def num_columns(self) -> int:
        return len(self.values[0])
        """Retorna el número de columnas de la matriz."""
    
    @property
    def shape(self) -> Tuple[int, int]:
        return (len(self.values),len(self.values[0]))
        """Retorna las dimensiones de la matriz como (filas, columnas)."""
    
    @property
    def T(self) -> 'Matrix':
        resultado = []
        for i in range(len(self.values[0])):
            fila = []
            for j in range(len(self.values)):
                fila.append(self.values[j][i])
            resultado.append(fila)
        return Matrix(resultado)
        """Retorna la transpuesta de la matriz."""
    
    @property
    def trace(self) -> Union[int, float]:
        if len(self.values) != len(self.values[0]):
            raise ValueError("La matriz no es cuadrada")
        
        else:
            lista = 0
            for i in range(len(self.values)):
                lista += self.values[i][i]
            return lista
        """Calcula y retorna la traza de la matriz (suma de elementos diagonales)."""
    
    @property
    def determinant(self) -> Union[int, float]:
        if len(self.values) != len(self.values[0]):
            raise ValueError("La matriz no es cuadrada")
        
        elif len(self.values) == 1:
            return self.values[0][0]
        
        elif len(self.values) == 2:
            return self.values[0][0]*self.values[1][1] - self.values[0][1]*self.values[1][0]
        
        else:
            det = 0 
            for j in range(len(self.values)):
                menor = [fila[:j] + fila[j+1:] for fila in self.values[1:]]
                det += ((-1) ** j) * self.values[0][j] * Matrix(menor).determinant
            return det
        """Calcula y retorna el determinante de la matriz."""
    
    @property
    def inverse(self) -> 'Matrix':
        if len(self.values) != len(self.values[0]) or determinant(self.values) == 0:
            raise ValueError("La matriz no tiene inversa")
        
        else: 
            det = self.determinant
            cofactores = []
            for i in range(len(self.values)):
                fila = []
                for j in range(len(self.values)):
                    menor = [fila[:j] + fila[j+1:] for fila in (self.values[:i] + self.values[i+1:])]
                    cofactor = ((-1) ** (i + j)) * Matrix(menor).determinant
                    fila.append(cofactor)
                cofactores.append(fila)

            adjunta = list(map(list, zip(*cofactores)))
            inversa = [[adjunta[i][j] / det for j in range(len(self.values))] for i in range(len(self.values))]
            return Matrix(inversa)
        """Calcula y retorna la matriz inversa."""
  
    def is_square(self) -> bool:
        if len(self.values) != len(self.values[0]):
            return False
        else:
            return True
        """Verifica si la matriz es cuadrada."""
    
    def is_symmetric(self) -> bool:
        """Verifica si la matriz es simétrica."""
    
    def is_diagonal(self) -> bool:
        """Verifica si la matriz es diagonal."""
    
    def get_row(self, index: int) -> 'Vector':
        """
        Obtiene una fila específica como vector.
        
        Args:
            index: Índice de la fila
            
        Returns:
            Vector con los elementos de la fila
        """
        pass
    
    def get_column(self, index: int) -> 'Vector':
        """
        Obtiene una columna específica como vector.
        
        Args:
            index: Índice de la columna
            
        Returns:
            Vector con los elementos de la columna
        """
        pass


# =============================================================================
# FUNCIONES DE VECTOR
# =============================================================================

def dot_product(v1: Vector, v2: Vector) -> float:
    """
    Calcula el producto punto entre dos vectores.
    
    Args:
        v1: Primer vector
        v2: Segundo vector
        
    Returns:
        El producto punto como un número
    """
    pass


def magnitude(v: Vector) -> float:
    """
    Calcula la magnitud (norma) de un vector.
    
    Args:
        v: El vector
        
    Returns:
        La magnitud del vector
    """
    pass


def normalize(v: Vector) -> Vector:
    """
    Normaliza un vector (lo convierte en vector unitario).
    
    Args:
        v: El vector a normalizar
        
    Returns:
        Un nuevo vector normalizado
    """
    pass


def cross_product(v1: Vector, v2: Vector) -> Vector:
    """
    Calcula el producto cruz entre dos vectores 3D.
    
    Args:
        v1: Primer vector
        v2: Segundo vector
        
    Returns:
        Un nuevo vector resultado del producto cruz
    """
    pass


def angle_between(v1: Vector, v2: Vector) -> float:
    """
    Calcula el ángulo entre dos vectores.
    
    Args:
        v1: Primer vector
        v2: Segundo vector
        
    Returns:
        El ángulo en radianes
    """
    pass


# =============================================================================
# FUNCIONES DE MATRIZ
# =============================================================================

def scale(matrix: Matrix, scalar: Union[int, float]) -> Matrix:
    """
    Multiplica una matriz por un escalar.
    
    Args:
        matrix: La matriz
        scalar: El escalar
        
    Returns:
        Una nueva matriz escalada
    """
    pass


def add(m1: Matrix, m2: Matrix) -> Matrix:
    """
    Suma dos matrices.
    
    Args:
        m1: Primera matriz
        m2: Segunda matriz
        
    Returns:
        Una nueva matriz resultado de la suma
    """
    pass


def subtract(m1: Matrix, m2: Matrix) -> Matrix:
    """
    Resta dos matrices.
    
    Args:
        m1: Primera matriz
        m2: Segunda matriz
        
    Returns:
        Una nueva matriz resultado de la resta
    """
    pass


def vector_multiply(matrix: Matrix, vector: Vector) -> Vector:
    """
    Multiplica una matriz por un vector.
    
    Args:
        matrix: La matriz
        vector: El vector
        
    Returns:
        Un nuevo vector resultado de la multiplicación
    """
    pass


def matrix_multiply(m1: Matrix, m2: Matrix) -> Matrix:
    """
    Multiplica dos matrices.
    
    Args:
        m1: Primera matriz
        m2: Segunda matriz
        
    Returns:
        Una nueva matriz resultado de la multiplicación
    """
    pass


def transpose(matrix: Matrix) -> Matrix:
    """
    Calcula la transpuesta de una matriz.
    
    Args:
        matrix: La matriz
        
    Returns:
        Una nueva matriz transpuesta
    """
    pass


def determinant(matrix: Matrix) -> Union[int, float]:
    """
    Calcula el determinante de una matriz cuadrada.
    
    Args:
        matrix: La matriz cuadrada
        
    Returns:
        El determinante
    """
    pass


def inverse(matrix: Matrix) -> Matrix:
    """
    Calcula la matriz inversa.
    
    Args:
        matrix: La matriz cuadrada invertible
        
    Returns:
        Una nueva matriz inversa
    """
    pass


def identity_matrix(size: int) -> Matrix:
    """
    Crea una matriz identidad de tamaño especificado.
    
    Args:
        size: El tamaño de la matriz (size x size)
        
    Returns:
        Una nueva matriz identidad
    """
    pass


def zeros_matrix(rows: int, columns: int) -> Matrix:
    """
    Crea una matriz de ceros con las dimensiones especificadas.
    
    Args:
        rows: Número de filas
        columns: Número de columnas
        
    Returns:
        Una nueva matriz llena de ceros
    """
    pass


def ones_matrix(rows: int, columns: int) -> Matrix:
    """
    Crea una matriz de unos con las dimensiones especificadas.
    
    Args:
        rows: Número de filas
        columns: Número de columnas
        
    Returns:
        Una nueva matriz llena de unos
    """
    pass
