# Repo de nuestro TPO Backend CaC 2024 - Equipo #04 📃

## Integrantes del equipo :construction: 

| **Apellido, Nombre** |
| -------------------- |
| Favara, Jésica |
| Clabel, Diana |
| Carvajal de Sousa, Mauro |

## Bitácora de entregables Proyecto Frontend :white_check_mark:

**Acceso a la página web del proyecto front:**
<a href="https://centrosalamone-dev.netlify.app/" target="_blank">Centro Salamone Saldungaray</a>

**Acceso al repositorio del proyecto front:**
<a href="https://github.com/maurocarvajaldesousa/tpo_cac_c24163_equipo10" target="_blank">Github proyecto front del Centro Salamone Saldungaray</a>

## Base de datos para nuestro Proyecto de Backend 🗃️

**DER del proyecto backend:**
![centrosalamone_db](https://github.com/maurocarvajaldesousa/tpo_cac_c24163_backend_equipo04/assets/1665906/ecf9d4cd-6b3f-438d-8db7-0cbd8c9f90d3)

**Acceso al script de creación del esquema para el proyecto backend:**
<a href="https://github.com/maurocarvajaldesousa/tpo_cac_c24163_backend_equipo04/blob/c231a99012c7d607b45d1f7f963bff1e888dc3ed/database_scripts/centrosalamone_db.sql" target="_blank">Script creación de base de datos</a>

**Acceso al script de generación de data de prueba para el proyecto backend:**
<a href="https://github.com/maurocarvajaldesousa/tpo_cac_c24163_backend_equipo04/blob/c231a99012c7d607b45d1f7f963bff1e888dc3ed/database_scripts/centrosalamone_db_data.sql" target="_blank">Script insertado de datos de prueba en la base de datos</a>

# Documentación de Endpoints disponibles

## Índice

- Obtener todas las obras: (GET /api/obras)
- Crear una obra: (POST /api/obras)
- Obtener una obra específica: (GET /api/obras/<int:id_obra>)
- Actualizar una obra: (PUT /api/obras/<int:id_obra>)
- Eliminar una obra: (DELETE /api/obras/<int:id_obra>)
- Obtener todas las rutas: (GET /api/rutas)
- Obtener todas las categorías: (GET /api/categorias)


**Ejemplo de solicitud (JSON) para crear una obra:**

```json
{
    "descripcion": "Nueva obra",
    "anio": 2023,
    "partido": "Nuevo Partido",
    "localidad": "Nueva Localidad",
    "latitud": 123.456,
    "longitud": 789.012,
    "gmaps": "Nueva URL de Google Maps",
    "imagen": "Nueva URL de la imagen",
    "ruta": 1,
    "categoria": 1,
    "estado": 1
}


**Ejemplo de solicitud (JSON) para actualizar una obra:**

```json
{
    "descripcion": "Descripción actualizada",
    "anio": 2022,
    "partido": "Partido actualizado",
    "localidad": "Localidad actualizada",
    "latitud": 456.789,
    "longitud": 012.345,
    "gmaps": "URL actualizada de Google Maps",
    "imagen": "URL actualizada de la imagen",
    "ruta": 2,
    "categoria": 1,
    "estado": "Estado actualizado de la obra"
}

