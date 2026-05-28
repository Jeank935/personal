"""
Extracción de un 'CSV' simulado y Carga a CouchDB
-------------------------------------------------
Simula extraer datos de una fuente, transformarlos a formato JSON y subirlos a CouchDB.
Similar a lo que se hace en el taller 05.
"""
import couchdb

def extraer_datos():
    # Simulamos datos que vienen de un CSV o PDF
    print("1. Extrayendo datos...")
    return [
        {"id": "001", "nombre": "Laptop", "precio": 1200.0, "stock": 50},
        {"id": "002", "nombre": "Teclado Mecánico", "precio": 100.0, "stock": 30},
        {"id": "003", "nombre": "Mouse", "precio": 45.0, "stock": 150}
    ]

def cargar_a_couchdb(datos):
    print("2. Conectando a CouchDB...")
    try:
        # Conexión local a CouchDB (Usando el contenedor Docker estándar)
        server = couchdb.Server('http://admin:admin@localhost:5984/')
        db_name = 'productos_db'
        
        # Crear base si no existe
        if db_name in server:
            db = server[db_name]
            print(f"   Base de datos '{db_name}' seleccionada.")
        else:
            db = server.create(db_name)
            print(f"   Base de datos '{db_name}' creada.")
            
        print("3. Cargando documentos JSON...")
        # Insertar los documentos
        for item in datos:
            # Usar el ID del producto como _id de CouchDB para evitar duplicados en re-ejecuciones
            item['_id'] = item['id']
            try:
                db.save(item)
                print(f"   [+] Insertado: {item['nombre']}")
            except couchdb.http.ResourceConflict:
                print(f"   [!] El producto {item['nombre']} ya existe en la BD. Saltando...")
                
        print("\n✅ ¡Carga a CouchDB finalizada con éxito!")
    except Exception as e:
        print(f"❌ Error con CouchDB: {e}")
        print("Asegúrate de tener el contenedor de CouchDB corriendo en el puerto 5984 con las credenciales admin:admin.")

if __name__ == "__main__":
    datos = extraer_datos()
    cargar_a_couchdb(datos)
