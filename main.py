import streamlit as st
import streamlit.components.v1 as components
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

def main():
    st.title("Navegación entre páginas en Streamlit")
    # Configuración de la página
    st.set_page_config(
        page_title="Gestion de Hoja de Cálculo",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Define el encabezado
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

    # Botón para cargar la página modificar.py
    if st.button("Ir a la página 'Modificar'"):
        load_page("modificar.py")

def load_page(page_name):
    with open(page_name, "r") as file:
        page_code = file.read()
    components.html(page_code, width=1000, height=800, scrolling=True)

if __name__ == "__main__":
    main()


