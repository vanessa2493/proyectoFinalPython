# Import models.py

import models

# App

print("_______________________")
print("Catálogo de Películas")
print("_______________________")

opcion = 0

while opcion != 4:
    print("Seleccione una de las siguientes opciones\n",
          "1: Agregar película\n",
          "2: Listar películas\n",
          "3: Eliminar catálogo películas\n",
          "4: Salir\n")

    opcion = int(input('Ingrese una opción: '))

    if (opcion == 1):
        print("agregar pelicula\n")
    elif (opcion == 2):
        print("listar pelicula\n")
    elif (opcion == 3):
        print("eliminar cat pelicula\n")
    elif (opcion == 4):
        print("salir\n")
    else:
        print("\nOpción incorrecta, elija una opción del 1 al 4.")
