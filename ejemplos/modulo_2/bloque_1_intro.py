# Introducción a Pandas
# Ejemplos Bloque Nro. 1
# Prof. Lucas Martín Treser

import pandas as pd
# Es posible importar una clase o función específica de un módulo
from pandas import Series

# Definimos una Series
mi_series = Series([17,5,7,5,67,84,29,52,12,53,1,10])

# El patrón de sintaxis es el siguiente: Series([valores])
# Donde valores es una lista de valores que queremos que tenga la Serie
print("El contenido de la Series es:\n\n", mi_series)

# Crear un DataFrame desde un diccionario
data = {
    "Nombre": ["Juan", "Ana", "Luis"],
    "Edad": [25, 30, 22],
    "Ciudad": ["Buenos Aires", "Mar del Plata", "Tandil"]
}

mi_dataframe = pd.DataFrame(data)
print("\nEl contenido del dataframe es:\n\n", mi_dataframe)