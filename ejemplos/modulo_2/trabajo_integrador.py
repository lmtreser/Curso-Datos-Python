# Introducción a Pandas
# Ejemplo de Trabajo Integrador
# Prof. Lucas Martín Treser 

import pandas as pd

df_messi = pd.read_csv("messi_goals.csv")
print(df_messi.info())

## --- Arreglar el dataset -------------------------------------------- 

# Tratar los valores nulos
print(df_messi.isnull().sum())
df_messi = df_messi.fillna("No data")

# Arreglar columnas
df_messi["Date"] = pd.to_datetime(df_messi["Date"], format="mixed")
df_messi["Minute"] = df_messi["Minute"].apply(eval)

# La columna "Season" tiene valores que no siguen un patrón como "11-Dec"
# Además algunas columnas tienen caracteres extraños, exploramos una a una:
print(df_messi["Season"].unique())
print(df_messi["Competition"].unique())
print(df_messi["Matchday"].unique())
print(df_messi["Club"].unique())
print(df_messi["Opponent"].unique())
print(df_messi["Type"].unique())
print(df_messi["Goal_assist"].unique())

str_dict = { 
            "-Dec": "/12", 
            "Dec-" : "12/",
            "Ã¡": "á",
            "Ã©": "é",
            "Ã­": "í",
            "Ã³": "ó",
            "Ãº": "ú",
            "Ã": "Á",
            "Ã‰": "É",
            "Ã": "Í",
            "Ã“": "Ó",
            "Ãš": "Ú",
            "Ã±": "ñ",
            "Ã‘": "Ñ",
            "Â¡": "¡",
            "Â¿": "¿",
            "Ã¶": "ö",
            "Ã£": "ã",
            "�": "é",
            "Fifth": "5th",
            "round": "Round",
            "final": "Final",
            "Kylian Mbappe": "Kylian Mbappé",
            "UEFA Champions League": "Champions League"
}

df_messi.replace(str_dict, regex=True, inplace=True)

## --- Estadísticas de los goles de Messi  ----------------------------

# Total de goles anotados en LaLiga
mask_competition = df_messi["Competition"] == "LaLiga"
df_laliga = df_messi.loc[mask_competition]
goles_laliga = df_laliga["GoalID"].count()
goles_total = df_messi["GoalID"].count()
print(f"Messi anotó {goles_laliga} goles en LaLiga de un total de {goles_total} goles registrados.")

# Máxima cantidad de goles en una temporada
season_max = df_messi["Season"].value_counts().idxmax()
season_goal = df_messi["Season"].value_counts().max()
print(f"En la temporada {season_max}, Messi anotó {season_goal} goles.")

# Máxima cantidad de goles en finales de competiciones
mask_matchday = df_messi["Matchday"] == "Final"
df_finals = df_messi.loc[mask_matchday]
finals_goal = df_finals["GoalID"].count()
print(f"Messi anotó {finals_goal} goles en finales.")

# El mayor asistidor de goles de Messi
mask_goalassist = df_messi["Goal_assist"].value_counts()
assist_name = mask_goalassist.index[1]
assist_goal = mask_goalassist[1]
print(f"El mayor asistidor de Messi fue {assist_name} con {assist_goal} pases.")

# Exportar el resultado a un archivo CSV
df_messi.to_csv("df_messi_output.csv", index=False)