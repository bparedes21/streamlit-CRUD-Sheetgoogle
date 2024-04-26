import streamlit as st


# Dictionary with page names and URLs
pages = {
    "Borrar": "/borrar",
    "Insertar": "/insertar",
    "Modificar": "/modificar"
}

# Display navigation menu
st.sidebar.title("Navegación")

for page_name, page_url in pages.items():
    st.sidebar.markdown(f"[{page_name}]({page_url})")