import streamlit as st
import streamlit.components.v1 as components

def main():
    st.title("Navegación entre páginas en Streamlit")

    # Botón para cargar la página modificar.py
    if st.button("Ir a la página 'Modificar'"):
        load_page("pages/modificar.py")

def load_page(page_name):
    with open(page_name, "r") as file:
        page_code = file.read()
    components.html(page_code, width=1000, height=800, scrolling=True)

if __name__ == "__main__":
    main()



