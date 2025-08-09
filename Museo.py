"""
este modulo contiene la clase principal Museo, maneja el menú, la interacción con el usuario, la carga de datos
y la visualización de obras
"""
import os
import requests
from PIL import Image

from api import obtener_departamentos, buscar_por_departamento, obtener_detalles_obra, buscar_por_nacionalidad, buscar_por_nombre_artista
from Department import Department
from Obra import Obra

class Museo:
    """
    clase principal que gestiona la aplicación
    """
    def start(self):
        """
        inicia el programa y llama los metodos para cargar los datos y muestra el menu principal
        """
        self.cargar_datos()
       
        while True:
            """
            menu principal que muestra las opciones al usuario
            """
            print("\n Bienvenido al museo MetroArt, Elija una opcion")
            interfaz = input("1.- Ver obras \n2.- Mostrar detalles de la obra \n3.- Salir \n---> ")

            if interfaz == "1":
                self.menu_busqueda()

            elif interfaz == "2":
                self.mostrar_detalles_obra()

            elif interfaz == "3":
                print("Saliendo del sistemaa")
                break

            else:
                print("Opcion invalida. Por favor seleccione un numero del 1 al 3.")

