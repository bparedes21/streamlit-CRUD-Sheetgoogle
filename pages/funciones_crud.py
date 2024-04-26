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

# Función para realizar la solicitud POST al endpoint de actualización
def update_data(id_value, category, product, price, discount):
    # URL de tu API de FastAPI
    api_url = "https://python-fastapi-iamgod.koyeb.app/update/"  # Actualiza con la URL de tu API
    url = api_url + {id_value}
    payload = {
        "column1": product,
        "column2": price,
        "column3": category,
        "column4": discount
    }
    response = requests.put(url, json=payload)
    return response

# Función para realizar la solicitud POST al endpoint de inserción
def insert_data(product, price, category, discount):
    url = "https://python-fastapi-iamgod.koyeb.app/insert"
    payload = {
        "column1": product,
        "column2": price,
        "column3": category,
        "column4": discount
    }
    response = requests.post(url, json=payload)
    return response

def delete_row(id):
    url = f"https://python-fastapi-iamgod.koyeb.app/delete/{id}"
    response = requests.delete(url)
    return response