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
    catalog['artworks'] = lt.newList('ARRAY_LIST')
    catalog['mediums'] = mp.newMap()
    catalog
    return catalog

# Funciones para agregar informacion al catalogo
def addArtwork(catalog, artwork):
    artistasObra = lt.newList()
    artistasId = artwork['ConstituentID'].replace('[','').replace(']','').split(',')
    n = 0
    while n < len(artistasId):
        artistasId[n] = artistasId[n].lstrip()
        n += 1
    for i in lt.iterator(catalog['artists']):
        artista = i['Artista']
        if artista['ConstituentID'] in artistasId:
            lt.addLast(i['Obras'], artwork)
            lt.addLast(artistasObra, artista['DisplayName'])
    lt.addLast(catalog["artworks"],{'Obra': artwork, 'Artistas': artistasObra})
    addArtworkMedium(catalog, artwork)

def addArtist(catalog, artist):
    # Se adiciona el libro a la lista de libros
    obras = lt.newList()
    lt.addLast(catalog["artists"],{'Artista': artist, 'Obras': obras})

def addArtworkMedium(catalog, artwork):
    medio = artwork['Medium']
    if mp.contains(catalog['mediums'], medio):
        entrada = mp.get(catalog['mediums'], medio)
        listaObras = me.getValue(entrada)
        lt.addLast(listaObras, artwork)
    else:
        listaObras = lt.newList('ARRAY_LIST')
        lt.addLast(listaObras, artwork)
        mp.put(catalog['mediums'], medio, listaObras)



# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
