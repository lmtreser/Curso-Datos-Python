# Introducción a Pandas
# Ejemplos Bloque Nro. 4
# Prof. Lucas Martín Treser

import pandas as pd

df_messi = pd.read_csv("messi_goals.csv")
df_messi["Date"] = pd.to_datetime(df_messi["Date"], format="mixed")

##### ORDENAR DATOS #####

# Ordenar por fecha de manera descendente
df_messi = df_messi.sort_values("Date", ascending=False)
print(df_messi.head())

##### TRABAJAR CON VALORES NULOS #####

# Detectar valores nulos
print(df_messi.isnull().sum())

# Rellenar valores nulos
df_messi["Type"].fillna(0, inplace=True)
print(df_messi.Type.isnull().sum())

##### CAMBIAR INDICES #####

# Usar una columna como índice
print(df_messi.info())
df_messi.set_index("GoalID", inplace=True)
print(df_messi.info())

##### APLICAR FUNCIONES A COLUMNAS #####

# Convertir todas las edades a string
df_messi["Venue"] = df_messi["Venue"].apply(str)
print(type(df_messi.Venue.iloc[0]))

# Ejecutar la función eval() en cada fila
print(df_messi["Minute"].apply(eval))

##### EXPORTAR DATOS #####

# A CSV
df_messi.to_csv("output.csv", index=False)

# A Microsoft Excel
df_messi.to_excel("output.xlsx", index=False)