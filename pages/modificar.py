import requests
import streamlit as st
import pandas as pd
from pages.funciones_crud import get_data, update_data


def update_data(id_value, product, price, category, discount):
    # URL of your FastAPI API
    api_url = "https://python-fastapi-iamgod.koyeb.app/update/"  # Update with your API URL
    url = api_url + id_value
    payload = {
        "column1": product,
        "column2": price,
        "column3": category,
        "column4": discount
    }
    
    try:
        response = requests.put(url, json=payload)
        response.raise_for_status()  # Check for errors in the response
        data = response.json()
        return data

    except requests.RequestException as e:
        # Log the error
        print(f"Error updating data: {e}")
        return None


data=pd.DataFrame()
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
    descuento = ["0","10","20","30"]
    selected_descuento = st.selectbox("Seleccione un descuento:", descuento)

    precio = st.number_input ('Ingrese un precio:', min_value=0, format="%d")

    precio_str=str(precio)
    selected_id_list_str=str(selected_id_list)
    
    st.write("Id:", selected_id_list_str)
    st.write("Producto:", selected_productos)
    st.write("Precio:", precio_str)
    st.write("Categoría:", selected_category)
    st.write("Descuento:", selected_descuento)
    
    if st.button("Modificar"):
        response = update_data(selected_id_list_str,selected_productos, precio_str , selected_category , selected_descuento)
        if 'status_code' in response and response['status_code'] == 200:

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
    
    st.subheader("Tabla Productos en Google Sheets")
    st.write(data)
else:
    st.warning("No se encontraron datos.")
