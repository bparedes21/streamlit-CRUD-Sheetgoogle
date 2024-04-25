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

        # Obtener las categorías
        categories = ['Almacen','Mascotas','Bebidas y bodega']
        productos_Almacen = ['Fideos','Arroz','Pure de Tomate']
        productos_Mascotas = ['Alimento para perro','Alimento para gato','Alimento para conejo']
        productos_Bebidas_y_bodega = ['Gaseosa','Agua','Vino']

        st.subheader("Ingrese los datos a modificar:")
        # Crear menú desplegable con las categorías
        selected_category = st.selectbox("Selecciona una categoría:", categories)
        if selected_category == 'Almacen':
            selected_productos_Almacen = st.selectbox("Seleccione un producto:", productos_Almacen)
        elif selected_category == 'Mascotas':
            selected_productos_Mascotas = st.selectbox("Seleccione un producto:", productos_Mascotas)
        elif selected_category == 'Bebidas y bodega':
            selected_productos_Bebidas_y_bodega = st.selectbox("Seleccione un producto:", productos_Bebidas_y_bodega)


        if st.button("Modificar"):
            # Aquí puedes realizar la lógica para modificar los datos en la API
            st.success("Datos modificados exitosamente")
    else:

        # Aquí puedes realizar la lógica para modificar los datos en la API
            st.success("No hay nungun registro para modificar")
        
# Mostrar los datos en Streamlit
if data is not None and not data.empty:
    st.title("Datos de la API CRUD Google Sheets")
   
    st.write(f"Datos de la categoría '{selected_category}'")
    st.write(data)
else:
    st.warning("No se encontraron datos.")
