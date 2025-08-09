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

def obtener_detalles_obra(id_obra):
    """
    Obtiene los detalles completos de una obra específica usando su ID desde la API (id_obra), regresa un diccionario
    con detalles de la obra
    """

    try:
        url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{id_obra}"
        obra = requests.get(url)
        
        if obra.status_code == 200:
            return obra.json()
        else:
            print(f"Error al obtener detalles de la obra con ID {id_obra}. Código: {obra.status_code}")
            return None
    
    except:
        print("Error, no se encontro nada")
        return None

def buscar_por_nacionalidad(nacionalidad):
    """
    Busca obras por la nacionalidad del artista en la API (nacionalidad), regresa una lista de IDs 
    que coinciden con la nacionalidad.
    """
    
    try:
        url = f"https://collectionapi.metmuseum.org/public/collection/v1/search?artistNationality={nacionalidad}&q=painting"
        nacionality = requests.get(url)

        if nacionality.status_code == 200:
            return nacionality.json().get("objectIDs", [])
        else:
            print(f"Error al buscar obras por nacionalidad '{nacionalidad}'. Código: {nacionality.status_code}")
            return []
    
    except:
        print("Error, no se encontro nada")
        return []

def buscar_por_nombre_artista(nombre_artista):
    """
    Busca obras por el nombre del artista en la API (nombre_artista), retorna una lista de
    IDs que coinciden con el nombre del artista
    """
   
    try:
        url = f"https://collectionapi.metmuseum.org/public/collection/v1/search?q={nombre_artista}"
        artista = requests.get(url)


        if artista.status_code == 200:
            return artista.json().get("objectIDs", [])
        else:
            print(f"Error al buscar obras por nombre de artista '{nombre_artista}'. Código: {artista.status_code}")
            return []
   
    except:
        print("Error, no se encontro nada")
        return []

        


