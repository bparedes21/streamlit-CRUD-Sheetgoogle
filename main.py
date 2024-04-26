import requests
import streamlit as st
import pages.modificar
import pages.insertar
import pages.borrar


st.title("Elegir una opcion: 'insertar','borrar' o 'modificar")
# Obtener las categorías
opcion_crud = ['','insertar','borrar','modificar']

# Crear menú desplegable con las categorías
selected_opcion_crud = st.selectbox("Opcion Sheet:", opcion_crud)

    # Redirigir a la página correspondiente
if selected_opcion_crud == 'insertar':
    pages.insertar.show_page()
elif selected_opcion_crud == 'borrar':
    pages.borrar.show_page()
elif selected_opcion_crud == 'modificar':
    st.write("Página de modificar")
    # Redireccionar a la página de modificar
    pages.modificar.show_page()