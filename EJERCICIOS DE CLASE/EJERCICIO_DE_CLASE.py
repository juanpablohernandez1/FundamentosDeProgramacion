import numpy as np
import pandas as pd
import math
from scipy import stats
from scipy.stats import norm,t,f,chi2, shapiro

# 1. CARGA DE DATOS
data = pd.read_excel(r"C:\Users\Usuario\Desktop\Python\prueba\FundamentosDeProgramacion\EJERCICIOS DE CLASE\Induccion.xls")
print(data.head())

# 2. HIPÓTESIS
# H0: Xi es Normal
# Ha: Xi No es normal

