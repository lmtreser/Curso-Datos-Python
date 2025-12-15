# Introducción a Streamlit
# Bloque 1: Introducción a Streamlit
# Prof. Lucas Martín Treser

import streamlit as st

# Configurar la página
st.set_page_config(
    page_title="Titulo de la App",
    page_icon="🌐",
    initial_sidebar_state="collapsed"
    )

st.title("¡Hola, Mundo!")
st.write("Esta es una primera aplicación")

# Input de texto
nombre = st.text_input("¿Cuál es tu nombre?")
st.write(f"Hola, {nombre}")

# Botones
if st.button("Haz clic aquí"):
    st.write("¡Botón presionado!")

# Sliders
edad = st.slider("Selecciona tu edad", 0, 100, 25)
st.write(f"Tenes {edad} años.")