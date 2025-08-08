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
