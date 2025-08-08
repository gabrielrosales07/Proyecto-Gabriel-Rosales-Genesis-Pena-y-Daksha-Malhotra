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
      
