/**
 * ==========================================================================
 *  MÓDULO FRONTEND (DOM, Eventos y Simulación Fetch)
 * ==========================================================================
 * Teoría:
 * JavaScript en el navegador se encarga de:
 * 1. Manipular el DOM (ej. inicializar plugins como DataTables).
 * 2. Escuchar eventos (clics, teclas).
 * 3. Solicitar datos al backend (mediante Fetch API) y renderizarlos.
 */

// Esperamos a que el HTML termine de cargar en el navegador
document.addEventListener('DOMContentLoaded', () => {
    
    // 1. Inicialización de librería de terceros (jQuery + DataTables)
    const tabla = $('#tablaEstudiantes').DataTable({
        language: {
            url: '//cdn.datatables.net/plug-ins/1.13.6/i18n/es-ES.json'
        }
    });

    // 2. Manipulación del DOM y Eventos
    const btnCargar = document.getElementById('btnCargar');
    
    btnCargar.addEventListener('click', () => {
        // 3. Simulación de Petición Asíncrona (Fetch) a un Backend (Python/ORM)
        console.log("Simulando llamada a API Backend...");
        
        const datosSimulados = [
            { id: 1, nombre: 'Juan Perez', promedio: 8.5 },
            { id: 2, nombre: 'Ana Gomez', promedio: 9.2 },
            { id: 3, nombre: 'Carlos Ruiz', promedio: 8.8 },
            { id: 4, nombre: 'Elena Torres', promedio: 9.9 }
        ];

        // Limpiamos los datos actuales de la tabla
        tabla.clear();

        // Recorremos el JSON devuelto y agregamos filas a la tabla
        datosSimulados.forEach(est => {
            const estado = est.promedio >= 9.0 ? 'Destacado' : 'Regular';
            tabla.row.add([
                est.id,
                est.nombre,
                est.promedio,
                estado
            ]);
        });

        // Dibujamos la tabla con los nuevos datos
        tabla.draw();
        
        alert('¡Datos cargados dinámicamente usando JS!');
    });
});
