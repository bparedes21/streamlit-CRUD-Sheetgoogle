import requests
import streamlit as st
import pandas as pd
from .funciones_crud import get_data, delete_row

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
    st.title("Tabla Productos Google Sheets")
    st.write(data)
else:
    st.warning("No se encontraron datos.")