import requests
import streamlit as st
import pandas as pd
from funciones_crud import get_data, update_data

# Obtener los datos de la API
data = get_data()
st.title("MODIFICAR Datos de la tabla Productos en Google Sheets")
# Obtener la lista de valores de la columna "ID"
id_list = data['ID'].tolist()
if len(id_list)!=0:
    selected_id_list= st.selectbox("Selecciona un ID de la tabla Productos:", id_list)    
    # Obtener las categorías
    categories = ['Almacen','Mascotas','Bebidas y bodega']
    productos_Almacen = ['Fideos','Arroz','Pure de Tomate']
    productos_Mascotas = ['Alimento para perro','Alimento para gato','Alimento para conejo']
    productos_Bebidas_y_bodega = ['Gaseosa','Agua','Vino']

    st.subheader("Ingrese los datos a modificar:")
    # Crear menú desplegable con las categorías
    selected_category = st.selectbox("Selecciona una categoría:", categories)
    if selected_category == 'Almacen':
        selected_productos = st.selectbox("Seleccione un producto:", productos_Almacen)
    elif selected_category == 'Mascotas':
        selected_productos = st.selectbox("Seleccione un producto:", productos_Mascotas)
    elif selected_category == 'Bebidas y bodega':
        selected_productos = st.selectbox("Seleccione un producto:", productos_Bebidas_y_bodega)
    descuento = ['0','10','20','30']
    selected_descuento = st.selectbox("Seleccione un descuento:", descuento)
    precio = st.text_input("Ingresar precio:")

    if st.button("Modificar"):
        response = update_data(selected_id_list, selected_category, selected_productos, precio, selected_descuento)
        if response.status_code == 200:
            
            st.empty()
            data = get_data()
            st.success("Datos modificados exitosamente")
        else:
            st.error(f"Hubo un error al modificar los datos")

        # Limpiar el contenido actual

else:

    st.warning("No se encontraron IDs para la categoría seleccionada.")


# Mostrar los datos en Streamlit
if data is not None and not data.empty:

    st.title("Tabla Productos Google Sheets")
    st.write(data)
else:
    st.warning("No se encontraron datos.")
