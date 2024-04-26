import streamlit as st
import requests
import pandas as pd

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
        response.raise_for_status()  # Check for errors in the response
        data = response.json()
        return data
  
    except requests.RequestException as e:
        # Log the error
        print(f"Error inserting data: {e}")
        return None


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

precio = st.number_input ('Ingrese un precio:', min_value=0.0, format="%.2f")
# Ensure the value is treated as a float
precio = round(float(precio), 2)
precio_str=str(precio)
st.write("Producto:", selected_productos)
st.write("Precio:", precio_str)
st.write("Categoría:", selected_category)
st.write("Descuento:", selected_descuento)

if st.button("insertar"):# Verificar tipos de datos

    response = insert_data(selected_productos, precio_str , selected_category , selected_descuento)
    
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
