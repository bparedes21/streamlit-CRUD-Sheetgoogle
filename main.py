import streamlit as st

import pages.borrar
import pages.insertar
import pages.modificar

# Create a sidebar with options for the pages
selected_page = st.sidebar.radio("Seleccionar página:", ["Borrar", "Insertar", "Modificar"])


if selected_page == "Borrar":
    pages.borrar.show()
elif selected_page == "Insertar":
    pages.insertar.show()
elif selected_page == "Modificar":
    pages.modificar.show()
