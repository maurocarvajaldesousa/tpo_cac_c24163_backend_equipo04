from app.database import get_db

class Obra:
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
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM obras"
        cursor.execute(query)
        rows = cursor.fetchall()
        obras = [Obra(id_obra=row[0], descripcion=row[1], anio=row[2], partido=row[3], localidad=row[4], latitud=row[5], longitud=row[6], gmaps=row[7], imagen=row[8], ruta=row[9], categoria=row[10], estado=row[11]) for row in rows]
        cursor.close()
        return obras

    @staticmethod
    def get_by_id(id_obra):
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM obras WHERE id_obra = %s"
        cursor.execute(query, (id_obra,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Obra(id_obra=row[0], descripcion=row[1], anio=row[2], partido=row[3], localidad=row[4], latitud=row[5], longitud=row[6], gmaps=row[7], imagen=row[8], ruta=row[9], categoria=row[10], estado=row[11])
        return None

    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id_obra is None:
            query = ("INSERT INTO obras (descripcion, anio, partido, localidad, latitud, longitud, gmaps, imagen, ruta, categoria, estado) "
                     "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
            cursor.execute(query, (self.descripcion, self.anio, self.partido, self.localidad, self.latitud, self.longitud, self.gmaps, self.imagen, self.ruta, self.categoria, self.estado))
            self.id_obra = cursor.lastrowid
        else:
            query = ("UPDATE obras SET descripcion=%s, anio=%s, partido=%s, localidad=%s, latitud=%s, longitud=%s, gmaps=%s, imagen=%s, ruta=%s, categoria=%s, estado=%s "
                     "WHERE id_obra=%s")
            cursor.execute(query, (self.descripcion, self.anio, self.partido, self.localidad, self.latitud, self.longitud, self.gmaps, self.imagen, self.ruta, self.categoria, self.estado, self.id_obra))
        db.commit()
        cursor.close()

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        query = "DELETE FROM obras WHERE id_obra = %s"
        cursor.execute(query, (self.id_obra,))
        db.commit()
        cursor.close()