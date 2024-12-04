import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
df = pd.read_csv("./data/vehicles_us.csv")

# Encabezado
st.header("Cuadro de Mandos: Análisis de Vehículos Usados")

# Casilla de verificación para mostrar el histograma
if st.checkbox("Mostrar histograma de odómetro"):
    fig_histogram = px.histogram(df, x="odometer", title="Distribución del Odómetro")
    st.plotly_chart(fig_histogram)  # Mostrar el histograma

# Casilla de verificación para mostrar el gráfico de dispersión
if st.checkbox("Mostrar gráfico de dispersión (Precio vs Año del Modelo)"):
    fig_scatter = px.scatter(df, x="model_year", y="price", title="Precio vs Año del Modelo")
    st.plotly_chart(fig_scatter)  # Mostrar el gráfico de dispersión