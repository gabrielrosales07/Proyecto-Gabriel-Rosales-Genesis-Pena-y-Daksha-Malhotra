class Department:
    """
    Clase que representa un departamento dentro del museo con atributos de id y nombre
    """
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def show(self):
        """
        muestra en la consola los atributos especificados
        """
        print(f"ID: {self.id}")
        print(f"Nombre: {self.nombre}")
