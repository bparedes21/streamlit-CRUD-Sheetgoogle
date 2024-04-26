import streamlit as st
import os

def main():
    st.set_page_config(
        page_title="Gestion de Hoja de Cálculo",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    load_page("pages/modificar.py")

def load_page(page_name):
    page_path = os.path.join(os.getcwd(), page_name)
    with open(page_path, "r") as file:
        code = file.read()
    exec(code)

if __name__ == "__main__":
    main()
