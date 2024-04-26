

    

import streamlit as st
import pages.modificar
import pages.insertar
import pages.borrar
# Set page configuration
st.set_page_config(
    page_title="Gestion de Hoja de Calculo",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Display navigation menu
st.sidebar.title("Navegación")

selected_page = st.sidebar.radio("Seleccionar página:", ["Borrar", "Insertar", "Modificar"])

if selected_page == "Borrar":
    pages.borrar.show_page()
elif selected_page == "Insertar":
    pages.insertar.show_page()
elif selected_page == "Modificar":
    pages.modificar.show_page()