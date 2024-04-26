from .pages.funciones_crud import *
import streamlit as st


# Set page configuration
st.set_page_config(
    page_title="Gestion de Hoja de Calculo",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="auto",
    show_sidebar_navigation=True  # To show the sidebar navigation
)

selected_page = st.sidebar.radio("Seleccionar página:", ["Borrar", "Insertar", "Modificar"], index=-1)

# Display navigation menu
st.sidebar.title("Navegación")
# Display content for selected page
if selected_page == "Borrar":
    data = get_data()
    cuerpo_insertar(data)
elif selected_page == "Insertar":
    st.write("You selected Insertar")
elif selected_page == "Modificar":
    st.write("You selected Modificar")
# Obtener los datos de la API
