from app.database import get_db

class Obra:
    # Constructor
    def __init__(self, id_obra=None, descripcion=None, anio=None, partido=None, localidad=None, latitud=None, longitud=None, gmaps=None, imagen=None, ruta=None, categoria=None, estado=None):
        self.id_obra = id_obra
        self.descripcion = descripcion
        self.anio = anio
        self.partido = partido
        self.localidad = localidad
        self.latitud = latitud
        self.longitud = longitud
        self.gmaps = gmaps
        self.imagen = imagen
        self.ruta = ruta
        self.categoria = categoria
        self.estado = estado
    
    def serialize(self):
        return {
            'id_obra': self.id_obra,
            'descripcion': self.descripcion,
            'anio': self.anio,
            'partido': self.partido,
            'localidad': self.localidad,
            'latitud': self.latitud,
            'longitud': self.longitud,
            'gmaps': self.gmaps,
            'imagen': self.imagen,
            'ruta': self.ruta,
            'categoria': self.categoria,
            'estado': self.estado
        }
        
    @staticmethod
    def get_all():
        # Logica de buscar en la base todas las obras
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM obras"
        cursor.execute(query)
        # Obtengo resultados
        rows = cursor.fetchall()
        obras = [Obra(id_obra=row[0], descripcion=row[1], anio=row[2], partido=row[3], localidad=row[4], latitud=row[5], longitud=row[6], gmaps=row[7], imagen=row[8], ruta=row[9], categoria=row[10], estado=row[11]) for row in rows]
        # Cerramos el cursor
        cursor.close()
        return obras