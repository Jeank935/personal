"""
Visualización de Datos desde CouchDB usando Streamlit
-----------------------------------------------------
Se conecta a CouchDB, lee los datos insertados en el script anterior y los muestra en web.
"""
import streamlit as st
import couchdb
import pandas as pd

st.set_page_config(page_title="Visualizador CouchDB")
st.title("📦 Visualizador de Inventario (CouchDB)")
st.write("Este script de Streamlit consume los documentos de CouchDB para mostrarlos.")

try:
    # Conexión a CouchDB
    server = couchdb.Server('http://admin:admin@localhost:5984/')
    db = server['productos_db']
    
    # Extraer todos los documentos
    documentos = []
    for doc_id in db:
        if not doc_id.startswith('_design'):
            documentos.append(db[doc_id])
            
    if documentos:
        # Convertir JSON a DataFrame para usar tablas nativas de Streamlit
        df = pd.DataFrame(documentos)
        
        # Limpiamos datos internos de couchdb que no le interesan al usuario final
        df = df.drop(columns=['_id', '_rev', 'id'], errors='ignore')
        
        st.success("¡Datos recuperados desde CouchDB!")
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Tabla de Datos")
            st.dataframe(df)
            
        with col2:
            st.subheader("Stock por Producto")
            st.bar_chart(df.set_index('nombre')['stock'])
            
    else:
        st.warning("La base de datos está vacía.")
        
except Exception as e:
    st.error(f"❌ Error al conectar con CouchDB: {e}")
    st.info("Para que esto funcione, ejecuta primero el script '1_extraccion_y_carga.py' de esta misma carpeta.")
