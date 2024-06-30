# Repo de nuestro TPO Backend CaC 2024 - Equipo #04 📃

## Integrantes del equipo :construction:

| **Apellido, Nombre**     |
| ------------------------ |
| Favara, Jésica           |
| Clabel, Diana            |
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

## Documentación de Endpoints disponibles

- Obtener todas las obras: (GET /api/obras)
- Crear una obra: (POST /api/obras)
- Obtener una obra específica: (GET /api/obras/<int:id_obra>)
- Actualizar una obra: (PUT /api/obras/<int:id_obra>)
- Eliminar una obra: (DELETE /api/obras/<int:id_obra>)
- Obtener todas las rutas: (GET /api/rutas)
- Obtener todas las categorías: (GET /api/categorias)

### EJEMPLOS PARA TESTEAR ENDPOINTS UTILIZANDO POSTMAN Ó THUNDER CLIENT

**Ejemplos de solicitud (JSON) para home, listar obras, listar categorías y listar rutas:**

- GET http://127.0.0.1:5000/
- GET http://127.0.0.1:5000/api/obras
- GET http://127.0.0.1:5000/api/categorias
- GET http://127.0.0.1:5000/api/rutas

**Ejemplo de solicitud (JSON) para crear una obra:**

- POST http://127.0.0.1:5000/api/obras

```json
{
  "anio": "1950",
  "categoria": 1,
  "descripcion": "Obra de prueba",
  "estado": 1,
  "gmaps": "https://maps.app.goo.gl/ACfZ52YgRNcAsrTE6",
  "id_obra": 1,
  "imagen": "https://raw.githubusercontent.com/maurocarvajaldesousa/tpo_cac_c24163_equipo10/main/img/obras/obra_01.png",
  "latitud": "-38.089060",
  "localidad": "SALDUNGARAY",
  "longitud": "-62.216740",
  "partido": "TORNQUIST",
  "ruta": 1
}
```

**Ejemplo de solicitud (JSON) para actualizar la obra con id 22:**

- PUT http://127.0.0.1:5000/api/obras/22

```json
{
  "anio": "1950",
  "categoria": 1,
  "descripcion": "Obra editada",
  "estado": 1,
  "gmaps": "https://maps.app.goo.gl/ACfZ52YgRNcAsrTE6",
  "id_obra": 1,
  "imagen": "https://raw.githubusercontent.com/maurocarvajaldesousa/tpo_cac_c24163_equipo10/main/img/obras/obra_01.png",
  "latitud": "-38.089060",
  "localidad": "SALDUNGARAY",
  "longitud": "-62.216740",
  "partido": "TORNQUIST",
  "ruta": 1
}
```

**Ejemplo de solicitud (JSON) para eliminar la obra con id 22:**

- DELETE http://127.0.0.1:5000/api/obras/22
