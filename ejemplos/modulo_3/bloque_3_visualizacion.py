# Introducción a Streamlit
# Bloque 3: Visualización de Datos
# Prof. Lucas Martín Treser

import pandas as pd
import streamlit as st

# Cargar los datos con cache para mejorar rendimiento
@st.cache_data(show_spinner=True)
def load_data():
    return pd.read_csv("dataset.csv")

data = load_data()

# Mostrar los primeros registros
st.write("Vista previa de los datos:")
st.write(data.head())

# Gráfico de área para visualizar tendencias de temperatura
# st.line_chart(data=None, *, x=None, y=None, x_label=None, y_label=None, color=None, 
#               width=None, height=None, use_container_width=True)
st.write("Gráfico de área")
st.area_chart(data["sensor_temperatura"], use_container_width=True)

# Gráfico de barras para contar el estado de los actuadores
# st.bar_chart(data=None, *, x=None, y=None, x_label=None, y_label=None, color=None, 
#              horizontal=False, stack=None, width=None, height=None, use_container_width=True)
st.write("Gráfico de barras")
st.bar_chart(data["actuador_luces"].value_counts(), use_container_width=True)

# Gráfico de líneas para visualizar la evolución de la humedad
# st.line_chart(data=None, *, x=None, y=None, x_label=None, y_label=None, color=None, 
#               width=None, height=None, use_container_width=True)
st.write("Gráfico de líneas")
st.line_chart(data, x="fecha", y="sensor_humedad", use_container_width=True)

# Gráfico de dispersión (Scatter Plot), relación entre temperatura y humedad
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=data["sensor_temperatura"],
    y=data["sensor_humedad"],
    mode="markers",
    marker=dict(color=data["sensor_luz"], colorscale="Viridis", size=5),
    name="Sensores"
))

fig.update_layout(title="Relación entre Temperatura y Humedad",
                  xaxis_title="Temperatura (C)",
                  yaxis_title="Humedad (%)")
st.plotly_chart(fig)

# Gráfico de indicador (Gauge), visualizar promedio de temperatura
avg_temp = data["sensor_temperatura"].mean()

fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=avg_temp,
    title={"text": "Temperatura Promedio"},
    gauge={"axis": {"range": [0, 40]}, "bar": {"color": "blue"}}
))
st.plotly_chart(fig)