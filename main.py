import streamlit as st
import requests
import pandas as pd

import pages.borrar as br
import pages.insertar as sr
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
# Función para modificar datos en la API
def update_data(id_value, product, price, category, discount):
    api_url = "https://python-fastapi-iamgod.koyeb.app/update/"
    url = api_url + id_value
    payload = {
        "column1": product,
        "column2": price,
        "column3": category,
        "column4": discount
    }
    
    try:
        response = requests.put(url, json=payload)
        if response.status_code == 200:
            return {"status_code": 200}
        else:
            return {"status_code": response.status_code, "message": response.text}
    except requests.RequestException as e:
        return {"status_code": 500, "message": str(e)}

def main_mr():
  
    
    data = get_data()

    st.title("MODIFICAR Datos de la tabla Productos en Google Sheets")

    id_list = data['ID'].tolist() if data is not None else []
    if id_list:
        selected_id = st.selectbox("Selecciona un ID de la tabla Productos:", id_list)
        
        # Definir los productos para cada categoría junto con sus emojis correspondientes
        productos = {
            'Almacen': [('🍝', 'Fideos'), ('🍚', 'Arroz'), ('🍅', 'Pure de Tomate')],
            'Mascotas': [('🐶', 'Alimento para perro'), ('🐱', 'Alimento para gato'), ('🐰', 'Alimento para conejo')],
            'Bebidas y bodega': [('🥤', 'Gaseosa'), ('💧', 'Agua'), ('🍷', 'Vino')]
        }
        
        st.subheader("Ingrese los datos a modificar:")
        selected_category = st.selectbox("Selecciona una categoría:", list(productos.keys()))
        productos_emojis = [producto[0] + " " + producto[1] for producto in productos[selected_category]]
        selected_product = st.selectbox("Seleccione un producto:", productos_emojis)
        selected_discount = st.selectbox("Seleccione un descuento:", ["0", "10", "20", "30"])
        selected_price = st.number_input("Ingrese un precio:", min_value=0.0, format="%.2f")

        if st.button("Modificar"):
            response = update_data(selected_id, selected_product, selected_price, selected_category, selected_discount)
            if response["status_code"] == 200:
                st.empty()
                st.success("Datos modificados exitosamente")
                data = get_data()  # Actualizar datos después de la modificación
            else:
                st.error(f"Hubo un error al modificar los datos: {response['message']}")

    else:
        st.warning("No se encontraron IDs para la categoría seleccionada.")

    if data is not None and not data.empty:
        st.subheader("Tabla Productos en Google Sheets")
        st.write(data)
    else:
        st.warning("No se encontraron datos.")


def main():
    st.set_page_config(
        page_title="Gestion de Hoja de Cálculo",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    page = st.sidebar.selectbox(
        "Seleccione una página:",
        ("","Modificar", "Borrar", "Insertar")
    )

    if page == "":
        with st.container():
            # Título en la barra lateral con tamaño de fuente reducido
            st.sidebar.title("👋 ¡Bienvenido/a!")

            st.sidebar.subheader("Navegue a través del menú:")
            page_explanations = {
                "Borrar": "Eliminar datos de la hoja de cálculo.",
                "Insertar": "Insertar nuevos datos en la hoja de cálculo.",
                "Modificar": "Modificar datos existentes en la hoja de cálculo."
            }
            st.write("# Bienvenidos a nuestro proyecto de gestión de datos 📊")
            st.write("Este proyecto tiene como objetivo facilitar la gestión de datos de una hoja de cálculo a través de una interfaz amigable y fácil de usar.")
            for page, explanation in page_explanations.items():
                st.write(f"**{page}**: {explanation}")
            data = get_data()
            st.write(data)

    elif page == "Modificar":
        main_mr()
    elif page == "Borrar":
        br
    elif page == "Insertar":
        sr

if __name__ == "__main__":
    main()
