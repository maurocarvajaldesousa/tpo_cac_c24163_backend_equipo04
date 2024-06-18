from app.database import get_db

class Obra:
  #contructor
  def __init__(self,id_obra=None,descripcion=None,anio=None,partido=None,localidad=None,latitud=None,longitud=None,gmaps=None,imagen=None,ruta=None,categoria=None,estado=None):
    self.id_obra
    self.descripcion
    self.anio
    self.partido
    self.localidad
    self.latitud
    self.longitud
    self.gmaps
    self.imagen
    self.ruta
    self.categoria
    self.estado
  
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
  #logica de buscar en la base todas las obras
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM obra"
    cursor.execute(query)
    #obtengo resultados
    rows = cursor.fetchall()
    obras = [Obra(id_obra=row[0], descripcion=row[1], anio=row[2], partido=row[3], localidad=row[4], latitud=row[5], longitud=row[6], gmaps=row[7], imagen=row[8],ruta=row[9],categoria=row[10],estado=row[11]) for row in rows]
    #cerramos el cursor
    cursor.close()
    return obras