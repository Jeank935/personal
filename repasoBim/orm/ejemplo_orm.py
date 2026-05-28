"""
Ejemplo Sencillo de ORM con SQLAlchemy
----------------------------------------
Concepto: Este script muestra cómo conectarse a una base de datos local SQLite,
definir una tabla usando clases (Modelos) y realizar inserciones y consultas, 
similar a lo visto en la clase 07.
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

# 1. Definición del Modelo
class Mascota(Base):
    __tablename__ = 'mascotas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    especie = Column(String(50), nullable=False)

def main():
    # 2. Crear el engine (conexión a la BD SQLite local)
    engine = create_engine("sqlite:///mascotas_demo.db", echo=False)
    
    # 3. Crear las tablas
    Base.metadata.create_all(engine)
    
    # 4. Iniciar sesión
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # 5. Insertar datos (si está vacío)
    if session.query(Mascota).count() == 0:
        m1 = Mascota(nombre="Firulais", especie="Perro")
        m2 = Mascota(nombre="Mishi", especie="Gato")
        m3 = Mascota(nombre="Nemo", especie="Pez")
        session.add_all([m1, m2, m3])
        session.commit()
        print("✅ Mascotas insertadas con éxito.")
        
    # 6. Consultar datos
    print("\n📋 Lista de Mascotas (Desde SQLite):")
    todas = session.query(Mascota).all()
    for m in todas:
        print(f" - ID {m.id}: {m.nombre} (Especie: {m.especie})")

if __name__ == "__main__":
    main()
