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

st.title("Bienvenido")

page_explanations = {
    "Borrar": "Eliminar datos de la hoja de cálculo.",
    "Insertar": "Insertar nuevos datos en la hoja de cálculo.",
    "Modificar": "Modificar datos existentes en la hoja de cálculo."
}

for page, explanation in page_explanations.items():
    st.write(f"{page}: {explanation}")




data = get_data()
st.write(data)