# Introducción a Pandas
# Ejemplos Bloque Nro. 3
# Prof. Lucas Martín Treser

import pandas as pd

df_messi = pd.read_csv("./ejemplos/messi_goals.csv")

##### CONVERTIR DATOS #####

# Para verificar el tipo de datos actual
print(df_messi.dtypes)

# Verificar el tipo específico de una columna
print(type(df_messi["Minute"].iloc[0]))

# Mostrar algunas filas para ver el contenido de la columna
print(df_messi["Minute"].head())

##### CONVERTIR A NUMEROS #####

# Datos están en object (texto) pero representan números
# pd.to_numeric convierte los valores a números
# El parámetro errors="coerce" maneja valores no convertibles
# Los valores no convertibles se convierten en NaN

df_messi["Minute"] = pd.to_numeric(df_messi["Minute"], errors="coerce")
print(df_messi["Minute"].info())
print(df_messi["Minute"].head())

# Mostrar las filas con valores NaN, devuelve True
print(df_messi["Minute"].isnull())

# Podemos saber cuántos valores nulos tenemos aplicando sum()
print(df_messi["Minute"].isnull().sum())

# Forzar a valores enteros: eliminar los NaN y convertir a int
df_messi["Minute"] = pd.to_numeric(df_messi["Minute"], errors="coerce").fillna(0).astype(int)
print(df_messi["Minute"].info())
print(df_messi["Minute"].head())

# Convertir int a float
df_messi["Minute"] = df_messi["Minute"].astype(float)
print(df_messi["Minute"].info())
print(df_messi["Minute"].head())

# Convertir float a int
df_messi["Minute"] = df_messi["Minute"].astype(int)
print(df_messi["Minute"].info())
print(df_messi["Minute"].head())

##### CONVERTIR A STRINGS #####

# astype(str) convierte todos los valores a cadenas
df_messi["Minute"] = df_messi["Minute"].astype(str)
print(df_messi["Minute"].info())
print(df_messi["Minute"].head())

# Convertir incluso valores nulos
df_messi["Minute"] = df_messi["Minute"].fillna("").astype(str)
print(df_messi["Minute"].info())
print(df_messi["Minute"].head())

##### CONVERTIR A FECHA #####

# Antes de convertir, veamos el contenido de la columna
print(df_messi["Date"].head())

# Convertir a formato datetime estableciendo el formato
#  pd.to_datetime(df["column"], format="%d/%m/%y")
# Convertir manejando formatos mixtos automáticamente
df_messi["Date"] = pd.to_datetime(df_messi["Date"], format="mixed")

print(df_messi["Date"].head())
print(df_messi["Date"].info())

##### FILTRAR DATOS #####

# Filtra las filas donde la columna "Minute" es menor a 5
serie_minute = df_messi["Minute"] < 5
print(serie_minute.info())
print(serie_minute.head())
filtro_minute = df_messi[serie_minute] 
print(filtro_minute.info())
print(filtro_minute.head())

# Filtrar filas donde el tiempo de juego sea menor a 5
filtro = df_messi[(df_messi["Minute"] > 0) & (df_messi["Minute"] < 5)]
print(filtro.info())
print(filtro)

# Filtrar solo los goles anotados en LaLiga
# Generar una mascara (mask), que es una Serie booleana
mask_laliga = df_messi["Competition"] == "LaLiga"
print(mask_laliga.info())
print(mask_laliga.head())

# Apliquemos la máscara al DataFrame
df_laliga = df_messi.loc[mask_laliga]
print(df_laliga.info())
print(df_laliga.head())

# Contar la cantidad de goles anotados en LaLiga
cant_laliga = df_laliga["GoalID"].count()
total_goles = df_messi["GoalID"].count()
print(f"Messi anotó {cant_laliga} goles en LaLiga de un total de {total_goles} goles registrados.")

# Filtrar los goles anotados contra el equipo que menos goles recibió
# idxmin() devolverá el índice del valor mínimo del primer valor de la serie
min_opponent = df_messi["Opponent"].value_counts().idxmin()
mask_opponent = df_messi["Opponent"] == min_opponent
df_min_opponent = df_messi.loc[mask_opponent]

cant_goles_min = df_min_opponent["GoalID"].count()
print(f"El equipo que menos goles recibió de Messi fue {min_opponent} con {cant_goles_min} goles.")

# Filtrar los goles en una temporada específica (ejemplo: 2014/2015)
mask_season = df_messi["Season"] == "14/15"
df_season = df_messi.loc[mask_season]
cant_goles_season = df_season["GoalID"].count()
print(f"En la temporada 2014/2015, Messi anotó {cant_goles_season} goles.")

# Filtrar los goles anotados en el minuto inicial (0 a 5 minutos)
mask_minuto_inicial = df_messi["Minute"] <= 5
df_minuto_inicial = df_messi.loc[mask_minuto_inicial]
cant_minuto_inicial = df_minuto_inicial["GoalID"].count()
print(f"Messi anotó {cant_minuto_inicial} goles en los primeros 5 minutos de juego.")

# Filtrar los goles anotados en finales de competiciones
mask_finales = df_messi["Matchday"] == "Final"
# mask_finales = df_messi["Matchday"].str.lower() == "final"

df_finales = df_messi.loc[mask_finales]
cant_finales = df_finales["GoalID"].count()
print(f"Messi anotó {cant_finales} goles en finales.")

# Filtrar los goles con asistencia de un jugador específico (ejemplo: Iniesta)
mask_asistencia = df_messi["Goal_assist"] == "Andres Iniesta"
df_asistencias = df_messi.loc[mask_asistencia]
cant_asistencias = df_asistencias["GoalID"].count()
print(f"Iniesta asistió en {cant_asistencias} goles de Messi.")

# Filtrar los goles en partidos jugados fuera de casa
mask_away = df_messi["Venue"] == "A"
df_away = df_messi.loc[mask_away]
cant_away = df_away["GoalID"].count()
print(f"Messi anotó {cant_away} goles en partidos fuera de casa.")

# Filtrar los goles contra equipos específicos (ejemplo: Real Madrid y Atlético de Madrid)
mask_big_rivals = df_messi["Opponent"].isin(["Real Madrid", "Atletico de Madrid"])
df_big_rivals = df_messi.loc[mask_big_rivals]
cant_big_rivals = df_big_rivals["GoalID"].count()
print(f"Messi anotó {cant_big_rivals} goles contra Real Madrid y Atlético de Madrid.")

# Filtrar los goles en competencias internacionales (Champions League)
mask_international = df_messi["Competition"] == "UEFA Champions League"
df_international = df_messi.loc[mask_international]
cant_international = df_international["GoalID"].count()
print(f"Messi anotó {cant_international} goles en la Champions League.")

# Filtrar los goles en partidos jugados en una fecha específica (ejemplo: 17 de junio de 2007)
mask_fecha = df_messi["Date"] == "2007-06-17"
df_fecha = df_messi.loc[mask_fecha]
cant_fecha = df_fecha["GoalID"].count()
print(f"El 17 de junio de 2007, Messi anotó {cant_fecha} goles.")

##### MANIPULAR COLUMNAS #####

# Crear una nueva columna
df_messi["Minutos"] = df_messi["Minute"]
print(df_messi.info())
print(df_messi.Minutos.head())

# Modificar el nombre de una columna
df_messi = df_messi.rename(columns = {"Minutos": "Minutitos"})
print(df_messi.info())

# Eliminar la columna "Minutitos"
df_messi = df_messi.drop("Minutitos", axis=1)
print(df_messi.info())

##### AGRUPAR DATOS #####

# Agrupar por una columna según los valores únicos en la columna Date
# Todas las filas que tienen el mismo valor en Date se agrupan juntas
agrupado = df_messi.groupby("Date")["Minute"]

for grupo, datos in agrupado:
    print(f"Grupo: {grupo}")
    print(datos)