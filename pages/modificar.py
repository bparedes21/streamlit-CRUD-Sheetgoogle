import streamlit as st
import requests
import pandas as pd

def main():
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


    def update_data(id_value, product, price, category, discount):
        # URL of your FastAPI API
        api_url = "https://python-fastapi-iamgod.koyeb.app/update/"  # Update with your API URL
        url = api_url + id_value
        payload = {
            "column1": product,
            "column2": price,
            "column3": category,
            "column4": discount
        }
        
        try:
            response = requests.put(url, json=payload)
            response.raise_for_status()  # Check for errors in the response
            data = response.json()
            return data

        except requests.RequestException as e:
            # Log the error
            print(f"Error updating data: {e}")
            return None


    data=pd.DataFrame()
    data = get_data()

    st.title("MODIFICAR Datos de la tabla Productos en Google Sheets")
    # Obtener la lista de valores de la columna "ID"
    id_list = data['ID'].tolist()
    if len(id_list)!=0:
        selected_id_list= st.selectbox("Selecciona un ID de la tabla Productos:", id_list)    
        # Definir los productos para cada categoría junto con sus emojis correspondientes
        productos = {
            'Almacen': [('🍝', 'Fideos'), ('🍚', 'Arroz'), ('🍅', 'Pure de Tomate')],
            'Mascotas': [('🐶', 'Alimento para perro'), ('🐱', 'Alimento para gato'), ('🐰', 'Alimento para conejo')],
            'Bebidas y bodega': [('🥤', 'Gaseosa'), ('💧', 'Agua'), ('🍷', 'Vino')]
        }
        
        st.subheader("Ingrese los datos a modificar:")
        # Crear menú desplegable con las categorías
        selected_category = st.selectbox("Selecciona una categoría:", list(productos.keys()))
        # Obtener los productos con emojis y sin emojis

        productos_emojis = [producto[0] + " " + producto[1] for producto in productos[selected_category]]
        productos_sin_emojis = [producto[1] for producto in productos[selected_category]]

        # Crear el selectbox para los productos
        selected_productos = st.selectbox("Seleccione un producto:", productos_emojis)

        # Obtener el producto sin emojis correspondiente al seleccionado
        selected_producto_sin_emojis = productos_sin_emojis[productos_emojis.index(selected_productos)]


        descuento = ["0","10","20","30"]
        selected_descuento = st.selectbox("Seleccione un descuento:", descuento)

        precio = st.number_input ('Ingrese un precio:', min_value=0.0, format="%.2f")
        # Ensure the value is treated as a float
        precio = round(float(precio), 2)
        precio_str=str(precio)
        selected_id_list_str=str(selected_id_list)
        
        st.subheader("Datos:")
        st.write("Id:", "🔢 " + selected_id_list_str)
        st.write("Producto:", selected_productos)
        st.write("Precio:", "💰 " + precio_str)
        st.write("Categoría:", "🏷️ " + selected_category)
        st.write("Descuento:", "🔖 " + selected_descuento)
        
        if st.button("Modificar"):
            response = update_data( selected_id_list_str, selected_producto_sin_emojis , precio_str , selected_category , selected_descuento)
            if 'status_code' in response and response['status_code'] == 200:

                st.empty()
                data = get_data()
                st.success("Datos modificados exitosamente")
            else:
                st.error(f"Hubo un error al modificar los datos")

            # Limpiar el contenido actual

    else:

        st.warning("No se encontraron IDs para la categoría seleccionada.")


    # Mostrar los datos en Streamlit
    if data is not None and not data.empty:
        
        st.subheader("Tabla Productos en Google Sheets")
        st.write(data)
    else:
        st.warning("No se encontraron datos.")
        
if __name__ == "__main__":
    main()