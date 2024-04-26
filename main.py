import streamlit as st

from pages import borrar, insertar, modificar
# Create a sidebar with options for the pages
selected_page = st.sidebar.radio("Seleccionar página:", ["Borrar", "Insertar", "Modificar"])


if selected_page == "Borrar":
    borrar.show()
elif selected_page == "Insertar":
    insertar.show()
elif selected_page == "Modificar":
    modificar.show()
