class Obra:
    """
    Clase que representa obra dentro del museo con sus atributos
    """
   
    def __init__(self, datos):
        """
        Constructor de la clase Obra, inicia un objeto a partir de un diccionario de datos de la api
        """
       
        self.id_objeto = datos.get("objectID")
        self.titulo = datos.get("title", "Título no disponible")
        self.nombre_artista = datos.get("artistDisplayName", "Artista no disponible")
        self.nacionalidad_artista = datos.get("artistNationality", "No disponible")
        self.fecha_nacimiento_artista = datos.get("artistBeginDate", "No disponible")
        self.fecha_muerte_artista = datos.get("artistEndDate", "No disponible")
        self.clasificacion = datos.get("classification", "No disponible")
        self.fecha_objeto = datos.get("objectDate", "No disponible")
        self.url_imagen = datos.get("primaryImage", None)


    def mostrar(self):
        """
        muestra en la consola los atributos especificados
        """
        print(f"ID de Obra: {self.id_objeto}")
        print(f"Titulo: {self.titulo}")
        print(f"Nombre: {self.nombre_artista}")
        print(f"Nacionalidad: {self.nacionalidad_artista}")
        print(f"Fecha de nacimiento: {self.fecha_nacimiento_artista}")
        print(f"Fecha de Muerte: {self.fecha_muerte_artista}")
        print(f"Clasificacion: {self.clasificacion}")
        print(f"Ano de creacion: {self.fecha_objeto}")
        if self.url_imagen:
            print(f"link de la Imagen: {self.url_imagen}")
        else:
            print("No hay link de imagen disponible")




#se decidio hacer esta clase de esta manera porque se accede directamente a la api (antes salia un error 502 para cada link)

