import streamlit as st
import requests
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="Gestion de Hoja de Calculo",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    show_sidebar_nav=False  # Corrected parameter name
)
st.title("Bienvenido")

