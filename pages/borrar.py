import streamlit as st
import requests
import pandas as pd
from pages.funciones_crud import get_data, delete_row

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
    
    try:
        response = requests.delete(url)
        if response.status_code == 200:
            return f"La fila con ID {id} fue eliminada exitosamente."
        else:
            return f"Error al eliminar la fila con ID {id}. Estado de la respuesta: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Error de conexión: {e}"
        
# Obtener los datos de la API
data = get_data()
st.title("BORRAR Datos de la tabla Productos en Google Sheets")
# Obtener la lista de valores de la columna "ID"
id_list = data['ID'].tolist()
if len(id_list)!=0:
    selected_id_list= st.selectbox("Selecciona un ID de la tabla Productos:", id_list)  
    # Botón para enviar el ID a eliminar
    if st.button("Eliminar"):
        response =  delete_row(selected_id_list)
        data = get_data()
        if response.status_code == 200:
            st.success("Registro eliminado exitosamente")
        else:
            st.error(f"Hubo un error al eliminar el registro: {response.json()['message']}")
    
else:

    st.warning("No se encontraron IDs para la categoría seleccionada.")

# Mostrar los datos en Streamlit
if data is not None and not data.empty:
    st.subheader("Tabla Productos en Google Sheets")
    st.write(data)
else:
    st.warning("No se encontraron datos.")