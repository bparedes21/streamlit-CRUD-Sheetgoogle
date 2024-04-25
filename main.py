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

# Mostrar los datos en Streamlit
if selected_opcion_crud == 'modificar':

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
    st.title("Datos de la API CRUD Google Sheets")
    st.write(data)
else:
    st.warning("No se encontraron datos.")
