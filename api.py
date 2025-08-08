import requests

def department_api ():
    department = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/departments")
    try:
        if department.status_code == 200:
            return department.json()
        
        else:
            print (f"Se encontro un error al buscar la API de los departamentos. Codigo: {department.status_code}")
    
    except:
        print (f"Error de conexion, intentelo de nuevo mas tarde")
        return []
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
        print (f"Error de conexion, intentelo de nuevo mas tarde")
        return []

      
