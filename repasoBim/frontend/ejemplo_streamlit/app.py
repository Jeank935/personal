"""
Frontend Básico en Streamlit
----------------------------
Este es un ejemplo puramente de Frontend y Visualización de datos,
sin conexión a bases de datos (perfecto para repasar componentes rápidos).
"""
import streamlit as st
import pandas as pd
import numpy as np

def main():
    st.set_page_config(page_title="Ejemplo Frontend Streamlit", layout="centered")
    
    st.title("🎨 Ejemplo Básico de Streamlit")
    st.markdown("Streamlit es ideal para construir dashboards rápidos en Python.")
    
    st.header("1. Elementos Interactivos")
    nombre = st.text_input("Ingresa tu nombre:", "Estudiante")
    edad = st.slider("Selecciona tu edad", 15, 60, 20)
    
    if st.button("Saludar"):
        st.success(f"¡Hola {nombre}! Tienes {edad} años.")
        
    st.header("2. Gráficos y Datos Aleatorios")
    st.write("Podemos mostrar gráficos usando Pandas y NumPy fácilmente:")
    
    # Generar datos aleatorios
    df_chart = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C']
    )
    
    st.line_chart(df_chart)

if __name__ == "__main__":
    main()
