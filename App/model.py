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
               'mediums': None }
    catalog['artists'] = lt.newList('ARRAY_LIST')
    catalog['artworks'] = mp.newMap()
    catalog['mediums'] = mp.newMap()
    catalog
    return catalog

# Funciones para agregar informacion al catalogo
def addArtwork(catalog, artwork):
    iD = artwork['ObjectID']
    mp.put(catalog['artworks'], iD, artwork)
    addArtworkMedium(catalog, artwork)

def addArtworkMedium(catalog, artwork):
    medio = artwork['medium']
    if mp.contains(catalog['mediums'], medio):
        entrada = mp.get(catalog['mediums'], medio)
        listaObras = me.getValue(entrada)
        lt.addLast(listaObras, artwork)
    else:
        listaObras = lt.newList('ARRAY_LIST')
        lt.addLast(artwork)
        mp.put(catalog['mediums'], medio, listaObras)

def addArtist(catalog, artist):
    iD = artist['ConstituentID']
    mp.put(catalog['artists'], iD, artist)

# Funciones para creacion de datos

# Funciones de consulta
def obrasmasantiguas(catalog,cantidad):
    return False


        
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
    if obra1 < obra2:
        return True
    else:
        return False

# Funciones de ordenamiento
def ordenarObrasPorFecha(lista):
    listadef=merge.sort(lista,cmpArtworkByDate)
    return listadef