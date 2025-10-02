import pandas as pd
import numpy as np
from scipy.stats import norm   

# 1. CARGA DE DATOS
df = pd.read_excel(r"C:\Users\Usuario\Desktop\Python\prueba\FundamentosDeProgramacion\TALLERES\Taller6\Base Taller 3 EAE 2025 2.xlsx")

# 2. LECTURA DE DATOS

n_total = len(df) # Tamaño de la muestra

n_estrato3 = (df["ESTRATO"] == 3).sum() # Número de estudiantes en estrato 3

p_hat = n_estrato3 / n_total # Proporción observada

p0 = 0.5 # Proporción bajo H0

# Estadístico Z
z_stat = (p_hat - p0) / np.sqrt(p0 * (1 - p0) / n_total)

# 3. TOMAR UNA DECISIÓN (cola superior porque Ha: p > 0.5)
p_value = 1 - norm.cdf(z_stat)

# Nivel de significancia
alpha = 0.06

print("Proporción observada:", p_hat)
print("Estadístico Z:", z_stat)
print("p-valor:", p_value)

if p_value < alpha:
    print("✅ No se rechaza Ha: la proporción en estrato 3 es significativamente mayor que la de los demás.")
else:
    print("❌ Se rechaza Ha: no hay evidencia suficiente para afirmar que estrato 3 > los demás.")