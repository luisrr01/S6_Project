import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

# agregar un encabezado a la página
st.header('Anuncios de ventas de coches')

build_histogram = st.checkbox('Construir un histograma') # crear un checkbox
build_dispersion = st.checkbox('Construir un gráfico de dispersión') # crear un checkbox

if build_histogram: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para la columna odómetro para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if build_dispersion: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para la columna odómetro para el conjunto de datos de anuncios de venta de coches')
            
    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
