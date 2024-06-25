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

- [Obtener todas las obras](#obtener-todas-las-obras)
- [Crear una obra](#crear-una-obra)
- [Obtener una obra específica](#obtener-una-obra-específica)
- [Actualizar una obra](#actualizar-una-obra)
- [Eliminar una obra](#eliminar-una-obra)
- [Obtener todas las rutas](#obtener-todas-las-rutas)
- [Obtener todas las categorías](#obtener-todas-las-categorías)

## Obtener todas las obras
Este endpoint permite obtener todas las obras almacenadas en la base de datos.

```
GET /api/obras
```

**Ejemplo de respuesta:**

```json
[
    {
        "id_obra": 1,
        "descripcion": "Descripción de la obra 1",
        "anio": 2021,
        "partido": "Partido 1",
        "localidad": "Localidad 1",
        "latitud": 123.456,
        "longitud": 789.012,
        "gmaps": "URL de Google Maps",
        "imagen": "URL de la imagen",
        "ruta": 1,
        "categoria": 1,
        "estado": 1
    },
    {
        "id_obra": 2,
        "descripcion": "Descripción de la obra 2",
        "anio": 2022,
        "partido": "Partido 2",
        "localidad": "Localidad 2",
        "latitud": 456.789,
        "longitud": 012.345,
        "gmaps": "URL de Google Maps",
        "imagen": "URL de la imagen",
        "ruta": 2,
        "categoria": 1,
        "estado": 1
    }
]


## Crear una obra
Este endpoint permite crear una nueva obra.

```
POST /api/obras
```

**Ejemplo de solicitud (JSON):**

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


## Obtener una obra específica
Este endpoint permite obtener los detalles de una obra específica mediante su identificador.

```
GET /api/obras/<int:id_obra>
```

**Ejemplo de respuesta:**

```json
{
    "id_obra": 1,
    "descripcion": "Descripción de la obra 1",
    "anio": 2021,
    "partido": "Partido 1",
    "localidad": "Localidad 1",
    "latitud": 123.456,
    "longitud": 789.012,
    "gmaps": "URL de Google Maps",
    "imagen": "URL de la imagen",
    "ruta": 1,
    "categoria": 1,
    "estado": 1
}


## Actualizar una obra
Este endpoint permite actualizar los detalles de una obra existente.

```
PUT /api/obras/<int:id_obra>
```

**Ejemplo de solicitud (JSON):**

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

## Eliminar una obra
Este endpoint permite eliminar una obra existente.

```
DELETE /api/obras/<int:id_obra>
```

## Obtener todas las rutas
Este endpoint permite obtener todas las rutas disponibles.

```
GET /api/rutas
```

## Obtener todas las categorías
Este endpoint permite obtener todas las categorías disponibles.

```
GET /api/categorias
```
