# ¿Se puede afirmar que el resultado medio obtenido por los colegios en Lectura Crítica es mayor 
# en los colegios de jornada completa que los que prestan servicio en jornadas diferentes? 
# Construir en Python un IC para al 90% de confianza asumiendo normalidad de las variables involucradas
# justifique su respuesta.

import numpy as np
import pandas as pd
import math
from scipy.stats import norm
from scipy.stats import t

print("=== INTERVALO DE CONFIANZA PARA MEDIA DE LECTURA ===")
print("Problema: ¿Los colegios de jornada completa tienen mejor resultado medio que los demás?")
print("Nivel de confianza: 90%")

# 1. CARGA DE DATOS
data = pd.read_csv(r"C:\Users\Usuario\Desktop\Python\prueba\FundamentosDeProgramacion\TALLERES\Taller5\DatosTrabajo2EAE20242.txt")
lectura_scores = data['PROMLECT'].dropna()
print(f"✓ Datos cargados. Observaciones válidas: {len(lectura_scores)}")

# 2. CÁLCULO DE ESTADÍSTICOS MUESTRALES
print("\nPASO 2: Cálculo de estadísticos muestrales")
data["COMPARACIÓN_JORNADA_COMPLETA"] = data["JORNADA"].apply(lambda x: "COMPLETA" if x == "COMPLETA" else "OTRAS")
datajornada = data.groupby("COMPARACIÓN_JORNADA_COMPLETA")['PROMLECT'].agg(
    n="count",                   # tamaño de muestra
    media="mean",                 # media muestral
    desv_std=lambda x: np.std(x, ddof=1)  # desviación estándar muestral
)

print("\n=== Estadísticos por JORNADA ===")
print(datajornada)

# 3. CONSTRUCCIÓN DEL INTERVALO DE CONFIANZA
print(f"\nPASO 3: Construcción del IC al 90%")

media_completa = datajornada.loc["COMPLETA", "media"]
media_otras = datajornada.loc["OTRAS", "media"]
diferencia = abs(media_completa - media_otras)

n1 = datajornada.loc["COMPLETA", "n"]
n2 = datajornada.loc["OTRAS", "n"]
s1 = datajornada.loc["COMPLETA", "desv_std"]
s2 = datajornada.loc["OTRAS", "desv_std"]

se = math.sqrt((s1**2)/n1 + (s2**2)/n2) # Error estándar de la diferencia

df = ((s1**2/n1 + s2**2/n2)**2) / (
    ((s1**2/n1)**2)/(n1-1) + ((s2**2/n2)**2)/(n2-1)
) # Grados de libertad de Welch

alpha = 0.10 # Para IC del 90%

# Valor crítico t
tcrit = t.ppf(1 - alpha/2, df)

# Margen de error
margen = tcrit * se

# Intervalo de confianza
li, ls = diferencia - margen, diferencia + margen

# Mostrar resultados
print(f"Diferencia de medias: {diferencia:.3f}")
print(f"Error estándar: {se:.3f}")
print(f"gl (Welch): {df:.2f}")
print(f"t crítico: {tcrit:.4f}")
print(f"IC 90%: ({li:.3f}, {ls:.3f})")

# 4. RESPUESTA A LA PREGUNTA
print(f"\nPASO 5: Respuesta a la pregunta")
print(f"Pregunta: ¿Los colegios de jornada completa tienen mejor resultado medio que los demás?")

if ls < media_otras:
   conclusion = f"NO se puede afirmar que μ > {media_otras}"
   explicacion = f"Todo el IC está por debajo de {media_otras}"
elif li > media_otras:
   conclusion = f"SÍ se puede afirmar que μ > {media_otras}"
   explicacion = f"Todo el IC está por encima de {media_otras}"
else:
   conclusion = f"NO se puede afirmar con 90% de confianza que μ > {media_otras}"
   explicacion = f"El valor {media_otras} está dentro del IC"


print(f"\nCONCLUSIÓN: {conclusion}")
print(f"RAZÓN: {explicacion}")
