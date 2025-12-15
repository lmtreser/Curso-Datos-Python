# Introducción a Streamlit
# Bloque 2: Diseño, Interactividad y Estado
# Prof. Lucas Martín Treser

import streamlit as st
import time

# Títulos y texto
st.title("Titulo")
st.header("Encabezado")
st.subheader("Subencabezado")
st.text("Texto simple")
st.write("¡Hola, Mundo!")
st.markdown("**Texto en negrita**")

# Entrada de texto
nombre = st.text_input("Ingresar nombre:")
st.write(f"Texto ingresado: {nombre}")

# Botón
if st.button("Enviar"):  
    st.write("Press!")

# Deslizador
edad = st.slider("Seleccionar edad:", 0, 100, 25)

# Selector dinámicos
color = st.selectbox("Elegir un color:", ["Rojo", "Verde", "Azul"])

# Selectores dinámicos
opciones = ['Opción 1', 'Opción 2', 'Opción 3']
seleccion = st.selectbox('Elegir una opción', opciones)
st.write(f'Opción elegida: {seleccion}')

# Checkbox
check = st.checkbox("Tildar opción")
if check:
    st.text("Opción marcada")
    
# Radio
radio = st.radio("Elegir una opción:", ["Opción 1", "Opción 2", "Opción 3"])

options = ["Opción 1", "Opción 2", "Opción 3", "Opción 4"]
selection = st.segmented_control(
                                 "Filtrar:", options, default="Opción 1", 
                                 selection_mode="single"
                                 )

# Emojis
st.write("Es posible utilizar emojis: 😍 🐈")
        
# Imagenes
st.image("lamp.svg", width=50)

# Archivos
archivo = st.file_uploader("Subir un archivo CSV")  
if archivo:
    st.write("Archivo subido")

# Barra de progreso animada
progress = st.progress(0)
for i in range(100):
    time.sleep(0.1)
    progress.progress(i + 1)