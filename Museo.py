from api import department_api, objects_in_departments
from Department import Department

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
        

  def show_departments (self):
    for department in self.
    print()
    department.show()

  def iniciar_objetos (self):   
        dic_departments = department_api() ["departments"]
        self.department = []
    
    for department in dic_departments:
      self.department.append (Department(department["departmentId"], department["displayName"]))
    
