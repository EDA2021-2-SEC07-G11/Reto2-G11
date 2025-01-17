﻿"""
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
 """

import config as cf
import model
import csv
import time



"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadArtists(catalog)
    loadArtworks(catalog)


def loadArtists(catalog):
    """
    Carga los artistas del archivo. 
    """
    artistsFile = cf.data_dir + 'MoMA/Artists-utf8-50pct.csv'
    input_file = csv.DictReader(open(artistsFile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)

def loadArtworks(catalog):
    """
    Carga todas las obras de arte del archivo
    """
    artworksFile = cf.data_dir + 'MoMA/Artworks-utf8-50pct.csv'
    input_file = csv.DictReader(open(artworksFile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtwork(catalog, artwork)






# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
def obrasNacionalidad(catalog, nationality):
    return model.darObrasNacionalidad(catalog, nationality)

def obrasmasantiguas(catalog,medio,numero):
    lista=model.obrasmasantiguas(catalog,medio,numero)
    return lista

def darArtistasRango(catalog, inicio, fin):
    return model.darArtistasRango(catalog, inicio, fin)

def darObrasRango(catalog, inicio, fin):
    return model.darObrasRango(catalog, inicio, fin)

def darObrasCompradas(lista):
    return model.obrasCompradas(lista)

def darInfoArtistas1(lista):
    return model.darViejosyJovenes(lista)

def darInfoObras2(catalog,lista):
    return model.darViejosyJovenesObra(catalog, lista)

def darInfoObras3(lista):
    return model.darPrimerayUltimasObra(lista)

def darInfoObras5(catalog,lista):
    return model.darCostosas(catalog, lista)

def darInfoObrasViejas(catalog,lista):
    return model.darViejas(catalog, lista)

def buscarArtista(catalog, nombre):
    return model.buscarArtista(catalog, nombre)

def darMediosArtista(catalog, artist):
    return model.darMediosArtista(catalog, artist)

def darObrasDepartamento(catalog, nombre):
    return model.darObrasDepartamento(catalog, nombre)

def costoLista(lista):
    return model.darCostoLista(lista)

def pesoLista(lista):
    return model.darPesoTotal(lista)