import requests
import streamlit as st
import pandas as pd

# URL de tu API de FastAPI
api_url = "https://python-fastapi-iamgod.koyeb.app"  # Actualiza con la URL de tu API

# Función para obtener los datos de la API
def get_data():
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

# Obtener los datos de la API
data = get_data()

# Obtener las categorías
categories = ['Almacen','Mascotas','Bebidas y bodega']

# Crear menú desplegable con las categorías
selected_category = st.selectbox("Selecciona una categoría:", categories)
# Mostrar los datos en Streamlit
if data is not None and not data.empty:
    st.title("Datos de la API CRUD Google Sheets")
   
    st.write(f"Datos de la categoría '{selected_category}'")
    st.write(data)
else:
    st.warning("No se encontraron datos.")
