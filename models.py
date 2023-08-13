# Import libraries

import os


# Create class Pelicula and CatalogoPelicula

class Pelicula:

    def __init__(self, nombrePelicula: str):
        self.__nombrePelicula = nombrePelicula

    def __str__(self):
        return f"nombrePelicula:{self.nombrePelicula}"

    @property
    def nombrePelicula(self):
        return self.__nombrePelicula

    @nombrePelicula.setter
    def nombrePelicula(self, nombrePelicula):
        self.__nombrePelicula = nombrePelicula


class CatalogoPelicula:

    def __init__(self, nombreCatalogo: str):
        self.nombreCatalogo = nombreCatalogo
        self.ruta_archivo = f'{self.nombreCatalogo}.txt'

    def __str__(self):
        return f"nombreCatalogo:{self.nombreCatalogo}, ruta_archivo: {self.ruta_archivo}"

    def __crearCatalogo(self, nombreCatalogo: str):
        with open(f'{nombreCatalogo}.txt', 'a+') as file:
            file.write(f'{self.nombreCatalogo}\n')

    def verificarExistenciaCatalogo(self):
        if os.path.exists(f'{self.nombreCatalogo}.txt'):
            print(f'El catálogo {self.nombreCatalogo} ya existe\n')
        else:
            self.__crearCatalogo(self.nombreCatalogo)
            print(f'Se creó el catálogo: {self.nombreCatalogo}\n')

    def agregarPelicula(self, pelicula: Pelicula):

        self.verificarExistenciaCatalogo()

        with open(f'{self.nombreCatalogo}.txt', 'a+') as file:
            file.write(f'{pelicula.nombrePelicula}\n')

    def listarPeliculas(self):
        with open(f'{self.nombreCatalogo}.txt', 'r') as file:
            for line in file:
                print(line.strip())

    def eliminarCatalogo(self):
        os.remove(f'{self.nombreCatalogo}.txt')
        print(f'El catálogo {self.nombreCatalogo} ha sido eliminado\n')


# catalogo = CatalogoPelicula("catalogo1")

# catalogo.verificarExistenciaCatalogo()

# catalogo.eliminarCatalogo()
