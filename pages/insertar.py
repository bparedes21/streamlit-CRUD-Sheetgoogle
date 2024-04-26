import requests
import streamlit as st
import pandas as pd

from pages.funciones_crud import get_data

def insert_data(product, price, category, discount):
    url = "https://python-fastapi-iamgod.koyeb.app/insert"
    payload = {
        "column1": product,
        "column2": price,
        "column3": category,
        "column4": discount
    }
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Verificar si hay errores en la respuesta
        data = response.json()
        # Resto del código para procesar la respuesta
        return data
    except requests.RequestException as e:
        
        return None
# Obtener los datos de la API
data = get_data()

st.title("INSERTAR Datos de la tabla Productos en Google Sheets")
  
categories = ['Almacen','Mascotas','Bebidas y bodega']
productos_Almacen = ['Fideos','Arroz','Pure de Tomate']
productos_Mascotas = ['Alimento para perro','Alimento para gato','Alimento para conejo']
productos_Bebidas_y_bodega = ['Gaseosa','Agua','Vino']

st.subheader("Ingrese los datos:")
# Crear menú desplegable con las categorías
selected_category = st.selectbox("Selecciona una categoría:", categories)
if selected_category == 'Almacen':
    selected_productos = st.selectbox("Seleccione un producto:", productos_Almacen)
elif selected_category == 'Mascotas':
    selected_productos = st.selectbox("Seleccione un producto:", productos_Mascotas)
elif selected_category == 'Bebidas y bodega':
    selected_productos = st.selectbox("Seleccione un producto:", productos_Bebidas_y_bodega)
descuento = ["0","10","20","30"]
selected_descuento = st.selectbox("Seleccione un descuento:", descuento)
selected_descuento_str=str(selected_descuento)
precio = st.text_input("Ingresar precio:")
precio_str=str(precio)
st.write("Precio ingresado:", selected_category,selected_productos,precio_str,selected_descuento_str)

if st.button("insertar"):# Verificar tipos de datos

    response = insert_data(selected_productos, precio_str, selected_category , selected_descuento_str)
    
    if response[1] == 200:
        st.empty()
        data = get_data()
        st.success("Datos insertados exitosamente")
    else:
        st.error(f"Hubo un error al insertar los datos: {response.text}")


# Mostrar los datos en Streamlit
if data is not None and not data.empty:
    st.subheader("Tabla Productos en Google Sheets")
    st.write(data)
else:
    st.warning("No se encontraron datos.")
