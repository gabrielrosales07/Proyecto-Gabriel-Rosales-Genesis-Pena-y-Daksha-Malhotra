def objects_in_departments ():
    obj_departments = requests.get ("https://collectionapi.metmuseum.org/public/collection/v1/search")
    try:
        if obj_departments.status_code == 200:
            db = obj_departments.json()
            return db.get ("objectIDs", [])
        
        else: 
            print (f"Se encontro un error al buscar por departamento. Codigo: {obj_departments.status_code}")
            return []
    
    except:
        print (f"Error de conexion, intentelo de nuev

class Obra:
    def __init__(self, id_obra, titulo, autor, nacionalidad, fecha):
        self.id_obra = id_obra
        self.titulo = titulo
        self.autor = autor
        self.nacionalidad = nacionalidad
        self.fecha = fecha

    def show(self):
        print(f"ID de la Obra: {self.id_obra}")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print(f"Fecha: {self.fecha}")
