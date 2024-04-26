import streamlit as st

st.set_page_config(
    page_title="Gestion de Hoja de Calculo",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    show_sidebar_navigation=False
)
# Dictionary with page names and URLs
pages = {
    "Borrar": "/borrar",
    "Insertar": "/insertar",
    "Modificar": "/modificar"
}

# Display navigation menu
st.sidebar.title("Navegación")

for page_name, page_url in pages.items():
    st.sidebar.markdown(f"[{page_name}]({page_url})")