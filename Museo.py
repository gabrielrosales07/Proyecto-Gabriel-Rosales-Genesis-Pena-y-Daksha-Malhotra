from api import department_api, objects_in_departments, objects_details, nationalities_api, objects_in_nationalities
from Department import Department
from Obra import Obra

class Museo:
  
  def start(self):
    self.iniciar_objetos()
    
    while True:
      interfaz = input ("""Bienvenido al Museo MetroArt, escoja una opcion: 
1- Buscar Obras
2- Ver Detalles de Obras
---> """)
      if interfaz == "1":
        self.show_obras()

  def show_obras (self):
    choice = input ("""Ingrese como desea ver las obras: 
1- Por Departamento
2- Por Nacionalidad del Autor
3- Por Nombre del Autor
---> """)
    
    if choice == "1":
      self.show_departments()
      id_departamento = input ("Ingrese el ID de un departamento: ")
      
      try:
        department_found = False
        for departamento in self.department:
          if departamento.id == int(id_departamento):
            department_found = True
            break
            
        if department_found:
          object_ids = objects_in_departments ()
          if len(object_ids) > 0:
            print("Obras encontradas con éxito")
            print(f"Se encontraron {len(object_ids)} obras. ")
              
            self.obras = []
            for object_id in object_ids [:10]:
              dic_obras = objects_details (object_id)
              if dic_obras:
                self.obras.append(Obra( id_obra = dic_obras.get ("objectID"), titulo = dic_obras.get ("title"), autor = dic_obras.get ("artistDisplayName"), nacionalidad = dic_obras.get ("artistNationality"), fecha = dic_obras.get ("objectDate")))

            for obra in self.obras:
              obra.show()

          else:
              print ("No se encontraron obras en este departamento")
          
        else:
            print ("Error: ID ingresado incorrecto")
            
      except:
        print ("Error: El ID del departamento debe ser un número")

  def show_departments (self):
    for department in self.department:
      print()
      department.show()

  def iniciar_objetos (self):   
    dic_departments = department_api() ["departments"]
    self.department = []
    
    for department in dic_departments:
      self.department.append (Department(department["departmentId"], department["displayName"]))
    
