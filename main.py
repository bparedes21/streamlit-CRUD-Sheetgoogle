import streamlit as st

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
    st.write("You selected Borrar")
elif selected_page == "Insertar":
    st.write("You selected Insertar")
elif selected_page == "Modificar":
    st.write("You selected Modificar")