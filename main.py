import streamlit as st
import pages.modificar as md
import pages.borrar as br
import pages.insertar as sr

def main():
    st.set_page_config(
        page_title="Gestion de Hoja de Cálculo",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    page = st.sidebar.selectbox(
        "Seleccione una página:",
        ("Modificar", "Borrar", "Insertar")
    )

    if page == "Modificar":
        md.main()
    elif page == "Borrar":
        br.main()
    elif page == "Insertar":
        sr.main()

if __name__ == "__main__":
    main()
