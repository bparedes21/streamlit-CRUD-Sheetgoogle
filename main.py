import streamlit as st
from pages import borrar, insertar, modificar

# Function to display the selected page
def display_page(page_name):
    if page_name == "Borrar":
        borrar.show()
    elif page_name == "Insertar":
        insertar.show()
    elif page_name == "Modificar":
        modificar.show()

# Set page configuration
st.set_page_config(
    page_title="Gestión de Hoja de Cálculo",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Create a sidebar with menu items
selected_page = st.sidebar.radio("Seleccionar página:", ["Borrar", "Insertar", "Modificar"])

# Display the selected page
display_page(selected_page)
