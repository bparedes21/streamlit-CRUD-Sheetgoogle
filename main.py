import requests
import streamlit as st
import pandas as pd
import pages.modificar
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


# Función para realizar la solicitud POST al endpoint de actualización
def update_data(id_value, category, product, price, discount):
    url = "https://python-fastapi-iamgod.koyeb.app/update/" + id_value
    payload = {
        "column1": category,
        "column2": product,
        "column3": price,
        "column4": discount
    }
    response = requests.put(url, json=payload)
    return response

# Obtener los datos de la API
data = get_data()

# Obtener las categorías
opcion_crud = ['','insertar','borrar','modificar']

# Crear menú desplegable con las categorías
selected_opcion_crud = st.selectbox("Opcion Sheet:", opcion_crud)

    # Redirigir a la página correspondiente
if selected_opcion_crud == 'insertar':
    pages.leer.show_page()
elif selected_opcion_crud == 'borrar':
    pages.leer.show_page()
elif selected_opcion_crud == 'modificar':
    st.write("Página de modificar")
    # Redireccionar a la página de modificar
    pages.modificar.show_page()