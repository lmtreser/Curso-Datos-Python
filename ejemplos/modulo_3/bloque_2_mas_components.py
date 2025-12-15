# Introducción a Streamlit
# Bloque 2: Diseño, Interactividad y Estado
# Prof. Lucas Martín Treser

import streamlit as st

# Título y texto
st.title("¡Hola, Mundo!")
st.write("Primera aplicación interactiva.")

# Encabezados y texto
st.header("Encabezado")
st.subheader("Subencabezado")
st.text("Texto simple")
st.markdown("**Texto en negrita**, *texto en cursiva*")

# Widgets interactivos

# Imágenes, audio y video
# st.image("kid.jpg")
# st.audio("Audio.mp3")
# st.video("video.mp4")

# Botones
if st.button("Haz clic aquí"):
    st.write("¡Botón presionado!")

# Sliders
edad = st.slider("Selecciona tu edad", 0, 100, 25)
st.write(f"Tienes {edad} años.")

# Selectores
st.select_slider("Seleccionar", ["Malo", "Bueno", "Excelente"])
st.checkbox("Check Box")
st.radio("Radio",["Opción 1","Opción 2"])
st.selectbox("Select Box",["True","False"])
st.multiselect("Multi Select",["Jupiter", "Marte", "Neptuno"])

# Input de texto
nombre = st.text_input("¿Cuál es tu nombre?")
st.write(f"Hola, {nombre}")

st.text_area("Descripción")
st.number_input("Elegir un número", 0,10)
st.date_input("Elegir una fecha")
st.time_input("Entrada de tiempo")
st.file_uploader("Subir archivo")
st.color_picker("Elección de color")

# Mostrar progreso
st.progress(10)

# Mostrar spinner
st.balloons()

# Esperar
with st.spinner("Wait for it..."):
    import time
    time.sleep(1)

# Mostrar mensajes
st.success("You did it !")
st.error("Error")
st.warning("Warning")
st.info("It's easy to build a streamlit app")
st.exception(RuntimeError("RuntimeError exception"))

# Graficar con matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig)

# Mostrar tablas
import pandas as pd

datos = pd.DataFrame({
    "Columna A": [1, 2, 3, 4],
    "Columna B": [5, 6, 7, 8]
})
st.dataframe(datos)

# Cargar archivos
archivo = st.file_uploader("Sube un archivo CSV", type=["csv"])
if archivo is not None:
    datos = pd.read_csv(archivo)
    st.dataframe(datos)