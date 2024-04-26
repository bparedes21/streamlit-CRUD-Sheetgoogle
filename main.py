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
    initial_sidebar_state="expanded",
    show_sidebar_nav=True  # Corrected parameter name
)
st.title("Bienvenido")

page_explanations = {
    "Borrar": "Eliminar datos de la hoja de cálculo.",
    "Insertar": "Insertar nuevos datos en la hoja de cálculo.",
    "Modificar": "Modificar datos existentes en la hoja de cálculo."
}

st.sidebar.title("Navegación")
selected_page = st.sidebar.radio("Seleccionar página:", list(page_explanations.keys()))

# Display explanation for selected page
if selected_page in page_explanations:
    st.sidebar.subheader(page_explanations[selected_page])

# Display content for selected page
if selected_page == "Borrar":
    data = get_data()
    st.write(data)  # Display the fetched data
elif selected_page == "Insertar":
    st.write("You selected Insertar")
elif selected_page == "Modificar":
    st.write("You selected Modificar")
