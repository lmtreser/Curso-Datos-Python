# Introducción a Streamlit
# Bloque 2: Diseño, Interactividad y Estado
# Prof. Lucas Martín Treser

import streamlit as st

# Crear columnas
col1, col2, col3 = st.columns(3, gap="small", vertical_alignment="top", border=True)

# Añadir contenido a cada columna
col1.header("Columna 1")
col1.write("Contenido de la primera columna.")
col2.header("Columna 2")
col2.button("Botón en columna 2")
col3.header("Columna 3")
col3.write("Texto en la tercera columna.")

st.divider()

# Ajustar el tamaño relativo de las columnas especificando proporciones
col4, col5 = st.columns([1, 2])  # col5 será más ancha que col1

col4.header("Columna 4")
col4.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam nec purus nec nunc")
col5.header("Columna 5")
col5.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam nec purus nec nunc")

st.divider()

# Usar notación "with" para insertar elementos en las columnas
# De está manera el código es más limpio y legible, ya que no es necesario repetir
# col6. o col7. antes de cada instrucción. El bloque "with" indica claramente qué 
# contenido pertenece a cada columna.
col6, col7 = st.columns(2)

with col6:
    st.header("Columna 6")
    st.write("Contenido de la columna 6")
with col7:
    st.header("Columna 7")
    st.write("Contenido de la columna 7")

st.divider()

# Usar pestañas para organizar el contenido
tab1, tab2, tab3 = st.tabs(["Pestaña 1", "Pestaña 2", "Pestaña 3"])

with tab1:
    st.write("Contenido de la pestaña 1")
with tab2:
    st.write("Contenido de la pestaña 2")
with tab3:
    st.write("Contenido de la pestaña 3")
    
st.divider()

# Usar contenedores con borde
with st.container(border=True):
    st.write("Contenido dentro del contenedor")
    st.write("Contenido dentro del contenedor")
st.write("Contenido fuera del contenedor")

st.divider()

# Usar expansores
with st.expander("Haz clic aquí para expandir"):
    st.write("Contenido del expansor")

st.divider()

# Sidebar
with st.sidebar:
    st.header("Opciones")
    opcion = st.radio("Escoge una opción:", ["A", "B", "C"])
    st.write(f"Opción seleccionada: {opcion}")
    
# Almacenar datos en la sesión
if "contador" not in st.session_state:
    st.session_state.contador = 0

if st.button("Incrementar"):
    st.session_state.contador += 1

st.write(f"Contador: {st.session_state.contador}")