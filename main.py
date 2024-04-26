import streamlit as st
import pages.modificar as md

def main():
    st.set_page_config(
        page_title="Gestion de Hoja de Cálculo",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    md.main()

if __name__ == "__main__":
    main()
