import requests
import streamlit as st
import pandas as pd
# URL de tu API de FastAPI
api_url = "https://python-fastapi-iamgod.koyeb.app"  # Actualiza con la URL de tu API

# Función para obtener los datos de la API
def get_data():
    try:
        response = requests.get(f"https://python-fastapi-iamgod.koyeb.app/read")
        data = response.json()

        if response.status_code == 200:
            data =data[0]
            list_data=data['data']
            df=pd.DataFrame(list_data)
            return df
        else:
            st.error(data)
            return None
    except requests.RequestException as e:
        st.error(f"Error al conectar con la API: {e}")
        return None

# Obtener los datos de la API
data = get_data()

# Mostrar los datos en Streamlit
if data:
    st.title("Datos de la API CRUD Google Sheets")
    st.write(data)
