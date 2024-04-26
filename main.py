import requests
import streamlit as st
import pages.modificar
import pages.insertar
import pages.borrar


st.title("Elegir una opcion: 'insertar','borrar' o 'modificar")
# Obtener las categorías

# Create a sidebar with options for the pages
selected_page = st.sidebar.radio("Seleccionar página:", ["Modificar", "Insertar", "Borrar"])


    # Redirigir a la página correspondiente
if selected_page == 'Insertar':
    pages.insertar.show_page()
elif selected_page == 'Borrar':
    pages.borrar.show_page()
elif selected_page == 'Modificar':
    pages.modificar.show_page()