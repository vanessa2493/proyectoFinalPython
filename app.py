# Import models.py

from models import CatalogoPelicula as cp
from models import Pelicula

# Import Libaries

import os

## App ##

print("***********************")
print(" Catálogo de Películas")
print("***********************\n")

# Initialize variables

opcion = 0
catalogo = None

# Starting app menu

while opcion != 6:
    if catalogo == None:
        print("______________________________________")
        print('\nDebe crear o seleccionar un catálogo\n')
    else:
        print(f'El catálogo seleccionado es {catalogo.nombreCatalogo}\n')

    print("Seleccione una de las siguientes opciones\n",
          "1: Agregar o seleccionar catálogo\n",
          "2: Listar catálogos\n",
          "3: Agregar película\n",
          "4: Listar películas\n",
          "5: Eliminar catálogo películas\n",
          "6: Salir\n")

    opcion = input('Ingrese una opción: ')
    opcion = int(opcion)

    if (opcion == 1):
        print("Agregar o seleccionar catálogo\n")
        catalogo = cp(input("Ingrese el nombre del catálogo: \n"))
        cp.verificarExistenciaCatalogo(catalogo)

    elif (opcion == 2):
        print("Los catálogos disponibles son: \n")
        txt_files = [file for file in os.listdir(
            "./") if os.path.splitext(file)[1] == ".txt"]
        print(txt_files, '\n')

    elif (opcion == 3):
        try:
            print("Agregar pelicula\n")
            cp.agregarPelicula(catalogo, Pelicula(input(
                "Ingrese el nombre de la película: \n")))
        except:
            print("No ha seleccionado ningún catálogo")

    elif (opcion == 4):
        try:
            print("Listar peliculas\n")
            cp.listarPeliculas(catalogo)
        except:
            print("No ha seleccionado ningún catálogo")

    elif (opcion == 5):
        try:
            print("Eliminar catálogo películas\n")
            print(
                f"¿Está segurx que desea eliminar el catálogo: {catalogo.nombreCatalogo}? ")
            opcion_eliminar = input("si/no\n")

            if (opcion_eliminar == "si"):
                cp.eliminarCatalogo(catalogo)
                catalogo = None
            elif (opcion_eliminar == "no"):
                print("No ha eliminado ningún catálogo")
            else:
                print("Elija una opción correcta: si/no")
        except:
            print("No ha seleccionado ningún catálogo")

    elif (opcion == 6):
        print("Ha salido de la aplicación\n")

    else:
        print("\nOpción incorrecta, elija una opción del 1 al 6.")
