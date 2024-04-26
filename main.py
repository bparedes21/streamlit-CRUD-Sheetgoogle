import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Gestion de Hoja de Calculo",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed",
    show_sidebar_navigation='True'
)

# Dictionary with page names and URLs
pages = {
    "Borrar": "/borrar",
    "Insertar": "/insertar",
    "Modificar": "/modificar"
}

# Display navigation menu
st.sidebar.title("Navegación")