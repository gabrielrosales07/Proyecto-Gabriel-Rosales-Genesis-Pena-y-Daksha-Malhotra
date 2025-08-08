import requests 
"""
Este módulo contiene funciones para interactuar con la API del Museo Metropolitano de Arte.
"""
def obtener_departamentos():
    """
    Obtiene la lista de todos los departamentos del museo desde la API, regresa Una lista de diccionarios,
    donde cada diccionario representa un departamento.
    """
    try:
        url = "https://collectionapi.metmuseum.org/public/collection/v1/departments"
        departamento = requests.get(url)
       
        if departamento.status_code == 200:
            return departamento.json().get("departments", [])
        else:
            print(f"Error al buscar los departamentos en la API. Código: {departamento.status_code}")
            return []
    except:
        print("Error, no se encontro nada")
        return []

def buscar_por_departamento(id_departamento):
    """
    Busca obras por un ID de departamento especifico en la API (argumento), retorna una lista de IDs de obras
    que coinciden con el departamento
    """
    try:
        url = f"https://collectionapi.metmuseum.org/public/collection/v1/search?departmentId={id_departamento}&q=painting"
        departamento = requests.get(url)

        if departamento.status_code == 200:
            return departamento.json().get("objectIDs", [])
        else:
            print(f"Error al buscar obras por departamento. Código: {departamento.status_code}")
            return []
   
    except:
        print("Error, no se encontro nada")
        return []


