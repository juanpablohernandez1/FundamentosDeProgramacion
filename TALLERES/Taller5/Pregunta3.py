# Construir en Python un IC para al 93% de confianza necesario para responder: 
# ¿Puede afirmarse que la proporción de colegios privados es mínimo del 50%? No asuma normalidad
# justifique su respuesta.

import numpy as np
import pandas as pd
import math
from scipy.stats import norm

print("=== INTERVALO DE CONFIANZA PARA PROPORCIÓN DE COLEGIOS PRIVADOS ===")
print("Problema: ¿la proporción de colegios privados es mínimo del 50%?")
print("Nivel de confianza: 93%")

# 1. CARGA DE DATOS
data = pd.read_csv(
    r"C:\Users\Usuario\Desktop\Python\prueba\FundamentosDeProgramacion\TALLERES\Taller5\DatosTrabajo2EAE20242.txt"
)

nat_scores = data['NATURALEZA'].dropna()
print(f"✓ Datos cargados. Observaciones válidas: {len(nat_scores)}")

# 2. AGRUPACIÓN DE DATOS DE COLEGIOS NO OFICIALES
nat_scores_bin = (data['NATURALEZA'] == "NO OFICIAL").astype(int)

# 3. CÁLCULO DE ESTADÍSTICOS
n = len(nat_scores_bin)
phat = nat_scores_bin.mean()  
alpha = 0.07
z = norm.ppf(1 - alpha/2)  
se = math.sqrt(phat*(1-phat)/n) 
li = phat - z*se
ls = phat + z*se

print("\nPASO 2: Estadísticos muestrales")
print(f"n (tamaño de muestra): {n}")
print(f"p̂ (proporción muestral de privados): {phat:.4f}")
print(f"α (alpha): {alpha}")
print(f"Z crítico: {z:.3f}")

print("\nPASO 3: Intervalo de Confianza (93%)")
print(f"IC = ({li:.4f}, {ls:.4f})")

# 4. INTERPRETACIÓN
if li >= 0.5:
    print("\nCon 93% de confianza, Se afirma que la proporción de colegios privados es mínimo del 50%.")
else:
    print("\nCon 93% de confianza, se niega que la proporción de colegios privados es mínimo del 50%.")

