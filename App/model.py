"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.Algorithms.Sorting import mergesort as merge
from DISClib.Algorithms.Sorting import quicksort as qk
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    """
    Inicializa el catálogo. Crea una lista vacia para guardar
    todos los artistas, adicionalmente, crea una lista vacia para las obras de arte,
    Retorna el catalogo inicializado.
    """
    catalog = {'artists': None,
               'artworks': None,
               'mediums': None,
               'nationalities': None }
    catalog['artists'] = lt.newList('ARRAY_LIST')
    catalog['artworks'] = lt.newList('ARRAY_LIST')
    catalog["mediums"]=mp.newMap(maptype="PROBING")
    catalog['nationalities']= mp.newMap()
    return catalog

# Funciones para agregar informacion al catalogo
def addArtwork(catalog, artwork):
    lt.addLast(catalog["artworks"],artwork)
    # Se adiciona el libro a la lista de libros

def addArtist(catalog, artist):
    # Se adiciona el libro a la lista de libros
    lt.addLast(catalog["artists"],artist)

def addNationalities(catalog):
    artistas = catalog['artists']
    nacionalidades = catalog['nationalities']
    for i in lt.iterator(artistas):
        nacionalidad = i['Nationality']
        if(nacionalidad ==''):
            nacionalidad = 'Unknown'
        obrasArtist = obrasArtista(i['ConstituentID'], catalog)
        if mp.contains(nacionalidades,nacionalidad):
            entry=mp.get(nacionalidades,nacionalidad)
            lista=me.getValue(entry)
            for obra in lt.iterator(obrasArtist):
                if not(lt.isPresent(lista, obra)):
                    lt.addLast(lista, obra)
        else:
            mp.put(nacionalidades, nacionalidad, obrasArtist)
        
            


# Funciones para agregar informacion al catalogo

def addArtworkMedium(catalog, artwork):
    medio = artwork['Medium']
    if mp.contains(catalog["mediums"],medio):
        entry=mp.get(catalog["mediums"],medio)
        lista=me.getValue(entry)
        lt.addLast(lista,artwork)   
    else:
        listaObras =lt.newList('ARRAY_LIST')
        lt.addLast(listaObras,artwork)
        mp.put(catalog["mediums"], medio, listaObras)
    

# Funciones para creacion de datos

# Funciones de consulta
def obrasmasantiguas(catalog,medio,cantidad):
    if mp.contains(catalog["mediums"],medio):
        entry=mp.get(catalog["mediums"],medio)
        lista=me.getValue(entry)
        listaord=ordenarObrasPorFecha(lista)
        mlista=lt.subList(listaord,0,cantidad)
        return mlista
    else:
        return False

def obrasArtista(artistId, catalog):
    obras = catalog['artworks']
    lista = lt.newList('ARRAY_LIST',cmpArtworks)
    for obra in lt.iterator(obras):
        artistasObra = obra['ConstituentID'].replace('[','').replace(']','').split(',')
        for i in artistasObra:
            i = i.strip()
        if artistId in artistasObra:
            lt.addLast(lista, obra)
    return lista

def darObrasNacionalidad(catalog, nationality):
    nacionalidades = catalog['nationalities']
    if mp.contains(nacionalidades, nationality):
        entry=mp.get(nacionalidades, nationality)
        lista=me.getValue(entry)
        return lista
    else:
        return None



    


        
# Funciones utilizadas para comparar elementos dentro de una lista
def cmpArtworkByDate(artwork1, artwork2):
    """
    Devuelve verdadero (True) si el 'Date' de artwork1 es menores que el de artwork2
    Args:
    artwork1: informacion de la primera obra que incluye su valor 'Date'
    artwork2: informacion de la segunda obra que incluye su valor 'Date'
    """
    obra1 = artwork1['Date']
    obra2 = artwork2['Date']
    if obra1=="":
        obra1=0
    elif obra2=="":
        obra2=0
    else:
        if int(obra1) < int(obra2):
            return True
    
        else:
            return False

def cmpArtworks(a1,a2):
    iD1= a1['ObjectID']
    iD2= a2['ObjectID']
    if iD1 > iD2:
        return 1
    elif iD2 > iD1:
        return -1
    return 0

# Funciones de ordenamiento
def ordenarObrasPorFecha(lista):
    listadef=qk.sort(lista,cmpArtworkByDate)
    return listadef
