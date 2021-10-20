"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from DISClib.ADT import map as mp
from tabulate import tabulate
from DISClib.DataStructures import mapentry as me


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Dar Artistas en un rango de años de nacimiento")
    print("3- Dar Obras en un rango de fecha de compra")
    print("4- Obras de un artista por medio.")
    print("5- Número de obras de una nacionalidad")

catalog = None

def initCatalog():
    """
    Inicializa el catalogo
    """
    return controller.initCatalog()
    
def loadData(catalog):
    """
    Carga los datos en la estructura de datos
    """
    controller.loadData(catalog)

def printartwork(artwork):
    print('Titulo: ' + artwork['Title'] )

def printartworkFecha(artwork):
    print('Titulo: ' + artwork['Obra']['Title'] + '. Fecha de adquisición: '+ artwork['Obra']['DateAcquired'] )

def printarworkInfo(artwork):
    print()

def printartist(artist):
    print('Nombre: ' + artist['DisplayName'])


def imprimir_ultimostresworks(lista):
    print("Estas son las ultimas tres obras: ")
    contador=0
    puesto=lt.size(lista)
    while contador<3:
        printartwork(lt.getElement(lista,puesto))
        puesto+=-1
        contador+=1

def imprimir_ultimostresworksFecha(lista):
    print("Estas son las últimas tres obras: ")
    contador=0
    puesto=lt.size(lista) - 2
    while contador<3:
        printartworkFecha(lt.getElement(lista,puesto))
        puesto+=1
        contador+=1


def imprimir_primerostresworksFecha(lista):
    print("Estas son las primeras tres obras: ")
    contador=0
    puesto=1
    while contador<3:
        printartworkFecha(lt.getElement(lista,puesto))
        puesto+=1
        contador+=1

def imprimir_ultimostresartist(lista):
    print("Estas son los ultimos tres artistas: ")
    contador=0
    puesto=lt.size(lista)
    while contador<3:
        printartist(lt.getElement(lista,puesto))
        puesto+=-1
        contador+=1
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        catalog = initCatalog()
        loadData(catalog)
        print('Obras Cargadas: ' + str(lt.size(catalog['artworks'])))
        lista=catalog["artworks"]
        imprimir_ultimostresworks(lista)
        print('Artistas cargados: ' + str(lt.size(catalog['artists'])))
        lista=catalog["artists"]
        imprimir_ultimostresartist(lista)
    
    elif int(inputs[0]) == 2:
        inicio=input("Ingrese el año inicial de nacimiento: ")
        if (inicio.isnumeric() == False) :
            print("Ha ingresado un año inválido")
        else:
            inicio = int(inicio)
            fin = input("Ingrese el año final de nacimiento: ")
            if (fin.isnumeric() == False or int(fin)< inicio) :
                print("Ha ingresado un año inválido")
            else:
                fin = int(fin)
                lista = controller.darArtistasRango(catalog,inicio,fin)
                if(lt.isEmpty(lista)):
                    print("No hay artistas en este rango")
                else:
                    artistas = controller.darInfoArtistas1(lista)
                    print("Hay " + str(lt.size(lista))+" artistas nacidos entre " +str(inicio)+" y "+str(fin))
                    print('Los 3 primeros y últimos artistas en el rango son:')
                    print(tabulate(artistas, headers=['DisplayName', 'BeginDate','EndDate','Nationality','Gender'], tablefmt='fancy_grid'))

    elif int(inputs[0]) == 3:
        inicio=input("Ingrese el año inicial de compra en formato AAAA-MM-DD: ")
        formato = inicio.split('-')
        if (len(formato) != 3 or len(formato[0]) != 4 or len(formato[1]) != 2 or len(formato[2]) != 2):
            print('Ha ingresado una fecha inicial inválida')
        else:
            fin = input('Ingrese el año final de compra en formato AAAA-MM-DD: ')
            formato = fin.split('-')
            if(len(formato) != 3 or len(formato[0]) != 4 or len(formato[1]) != 2 or len(formato[2]) != 2 or inicio > fin):
                print('Ha ingresado una fecha final inválida')
            else:
                lista = controller.darObrasRango(catalog, inicio, fin)
                artistas = controller.darInfoObras2(catalog, lista)
                print('El MOMA adquirió '+str(lt.size(lista))+ ' piezas únicas entre '+inicio+ ' y '+fin)
                print('De las cuales compró '+ str(controller.darObrasCompradas(lista)))
                print('Las 3 primeras y últimas obras en el rango son:')
                print(tabulate(artistas, headers=['Title', 'ArtistsName','Date','DateAcquired','Medium','Dimensions'], tablefmt='fancy_grid'))

    elif int(inputs[0]) == 4:
        nombre=input("Digite el nombre del artista: ")
        artista = controller.buscarArtista(catalog, nombre)
        if artista != False:
            lista = controller.darMediosArtista(catalog, artista)
            respuesta = []
            totalObras = 0
            n = 0
            for medio in lt.iterator(lista):
                totalObras += lt.size(medio['Obras']) 
                respuesta.append([medio['Medio'],lt.size(medio['Obras'])])
                n += 1
                if n == 5:
                    break
            print(artista['DisplayName']+' con ID de MOMA '+artista['ConstituentID']+' tiene '+str(totalObras)+' a su nombre en el museo')
            print('En su trabajo hay presentes '+str(lt.size(lista))+' medios/técnicas')
            print('Su top 5 de medios/técnicas son: ')
            print(tabulate(respuesta, headers=['MediumName', 'Count'], tablefmt='fancy_grid'))
            primerMedio = lt.firstElement(lista)
            print('Su medio más utilizado es: '+ primerMedio['Medio']+ ' con '+ str(lt.size(primerMedio['Obras']))+' piezas')
            print('Las primeras y últimas 3 obras de esta técnica son: ')
            info = controller.darInfoObras3(primerMedio['Obras'])
            print(tabulate(info, headers=['Title', 'Date','Medium','Dimensions'], tablefmt='fancy_grid'))
        else:
            print('Este artista no se encuentra en nuestra base de datos')

    elif int(inputs[0]) == 5:
        nacionalidad=input("Digite la nacionalidad buscada: \n ")
        lista=controller.obrasNacionalidad(catalog, nacionalidad)
        if lista==None:
            print("La nacionalidad no encuentra en el catalogo.")
        else:
            print('La nacionalidad '+ nacionalidad + ' contiene '+str(lt.size(lista))+' obras')

    else:
        sys.exit(0)
sys.exit(0)
