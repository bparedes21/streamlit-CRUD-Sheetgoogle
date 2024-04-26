import streamlit as st
import requests
import pandas as pd
def get_data():
        # URL de tu API de FastAPI
    api_url = "https://python-fastapi-iamgod.koyeb.app"  # Actualiza con la URL de tu API

    try:
        response = requests.get(f"{api_url}/read")
        data = response.json()

        if response.status_code == 200:
            data = data[0]
            list_data = data['data']
            df = pd.DataFrame(list_data)
            return df
        else:
            st.error(data)
            return None
    except requests.RequestException as e:
        st.error(f"Error al conectar con la API: {e}")
        return None
# Set page configuration
st.set_page_config(
    page_title="Gestion de Hoja de Calculo",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define el encabezado
with st.container():
    # Set title in the sidebar with reduced font size
    st.sidebar.title("Bievenido/a")

    st.sidebar.subheader("Navege a través del menú:")
    page_explanations = {
        "Borrar": "Eliminar datos de la hoja de cálculo.",
        "Insertar": "Insertar nuevos datos en la hoja de cálculo.",
        "Modificar": "Modificar datos existentes en la hoja de cálculo."
    }
    st.write("# Bienvenidos a nuestro proyecto de gestión de datos")
    st.write("Este proyecto tiene como objetivo facilitar la gestión de datos de una hoja de cálculo a través de una interfaz amigable y fácil de usar.")
    for page, explanation in page_explanations.items():
        st.write(f"{page}: {explanation}")
    data = get_data()
    st.write(data)