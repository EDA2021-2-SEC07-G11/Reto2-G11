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


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Obras más antiguas por medio.")

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
        medio=input("Digite el medio utilizado por los artistas: ")
        numero=int(input("Digite el numero de obras que desea sacar: "))
        lista=controller.obrasmasantiguas(catalog,medio,numero)
        if lista==False:
            print("El medio no se encuentra en el catalogo.")
        else:
            print(lista)

        

    else:
        sys.exit(0)
sys.exit(0)
