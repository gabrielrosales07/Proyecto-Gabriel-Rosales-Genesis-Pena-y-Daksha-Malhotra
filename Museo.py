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

    def menu_busqueda(self):
        """
        muestra el submenu de opciones por departamento, nacionalidad, artista
        """
      
        while True:
            opcion = input("1. Por departamento \n2. Por Nacionalidad del Autor \n3. Por Nombre del Autor \n4. Volver \n---> ")
            
            if opcion == "1":
                self.buscar_obras_por_departamento()

            elif opcion == "2":
                self.buscar_obras_por_nacionalidad()

            elif opcion == "3":
                self.buscar_obras_por_artista()

            elif opcion == "4":
                break 
            
            else:
                print("Opción invalida. intentalo de nuevo.")

    def buscar_obras_por_departamento(self):
        """
        Permite al usuario buscar obras por ID de departamento
        Muestra los departamentos disponibles y luego pide un ID para buscar obras
        Utiliza mostrar_obras_paginadas para mostrar los resultados de 10 en 10
        """
       
        for departamento in self.departamentos:
            departamento.show()
           
        try:
            id_departamento = int(input("\n Ingrese el ID del departamento que desea explorar: "))
           
            ids_obras = buscar_por_departamento(id_departamento)
            if not ids_obras:
                print("No se encontraron obras para este departamento.")
                return
            self.mostrar_obras_paginadas(ids_obras)
           
        except:
            print("opcion invalida")

    def buscar_obras_por_nacionalidad(self):
        """
        Permite al usuario buscar obras por nacionalidad del autor
        Muestra las nacionalidades disponibles y luego pide un numero para buscar obras por la nacionalidad
        Utiliza mostrar_obras_paginadas para mostrar los resultados de 10 en 10
        """
        for i, nacionalidad in enumerate(self.nacionalidades):
            print(f"{i+1}. {nacionalidad}")
            
        try:
            opcion = int(input("\n Seleccione el numero de una nacionalidad: "))

            if opcion >= 1 and opcion <= len(self.nacionalidades):
                nacionalidad_elegida = self.nacionalidades[opcion - 1]
               
                ids_obras = buscar_por_nacionalidad(nacionalidad_elegida)
               
                if ids_obras:
                    self.mostrar_obras_paginadas(ids_obras)
                else:
                    print(f"No se encontraron obras en {nacionalidad_elegida} ")
            else:
                print("Opcion no valida, elija un número de la lista")
        except:
            print("opcion invalida, ingrese un numero)

    def leer_nacionalidades_desde_archivo(self):
        """
        Lee la lista de nacionalidades desde el archivo "Nationalities.txt"
        """
        nacionalidades_cargadas = []

        #se tuvo que buscar una manera que no conocemos para leer un archivo txt, importamos os
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        file = os.path.join(directorio_actual, "Nationalities.txt")

        try:
            with open(file, "r") as archivo:
                for linea in archivo:
                    nacionalidades_cargadas.append(linea.strip())
        except:
            print(f" no se encontro archivo: {file}")
       
        return nacionalidades_cargadas

    def buscar_obras_por_artista(self):
        """
        Permite al usuario buscar obras por el nombre del artista
        Utiliza mostrar_obras_paginadas para mostrar los resultados de 10 en 10
        """
       
        nombre_artista = input("\n Ingrese el nombre del artista: ").strip()


        if nombre_artista:
            ids_obras = buscar_por_nombre_artista(nombre_artista)
           
            if ids_obras:
                self.mostrar_obras_paginadas(ids_obras)
            else:
                print(f"No se encontraron obras para el artista {nombre_artista}")
       
        else:
            print("error, no ingresaste nada.")
       

    def mostrar_obras_paginadas(self, ids_obras):
        """
        Muestra una lista de obras de 10 en 10.
        Para cada obra muestra: ID, Título, Autor
        """
     
        total_obras = len(ids_obras)
       
        if total_obras == 0:
            return

        indice_actual = 0
        while indice_actual < total_obras:
            print(f"\n Imprimiendo de 10 en 10 ")
           
            """
            Se tiene un parametro inicial (indice_actual) que permite iterar en un rango de 10 en 10
            siempre y cuandoel indice actual no sea mayor que el total de obras
            """
            for i in range(indice_actual, min(indice_actual + 10, total_obras)):
                id_obra_actual = ids_obras[i]
                try:
                    datos_obra = obtener_detalles_obra(id_obra_actual)
                    if datos_obra:
                        obra_objeto = Obra(datos_obra)
                        print(f"ID: {obra_objeto.id_objeto} - Título: {obra_objeto.titulo} - Autor: {obra_objeto.nombre_artista}")
                    else:
                        print(f"ID no dispomible")

                except:
                    print(f"Error al procesar ")

            indice_actual += 10
           
            """
            Se le pide al usuario si quiere continuar viendo mas obras, si coloca "s" imprime las siguientes 10
            sino rompe el bucle
            """
            if indice_actual < total_obras:
                continuar = input("\n quiere ver más obras? (s/n): ").strip().lower()
                if continuar != 's':
                    break
            else:
                print("\n no hay mas obras")
    
    
    def mostrar_detalles_obra(self):
        """
        permite al usuario ver los detalles de una obra en concreto preguntando por su ID
        y los muestra utilizando la clase Obra.
        """
        
        try:
            id_obra = int(input("\n Ingrese el ID para ver detalles: "))

            datos_obra = obtener_detalles_obra(id_obra)

            if datos_obra:
                obra_objeto = Obra(datos_obra)
                obra_objeto.mostrar() 
                
            else:
                print(f"no se encontraron detalles de la obra {id_obra}")
        
        except:
            print("valor ingresado incorrecto")
        
           

    def cargar_datos(self):
            """
            carga los datos iniciales como objetos al inicio de la aplicación
            """
            self.departamentos = []
            self.nacionalidades = []

            datos_departamentos = obtener_departamentos()
            for departamento in datos_departamentos:
                self.departamentos.append(Department(departamento["departmentId"], departamento["displayName"]))
            
            self.nacionalidades = self.leer_nacionalidades_desde_archivo()
    



