import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def get_data():
    # URL de tu API de FastAPI
    api_url = "https://zippy-angelina-iamgod-54e12d2b.koyeb.app"  # Actualiza con la URL de tu API

    try:
        response = requests.get(f"{api_url}/read")
        data = response.json()

        if response.status_code == 200:
            data = data[0]
            if data is not None:
                list_data = data.get('data')
                if list_data:
                    df = pd.DataFrame(list_data)
                    return df
                else:
                    error_message = "No hay datos en la tabla"
                    return None, error_message
            else:
                error_message = "La respuesta de la API está vacía"
                return None, error_message
        else:
            error_message = f"Error al obtener datos: {response.status_code}"
            return None, error_message
    except requests.RequestException as e:
        error_message = f"Error al conectar con la API: {e}"
        return None, error_message

    
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
            return {"status_code": response.status_code}
    except requests.RequestException as e:
        return {"status_code": 500, "message": str(e)}

def main_mr():
    
    data = get_data()

    st.title("MODIFICAR Datos de la tabla Productos en Google Sheets")

    if data is not None and isinstance(data, pd.DataFrame):
        id_list = data['ID'].tolist()
    
        selected_id = st.selectbox("Selecciona un ID de la tabla Productos:", id_list)
        
        categories = ['Almacen', 'Mascotas', 'Bebidas y bodega']

        # Definir los productos para cada categoría junto con sus emojis correspondientes
        productos = {
            'Almacen': [('🍝', 'Fideos'), ('🍚', 'Arroz'), ('🍅', 'Pure de Tomate')],
            'Mascotas': [('🐶', 'Alimento para perro'), ('🐱', 'Alimento para gato'), ('🐰', 'Alimento para conejo')],
            'Bebidas y bodega': [('🥤', 'Gaseosa'), ('💧', 'Agua'), ('🍷', 'Vino')]
        }

        st.subheader("Ingrese los datos:")
        # Crear menú desplegable con las categorías
        selected_category = st.selectbox("Selecciona una categoría:", categories)

        productos_emojis = [producto[0] + " " + producto[1] for producto in productos[selected_category]]
        productos_sin_emojis = [producto[1] for producto in productos[selected_category]]

        # Crear el selectbox para los productos
        selected_productos = st.selectbox("Seleccione un producto:", productos_emojis)

        # Obtener el producto sin emojis correspondiente al seleccionado
        selected_producto_sin_emojis = productos_sin_emojis[productos_emojis.index(selected_productos)]

        cantidad = st.number_input('Ingrese una Cantidad:', min_value=0, step=1)

        precio = st.number_input('Ingrese un precio:', min_value=0.0, format="%.2f")
        
  

        # Obtener emoji correspondiente a la categoría seleccionada
        category_emoji = {
            'Almacen': '🏬',
            'Mascotas': '🐾',
            'Bebidas y bodega': '🍷'
        }
        st.subheader("Datos:")
        st.write("Producto:", selected_productos)
        st.write("Precio:", precio)
        st.write("Categoría:", category_emoji[selected_category], selected_category)
        st.write("Cantidad:", cantidad)

        if st.button("Modificar"):
            response = update_data(selected_id, selected_producto_sin_emojis, precio, selected_category, cantidad)
            if response["status_code"] == 200:
                st.empty()
                st.success("Datos modificados exitosamente")
                data = get_data()  # Actualizar datos después de la modificación
            else:
                st.error(f"Hubo un error al modificar los datos: {response['message']}")


    st.write(data)

def insert_data(product, price, category, discount):
    url = "https://python-fastapi-iamgod.koyeb.app/insert"
    payload = {
        "column1": product,
        "column2": price,
        "column3": category,
        "column4": discount
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Check for errors in the response
        data = response.json()
        return data

    except requests.RequestException as e:
        # Log the error
        print(f"Error inserting data: {e}")
        return None

def main_sr():

    data = get_data()
    st.title("📝 INSERTAR Datos de la tabla Productos en Google Sheets")

    categories = ['Almacen', 'Mascotas', 'Bebidas y bodega']

    # Definir los productos para cada categoría junto con sus emojis correspondientes
    productos = {
        'Almacen': [('🍝', 'Fideos'), ('🍚', 'Arroz'), ('🍅', 'Pure de Tomate')],
        'Mascotas': [('🐶', 'Alimento para perro'), ('🐱', 'Alimento para gato'), ('🐰', 'Alimento para conejo')],
        'Bebidas y bodega': [('🥤', 'Gaseosa'), ('💧', 'Agua'), ('🍷', 'Vino')]
    }

    st.subheader("Ingrese los datos:")
    # Crear menú desplegable con las categorías
    selected_category = st.selectbox("Selecciona una categoría:", categories)

    productos_emojis = [producto[0] + " " + producto[1] for producto in productos[selected_category]]
    productos_sin_emojis = [producto[1] for producto in productos[selected_category]]

    # Crear el selectbox para los productos
    selected_productos = st.selectbox("Seleccione un producto:", productos_emojis)

    # Obtener el producto sin emojis correspondiente al seleccionado
    selected_producto_sin_emojis = productos_sin_emojis[productos_emojis.index(selected_productos)]

    cantidad = st.number_input('Ingrese una Cantidad:', min_value=0, step=1)
    selected_cantidad=str(cantidad)
    precio = st.number_input('Ingrese un precio:', min_value=0.0, format="%.2f")
    # Asegurarse de que el valor se trate como un flotante
    precio = round(float(precio), 2)
    precio_str = str(precio)

    # Obtener emoji correspondiente a la categoría seleccionada
    category_emoji = {
        'Almacen': '🏬',
        'Mascotas': '🐾',
        'Bebidas y bodega': '🍷'
    }
    st.subheader("Datos:")
    st.write("Producto:", selected_productos)
    st.write("Precio:", precio_str)
    st.write("Categoría:", category_emoji[selected_category], selected_category)
    st.write("Cantidad:", selected_cantidad)
    if st.button("Insertar"):# Verificar tipos de datos

        response = insert_data(selected_producto_sin_emojis, precio_str , selected_category , selected_cantidad)
        
        if response[1] == 200:
            st.empty()
            data = get_data()
            st.success("Datos insertados exitosamente")
        else:
            st.error(f"Hubo un error al insertar los datos")

        st.subheader("Tabla Productos en Google Sheets")
    st.write(data)

def delete_data(id):
    # URL de la API para borrar datos
    api_url = "https://python-fastapi-iamgod.koyeb.app/delete/"

    try:
        # Realizar la solicitud DELETE
        response = requests.delete(api_url + str(id))
        return response
    except requests.RequestException as e:
        st.error(f"Error de conexión: {e}")
        return None

def main_br():   
    # Obtener los datos de la API
    data = get_data()
    st.title("BORRAR Datos de la tabla Productos en Google Sheets")
    # Obtener la lista de valores de la columna "ID"
    
    if data is not None and isinstance(data, pd.DataFrame):
        id_list = data['ID'].tolist()
        selected_id_list= st.selectbox("Selecciona un ID de la tabla Productos:", id_list)  
        # Botón para enviar el ID a eliminar
        if st.button("Borrar"):
            # Llamar a la función delete_data para borrar el registro seleccionado
            response = delete_data(selected_id_list)
            
            # Verificar si la solicitud fue exitosa
            if response is not None and response.status_code == 200:
                st.success("Datos borrados exitosamente")
                # Actualizar los datos después del borrado
                data = get_data()
            else:
                st.error("Hubo un error al borrar los datos")
    else:

        st.warning("No se encontraron IDs para la categoría seleccionada.")

    st.write(data)

def main():
    st.set_page_config(
    page_title="Gestion de Hoja de Cálculo",
    page_icon="📊",
    layout="wide")
    # Título principal
    st.write("Creado por: Alexis Andrade")

    # Sidebar con mensaje de bienvenida
    with st.sidebar:
        st.sidebar.title("👋 ¡Bienvenido/a!")

        st.sidebar.subheader("Navegue a través del menú:")
        page = st.sidebar.selectbox(
            "Seleccione una página:",
            ("Inicio","Modificar", "Borrar", "Insertar", "Gráfico 'Top 3 Productos'","Variación, Comparación de Precios y Cantidad de Productos por Día")
        )

    if page == "Inicio":
        with st.container():

            page_explanations = {
            "Inicio": "Ver la lista de datos.",
            "Modificar": "Modificar datos existentes en la hoja de cálculo.",
            "Borrar": "Eliminar datos de la hoja de cálculo.",
            "Insertar": "Insertar nuevos datos en la hoja de cálculo."
            }

            st.title("👋 ¡Bienvenido/a! a mi proyecto de gestión de datos 📊")
            st.markdown("Puedes encontrar la hoja de GOOGLE en  [Google Sheets](https://docs.google.com/spreadsheets/d/1wF_mgiNfDMFZp5M94imuFpXHdND9bvKOD41IjZNNqdo/edit?usp=sharing)")
            st.write("Este proyecto tiene como objetivo facilitar la gestión de datos de una hoja de cálculo a través de una interfaz amigable y fácil de usar.")
            for page, explanation in page_explanations.items():
                st.write(f"**{page}**: {explanation}")
            data = get_data()
            st.write(data)


    elif page == "Gráfico 'Top 3 Productos'":
        
        data = get_data()
        
        # Convertir 'F. DE COMPRA' a datetime
        data['F. DE COMPRA'] = pd.to_datetime(data['F. DE COMPRA'], format='%d/%m/%Y')
                # Convertir la columna 'CANTIDAD' a tipo entero
        data["CANTIDAD"] = data["CANTIDAD"].astype(int)
        
        # Obtener el mes ingresado en la planilla
        mes_ingresado = data['F. DE COMPRA'].max().to_period('M')
        data_mes_ingresado = data[data['F. DE COMPRA'].dt.to_period('M') == mes_ingresado]

        # Convertir la columna 'CANTIDAD' a tipo numérico
        data_mes_ingresado['CANTIDAD'] = pd.to_numeric(data_mes_ingresado['CANTIDAD'], errors='coerce')

        # Calcular el total de cada producto por fecha de compra en el mes ingresado
        df_grouped = data_mes_ingresado.groupby('PRODUCTO')['CANTIDAD'].sum().nlargest(3)

        # Graficar con Plotly
        fig = go.Figure()

        # Añadir los datos de la torta
        fig.add_trace(go.Pie(labels=df_grouped.index, values=df_grouped, 
                            hoverinfo='label+percent', textinfo='value+label',
                            textfont_size=12))

        # Título del gráfico
        fig.update_layout(title_text=f"Top 3 Productos por Cantidad en {mes_ingresado}")

        # Mostrar gráfico
        st.plotly_chart(fig)
        st.write(f"con más unidades compradas del {mes_ingresado}")

    elif page == "Modificar":
        main_mr()
    elif page == "Borrar":
        main_br()
    elif page == "Insertar":
        main_sr()
    elif page == "Variación, Comparación de Precios y Cantidad de Productos por Día":
        
        data = get_data()
        
        df = pd.DataFrame(data)

            
        # Convertir la columna 'F. DE COMPRA' a tipo datetime
        df["F. DE COMPRA"] = pd.to_datetime(df["F. DE COMPRA"], format='%d/%m/%Y')
        # Convertir la columna 'PRECIO POR CANT.' a tipo float
        df["PRECIO POR CANT."] = df["PRECIO POR CANT."].str.replace(",", "").astype(float)
        # Convertir la columna 'CANTIDAD' a tipo entero
        df["CANTIDAD"] = df["CANTIDAD"].astype(int)

        # Agrupar por fecha de compra y calcular el total del precio por cantidad y cantidad de productos por día
        df_grouped = df.groupby("F. DE COMPRA").agg({"PRECIO POR CANT.": "sum", "PRODUCTO": "size"}).reset_index()
        df_grouped1 = df.groupby("F. DE COMPRA").agg({"CANTIDAD": "sum"}).reset_index()
        # Crear subtramas
        fig = make_subplots(specs=[[{"secondary_y": True}]])

        # Agregar la línea para los precios por día
        fig.add_trace(go.Scatter(
            x=df_grouped["F. DE COMPRA"], 
            y=df_grouped["PRECIO POR CANT."], 
            name="Total de Precios", 
            mode='lines+markers',
            hovertemplate='<b>Fecha:</b> %{x|%d/%m}<br><b>Total de Precios:</b> $%{y:,.2f}'
        ), secondary_y=False)

        # Agregar las barras para la cantidad de productos por día
        fig.add_trace(go.Bar(
            x=df_grouped1["F. DE COMPRA"], 
            y=df_grouped1["CANTIDAD"], 
            name="Cantidad de Productos",
            hovertemplate='<b>Fecha:</b> %{x|%d/%m}<br><b>Cantidad de Productos:</b> %{y}'
        ), secondary_y=True)

        # Actualizar las etiquetas de los ejes
        fig.update_layout(
        title="Comparación de la Evolución de los Precios Totales y la Cantidad de Productos por Día",
        xaxis=dict(title="Fecha de Compra"),
        yaxis=dict(title="Total de Precios", color="blue"),
        yaxis2=dict(title="Cantidad de Productos", color="red"),
        hovermode="x unified"
        )

        # Mostrar el gráfico en Streamlit
        st.plotly_chart(fig)

if __name__ == "__main__":
    main()
