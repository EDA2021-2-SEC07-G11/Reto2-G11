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


from DISClib.DataStructures.arraylist import isPresent, size
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
    catalog["mediums"]=mp.newMap(maptype='PROBING', loadfactor= 0.80)
    catalog['nationalities']= mp.newMap(maptype='PROBING',loadfactor=0.80)
    catalog['años'] = mp.newMap(maptype='PROBING',loadfactor=0.80)
    return catalog

# Funciones para agregar informacion al catalogo
def addArtwork(catalog, artwork):
    artistas = catalog['artists']
    artwork['ConstituentID'] = artwork['ConstituentID'].replace('[','').replace(']','').split(',')
    for i in artwork['ConstituentID']:
        i = i.strip()
    lt.addLast(catalog["artworks"],artwork)
    #total = len(artwork['ConstituentID'])
    #cantidad = 0
    #for artista in lt.iterator(artistas):
    #    if artista['ConstituentID'] in artwork['ConstituentID']:
   #         addNationality(catalog, artista, artwork)
    #        cantidad += 1
     #   if cantidad == total:
      #      break
    addArtworkMedium(catalog, artwork)


def addArtist(catalog, artist):
    # Se adiciona el libro a la lista de libros
    lt.addLast(catalog["artists"],artist)
    agregarArtistaFecha(catalog, artist)


def addNationality(catalog, artista, artwork):
    nacionalidad = artista['Nationality']
    nacionalidades = catalog['nationalities']
    if(nacionalidad ==''):
        nacionalidad = 'Unknown'
    if mp.contains(nacionalidades,nacionalidad):
        entry=mp.get(nacionalidades,nacionalidad)
        lista=me.getValue(entry)
        if not(lt.isPresent(lista, artwork)):
            lt.addLast(lista, artwork)
    else:
        listaNacionalidad = lt.newList('ARRAY_LIST', cmpArtworks)
        lt.addLast(listaNacionalidad, artwork)
        mp.put(nacionalidades, nacionalidad,listaNacionalidad)
        

def addArtworkMedium(catalog,artwork):
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



def darObrasNacionalidad(catalog, nationality):
    nacionalidades = catalog['nationalities']
    if mp.contains(nacionalidades, nationality):
        entry=mp.get(nacionalidades, nationality)
        lista=me.getValue(entry)
        return lista
    else:
        return None


def agregarArtistaFecha(catalog, artist):
    mapa = catalog['años']
    fecha = artist['BeginDate']
    if(fecha == ''):
        fecha = 10000
    else:
        fecha = int(fecha)
    if mp.contains(mapa, fecha):
        entry=mp.get(mapa, fecha)
        lista=me.getValue(entry)
        lt.addLast(lista, artist)
    else:
        lista = lt.newList()
        lt.addLast(lista, artist)
        mp.put(mapa, fecha, lista)

def darArtistasRango(catalog, inicio, fin):
    lista = lt.newList(datastructure='ARRAY_LIST')
    mapa = catalog['años']
    for i in range(inicio, fin):
        if mp.contains(mapa, i):
            entry=mp.get(mapa, i)
            artistas=me.getValue(entry)
            for artista in lt.iterator(artistas):
                lt.addLast(lista, artista)
    return merge.sort(lista, cmpArtistDate)

    
def darViejosyJovenes(lista):
    retorno = []
    if lt.size(lista) >= 3:
        n = 1
        while n < 4:
            artista = lt.getElement(lista, n)
            retorno.append(darInfoArtista1(artista))
            n += 1
        n = lt.size(lista) - 2
        while n < lt.size(lista)+1:
            artista = lt.getElement(lista, n)
            retorno.append(darInfoArtista1(artista))
            n += 1
    else:
        for artista in lt.iterator(lista):
            retorno.append(darInfoArtista1(artista))
    return retorno

def darInfoArtista1(artista):
    nombre = artista['DisplayName']
    if nombre == "":
        nombre = "Unknown"
    inicio = artista['BeginDate']
    if inicio == "":
        inicio = "Unknown"
    final = artista['EndDate']
    if final == "":
        final = "Unknown"
    if int(final) ==0 and int(final) <int(inicio):
        final = "Todavía Vive"
    nacionalidad = artista['Nationality']
    if nacionalidad == "":
        nacionalidad = "Unknown"
    genero = artista['Gender']
    if genero == "":
        genero = "Unknown"
    return nombre, inicio, final, nacionalidad, genero

def buscarArtista(catalog, nombre):
    artistas = catalog['artists']
    for artista in lt.iterator(artistas):
        if artista['DisplayName'] == nombre:
            return artista
    return False

def darMediosArtista(catalog, artista):
    medios = catalog['mediums']
    iD = artista['ConstituentID']



        
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

def cmpArtists(a1,a2):
    iD1= a1['ConstituentID']
    iD2= a2['ConstituentID']
    if iD1 > iD2:
        return False
    elif iD2 > iD1:
        return True


def cmpArtistDate(a1,a2):
    fecha1= a1['BeginDate']
    fecha2= a2['BeginDate']
    if(fecha1 < fecha2):
        return True
    else:
        return False


# Funciones de ordenamiento
def ordenarObrasPorFecha(lista):
    listadef=qk.sort(lista,cmpArtworkByDate)
    return listadef
