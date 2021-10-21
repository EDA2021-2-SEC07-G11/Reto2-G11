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
               'nationalities': None,
               'añosArtistas': None,
               'fechasObras': None,
               'departamentos': None }
    catalog['artists'] = lt.newList('ARRAY_LIST')
    catalog['artworks'] = lt.newList('ARRAY_LIST')
    catalog["mediums"]=mp.newMap(maptype='CHAINING', loadfactor= 4.00)
    catalog['nationalities']= mp.newMap(maptype='PROBING',loadfactor=4.00)
    catalog['añosArtistas'] = mp.newMap(maptype='CHAINING',loadfactor=4.00)
    catalog['fechasObras'] = mp.newMap(maptype='CHAINING',loadfactor=4.00)
    catalog['departamentos'] = mp.newMap(maptype='CHAINING',loadfactor=4.00)
    return catalog

# Funciones para agregar informacion al catalogo
def addArtwork(catalog, artwork):
    artistas = catalog['artists']
    artwork['ConstituentID'] = artwork['ConstituentID'].replace('[','').replace(']','').split(',')
    n = 0
    while n < len(artwork['ConstituentID']):
        artwork['ConstituentID'][n] = artwork['ConstituentID'][n].strip()
        n += 1
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
    agregarObraFecha(catalog, artwork)
    agregarObraDepartamento(catalog, artwork)


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

def agregarArtistaFecha(catalog, artist):
    mapa = catalog['añosArtistas']
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
        lista = lt.newList('ARRAY_LIST')
        lt.addLast(lista, artist)
        mp.put(mapa, fecha, lista)

def agregarObraFecha(catalog, artwork):
    mapa = catalog['fechasObras']
    fecha = artwork['DateAcquired']
    if mp.contains(mapa, fecha):
        entry=mp.get(mapa, fecha)
        lista=me.getValue(entry)
        lt.addLast(lista, artwork)
    else:
        lista = lt.newList('ARRAY_LIST')
        lt.addLast(lista, artwork)
        mp.put(mapa, fecha, lista)

def agregarObraDepartamento(catalog, artwork):
    mapa = catalog['departamentos']
    dpto = artwork['Department']
    if mp.contains(mapa, dpto):
        entry=mp.get(mapa, dpto)
        lista=me.getValue(entry)
        lt.addLast(lista, artwork)
    else:
        lista = lt.newList('ARRAY_LIST')
        lt.addLast(lista, artwork)
        mp.put(mapa, dpto, lista)

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




def darArtistasRango(catalog, inicio, fin):
    lista = lt.newList(datastructure='ARRAY_LIST')
    mapa = catalog['añosArtistas']
    for i in range(inicio, fin):
        if mp.contains(mapa, i):
            entry=mp.get(mapa, i)
            artistas=me.getValue(entry)
            for artista in lt.iterator(artistas):
                lt.addLast(lista, artista)
    return merge.sort(lista, cmpArtistDate)

def darObrasRango(catalog, inicio, fin):
    lista = lt.newList(datastructure='ARRAY_LIST')
    mapa = catalog['fechasObras']
    fechas = mp.keySet(mapa)
    for fecha in lt.iterator(fechas):
        if fecha>= inicio and fecha <= fin:
            entry=mp.get(mapa, fecha)
            obras=me.getValue(entry)
            for obra in lt.iterator(obras):
                lt.addLast(lista, obra)
    return merge.sort(lista, cmpArtworkByDateAcquired)

def obrasCompradas(lista):
    n = 0
    for obra in lt.iterator(lista):
        if 'purchase' in obra['CreditLine'].lower():
            n += 1
    return n 
    
def darViejosyJovenes(lista):
    retorno = []
    if lt.size(lista) >= 6:
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

def darViejosyJovenesObra(catalog, lista):
    retorno = []
    if lt.size(lista) >= 6:
        n = 1
        while n < 4:
            obra = lt.getElement(lista, n)
            retorno.append(darInfoObra2(catalog,obra))
            n += 1
        n = lt.size(lista) - 2
        while n < lt.size(lista)+1:
            obra = lt.getElement(lista, n)
            retorno.append(darInfoObra2(catalog,obra))
            n += 1
    else:
        for obra in lt.iterator(lista):
            retorno.append(darInfoObra2(catalog,obra))
    return retorno

def darPrimerayUltimasObra(lista):
    retorno = []
    if lt.size(lista) >= 6:
        n = 1
        while n < 4:
            obra = lt.getElement(lista, n)
            retorno.append(darInfoObra3(obra))
            n += 1
        n = lt.size(lista) - 2
        while n < lt.size(lista)+1:
            obra = lt.getElement(lista, n)
            retorno.append(darInfoObra3(obra))
            n += 1
    else:
        for obra in lt.iterator(lista):
            retorno.append(darInfoObra3(obra))
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

def darInfoObra2(catalog, obra):
    titulo = obra['Title']
    if titulo == "":
        titulo = "Unknown"
    if len(titulo) > 20:
        contador = 20
        while contador < len(titulo):
            if(titulo[contador-2] == ' '):
                titulo = titulo[:contador-1]+'\n'+titulo[contador-1:]
            else: 
                titulo = titulo[:contador]+'\n'+titulo[contador:]
            contador+=20
    fecha = obra['Date']
    if fecha == '':
        fecha = 'Unknown'
    fechaCompra = obra['DateAcquired']
    if fechaCompra == '':
        fechaCompra = 'Unknown'
    medio = obra['Medium']
    if medio == '':
        medio = 'Unknown'
    if len(medio) > 20:
        contador = 20
        while contador < len(medio):
            if (medio[contador-2]==' '):
                medio = medio[:contador-1]+'\n'+medio[contador-1:]
            else:
                medio = medio[:contador]+'\n'+medio[contador:]
            contador+=20
    dimensiones = obra['Dimensions']
    if dimensiones == '':
        dimensiones = 'Unknown'
    if len(dimensiones) > 22:
            contador = 22
            while contador < len(dimensiones):
                if(dimensiones[contador-2]==' '):
                    dimensiones = dimensiones[:contador-1]+'\n'+dimensiones[contador-1:]
                else:
                    dimensiones = dimensiones[:contador]+'\n'+dimensiones[contador:]
                contador+=22
    artistas = darArtistasObra(catalog, obra)
    if artistas == '':
        artistas = 'Unkwnown'
    return titulo, artistas, fecha, fechaCompra, medio, dimensiones

def darInfoObra3(obra):
    titulo = obra['Title']
    if titulo == "":
        titulo = "Unknown"
    if len(titulo) > 20:
        contador = 20
        while contador < len(titulo):
            if(titulo[contador-2] == ' '):
                titulo = titulo[:contador-1]+'\n'+titulo[contador-1:]
            else: 
                titulo = titulo[:contador]+'\n'+titulo[contador:]
            contador+=20
    fecha = obra['Date']
    if fecha == '':
        fecha = 'Unknown'
    medio = obra['Medium']
    if medio == '':
        medio = 'Unknown'
    if len(medio) > 20:
        contador = 20
        while contador < len(medio):
            if (medio[contador-2]==' '):
                medio = medio[:contador-1]+'\n'+medio[contador-1:]
            else:
                medio = medio[:contador]+'\n'+medio[contador:]
            contador+=20
    dimensiones = obra['Dimensions']
    if dimensiones == '':
        dimensiones = 'Unknown'
    if len(dimensiones) > 22:
            contador = 22
            while contador < len(dimensiones):
                if(dimensiones[contador-2]==' '):
                    dimensiones = dimensiones[:contador-1]+'\n'+dimensiones[contador-1:]
                else:
                    dimensiones = dimensiones[:contador]+'\n'+dimensiones[contador:]
                contador+=22
    return titulo, fecha, medio, dimensiones

def darInfoObra5(catalog,obra):
    titulo = obra['Title']
    if titulo == "":
        titulo = "Unknown"
    if len(titulo) > 20:
        contador = 20
        while contador < len(titulo):
            if(titulo[contador-2] == ' '):
                titulo = titulo[:contador-1]+'\n'+titulo[contador-1:]
            else: 
                titulo = titulo[:contador]+'\n'+titulo[contador:]
            contador+=20
    fecha = obra['Date']
    if fecha == '':
        fecha = 'Unknown'
    clasificacion = obra['Classification']
    if clasificacion == '':
        clasificacion = 'Unknown'
    medio = obra['Medium']
    if medio == '':
        medio = 'Unknown'
    if len(medio) > 20:
        contador = 20
        while contador < len(medio):
            if (medio[contador-2]==' '):
                medio = medio[:contador-1]+'\n'+medio[contador-1:]
            else:
                medio = medio[:contador]+'\n'+medio[contador:]
            contador+=20
    dimensiones = obra['Dimensions']
    if dimensiones == '':
        dimensiones = 'Unknown'
    if len(dimensiones) > 22:
            contador = 22
            while contador < len(dimensiones):
                if(dimensiones[contador-2]==' '):
                    dimensiones = dimensiones[:contador-1]+'\n'+dimensiones[contador-1:]
                else:
                    dimensiones = dimensiones[:contador]+'\n'+dimensiones[contador:]
                contador+=22
    artistas = darArtistasObra(catalog, obra)
    if artistas == '':
        artistas = 'Unkwnown'
    costo = obra['Costo']
    return titulo, artistas, clasificacion, fecha, medio, dimensiones, costo


def darArtistasObra(catalog, artwork):
    total = len(artwork['ConstituentID'])
    n = 0
    respuesta = ''
    for artista in lt.iterator(catalog['artists']):
        if artista['ConstituentID'] in artwork['ConstituentID']:
            respuesta += artista['DisplayName']+'\n'
            n += 1
        if n == total:
            return respuesta
    return respuesta
        
def darObrasDepartamento(catalog, nombre):
    dptos = catalog['departamentos']
    if mp.contains(dptos, nombre):
        entry=mp.get(dptos, nombre)
        obrasdpto=me.getValue(entry)
        for obra in lt.iterator(obrasdpto):
            darCostoObra(obra)
        return merge.sort(obrasdpto, compararObrasPorCosto)
    else:
        return False

def darCostosas(catalog,lista):
    respuesta = []
    n = 1
    while n <= 5:
        obra = lt.getElement(lista, n)
        respuesta.append(darInfoObra5(catalog,obra))
        n += 1
    return respuesta

def darViejas(catalog,lista):
    lista = merge.sort(lista, cmpArtworkByDate)
    respuesta = []
    n = 1
    while n <= 5:
        obra = lt.getElement(lista, n)
        respuesta.append(darInfoObra5(catalog,obra))
        n += 1
    return respuesta  
        
    

def buscarArtista(catalog, nombre):
    artistas = catalog['artists']
    for artista in lt.iterator(artistas):
        if artista['DisplayName'] == nombre:
            return artista
    return False

def darMediosArtista(catalog, artista):
    medios = catalog['mediums']
    iD = artista['ConstituentID']
    llaves = mp.keySet(medios)
    listanueva = lt.newList('ARRAY_LIST')
    for llave in lt.iterator(llaves):
        lista = lt.newList()
        entry=mp.get(medios, llave)
        obrasMedio=me.getValue(entry)
        for obra in lt.iterator(obrasMedio):
            if iD in obra['ConstituentID']:
                lt.addLast(lista, obra)
        if lt.size(lista) > 0:
            lt.addLast(listanueva,{'Medio':llave,'Obras':lista}) 
    return merge.sort(listanueva, cmpListasMedios)

                
def darPesoTotal(lista):
    peso = 0
    for i in lt.iterator(lista):
        if(i['Weight (kg)'] != ''):
            peso += float(i['Weight (kg)'])
    return peso

def darCostoObra(artwork):
    costo = 0
    if artwork['Weight (kg)'] != '':
        peso = float(artwork['Weight (kg)'])
    else:
        peso = 0
    tamano = 0
    alto = artwork['Height (cm)']
    largo = artwork['Length (cm)']
    ancho = artwork['Width (cm)']
    if alto != '':
        alto = float(alto)/100
        tamano = alto
        if largo != '':
            largo = float(largo)/100
            tamano *= largo
            if(ancho != ''):
                ancho = float(ancho)/100
                tamano *= ancho
        else:
            if(ancho != ''):
                ancho = float(ancho)/100
                tamano *= ancho
    elif largo != '':
        largo = float(largo)/100
        tamano = largo
        if ancho != '':
            ancho = float(ancho)/100
            tamano *= ancho
    elif ancho != '':
        ancho = float(ancho)/100
        tamano = ancho
    
    if(peso>0 or tamano > 0):
        if (peso * 72 >= tamano*72):
            costo = peso * 72
        else:
            costo = tamano *72
    else:
        costo = 48
    artwork['Costo'] = costo
    return costo

def darCostoLista(lista):
    costo = 0
    for i in lt.iterator(lista):
        costo += i['Costo']
    return costo


        
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

def cmpArtworkByDateAcquired(artwork1, artwork2):
    """
    Devuelve verdadero (True) si el 'Date' de artwork1 es menores que el de artwork2
    Args:
    artwork1: informacion de la primera obra que incluye su valor 'Date'
    artwork2: informacion de la segunda obra que incluye su valor 'Date'
    """
    obra1 = artwork1['DateAcquired']
    obra2 = artwork2['DateAcquired']
    if obra1=="":
        obra1=0
    elif obra2=="":
        obra2=0
    else:
        if obra1 < obra2:
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

def cmpListasMedios(l1,l2):
    lista1 = lt.size(l1['Obras'])
    lista2 = lt.size(l2['Obras'])
    if lista1 > lista2:
        return True
    else:
        return False
    
def compararObrasPorCosto(artwork1, artwork2):
    costo1 = artwork1['Costo']
    costo2 =artwork2['Costo']
    if(costo1 > costo2):
        return True
    else:
        return False


# Funciones de ordenamiento
def ordenarObrasPorFecha(lista):
    listadef=qk.sort(lista,cmpArtworkByDate)
    return listadef




