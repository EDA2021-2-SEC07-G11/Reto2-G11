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
    start_time = time.process_time()
    loadArtists(catalog)
    loadArtworks(catalog)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    print(elapsed_time_mseg)


def loadArtists(catalog):
    """
    Carga los artistas del archivo. 
    """
    artistsFile = cf.data_dir + 'MoMA/Artists-utf8-large.csv'
    input_file = csv.DictReader(open(artistsFile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)

def loadArtworks(catalog):
    """
    Carga todas las obras de arte del archivo
    """
    artworksFile = cf.data_dir + 'MoMA/Artworks-utf8-large.csv'
    input_file = csv.DictReader(open(artworksFile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtwork(catalog, artwork)



def obrasmasantiguas(catalog,medio,numero):
    lista=model.obrasmasantiguas(catalog,medio,numero)
    return lista


# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
def obrasNacionalidad(catalog, nationality):
    return model.darObrasNacionalidad(catalog, nationality)