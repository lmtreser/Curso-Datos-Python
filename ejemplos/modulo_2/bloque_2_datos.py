# Introducción a Pandas
# Ejemplos Bloque Nro. 2
# Prof. Lucas Martín Treser

import pandas as pd

# Leer un archivo CSV (dataset ficticio sobre goles de Messi)
df_messi = pd.read_csv("messi_goals.csv")

##### METODOS PARA EXPLORAR DATOS #####

# Ver la estructura del DataFrame
print(df_messi.info())

# Ver los tipos de datos de las columnas del dataset
print(df_messi.dtypes)

# Ver la cantidad de registros y columnas del dataset
print(f"El dataset tiene {df_messi.shape[0]} registros y {df_messi.shape[1]} columnas.")

# Estadísticas descriptivas, columnas numéricas
print("Estadísticas descriptivas (numericas):")
print(df_messi.describe())  # Media, desviación estándar, etc.

# Estadísticas descriptivas, columnas categoricas
print("Estadísticas descriptivas (categoricas):")
print(df_messi.describe(include=['object']))  # Media, desviación estándar, etc.

# Ver los valores únicos en la columna "Club"
print("Clubes únicos en el dataset:")
print(df_messi.Club.unique())

# Ver la cantidad de goles por cada club
print("Cantidad de goles por club:")
print(df_messi.Club.value_counts())

# Ver las primeras 5 filas del dataset
print("Primeras 5 filas:")
print(df_messi.head(5))

# Ver los últimos 4 registros del dataset
print("Últimos 4 registros:")
print(df_messi.tail(4))

# Ver 3 registros aleatorios del dataset
print("3 registros aleatorios:")
print(df_messi.sample(3))

# Obtener el menor y el mayor minuto en el que Messi anotó
print("Menor minuto en el que Messi anotó un gol:")
print(df_messi["Minute"].min())

print("Mayor minuto en el que Messi anotó un gol:")
print(df_messi["Minute"].max())

# Sumar todos los minutos de juego donde anotó
print("Suma total de minutos donde Messi anotó:")
print(df_messi["Minute"].sum())

##### INDEXACION BASICA #####

# Acceder a la columna "Club" de dos maneras diferentes
print("Lista de clubes (forma 1):")
print(df_messi["Club"])

print("Lista de clubes (forma 2):")
print(df_messi.Club)

# Crear un pequeño DataFrame para pruebas adicionales
df = pd.DataFrame({
    "Goals": [2, 1, 3],
    "Assists": [1, 0, 2]
}, index=["Match 1", "Match 2", "Match 3"])

# Seleccionar una fila por etiqueta
print("Datos del partido 2:")
print(df.loc["Match 2"])

# Seleccionar múltiples filas y columnas
print("Datos de los goles del partido 1 y partido 3:")
print(df.loc[["Match 1", "Match 3"], ["Goals"]])

# Filtrar con condiciones (partidos con más de 2 goles)
print("Partidos donde Messi anotó más de 2 goles:")
print(df.loc[df["Goals"] > 2])

# Acceder a una fila por índice
print("Primera fila del dataset original:")
print(df_messi.iloc[0])

# Seleccionar la segunda fila
print("Segunda fila del dataset original:")
print(df_messi.iloc[1])

# Seleccionar un rango de filas
print("Primeras dos filas del dataset original:")
print(df_messi.iloc[0:2])

# Seleccionar un rango de filas y columnas
print("Primeras dos filas y la primera columna:")
print(df_messi.iloc[0:2, 0:1])