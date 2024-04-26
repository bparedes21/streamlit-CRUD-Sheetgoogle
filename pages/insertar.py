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


        
def main_sr():
    st.set_page_config(
    page_title="Gestion de Hoja de Cálculo",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
    )

    data = get_data()
    st.title("📝 INSERTAR Datos de la tabla Productos en Google Sheets")

    categories = ['Almacen', 'Mascotas', 'Bebidas y bodega']

    # Definir los productos para cada categoría junto con sus emojis correspondientes
    productos = {
        'Almacen': [('🍝', 'Fideos'), ('🍚', 'Arroz'), ('🍅', 'Pure de Tomate')],
        'Mascotas': [('🐶', 'Alimento para perro'), ('🐱', 'Alimento para gato'), ('🐰', 'Alimento para conejo')],
        'Bebidas y bodega': [('🥤', 'Gaseosa'), ('💧', 'Agua'), ('🍷', 'Vino')]
    }

    st.subheader("Ingrese los datos:")
    # Crear menú desplegable con las categorías
    selected_category = st.selectbox("Selecciona una categoría:", categories)

    productos_emojis = [producto[0] + " " + producto[1] for producto in productos[selected_category]]
    productos_sin_emojis = [producto[1] for producto in productos[selected_category]]

    # Crear el selectbox para los productos
    selected_productos = st.selectbox("Seleccione un producto:", productos_emojis)

    # Obtener el producto sin emojis correspondiente al seleccionado
    selected_producto_sin_emojis = productos_sin_emojis[productos_emojis.index(selected_productos)]

    descuento = ["0", "10", "20", "30"]
    selected_descuento = st.selectbox("Seleccione un descuento:", descuento)

    precio = st.number_input('Ingrese un precio:', min_value=0.0, format="%.2f")
    # Asegurarse de que el valor se trate como un flotante
    precio = round(float(precio), 2)
    precio_str = str(precio)

    # Obtener emoji correspondiente a la categoría seleccionada
    category_emoji = {
        'Almacen': '🏬',
        'Mascotas': '🐾',
        'Bebidas y bodega': '🍷'
    }
    st.subheader("Datos:")
    st.write("Producto:", selected_productos)
    st.write("Precio:", precio_str)
    st.write("Categoría:", category_emoji[selected_category], selected_category)
    st.write("Descuento:", selected_descuento)
    if st.button("insertar"):# Verificar tipos de datos

        response = insert_data(selected_producto_sin_emojis, precio_str , selected_category , selected_descuento)
        
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

