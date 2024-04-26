import requests
import streamlit as st
import pandas as pd
# Función para obtener los datos de la API
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


def delete_row(id):
    url = f"https://python-fastapi-iamgod.koyeb.app/delete/{id}"
    response = requests.delete(url)
    return response