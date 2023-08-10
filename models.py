# Create class Pelicula and CatalogoPelicula

class Pelicula:

    def __init__(self, nombrePelicula):
        self.__nombrePelicula: nombrePelicula

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

    def crearCatalogo(self, nombreCatalogo: str):
        with open(f'{nombreCatalogo}.txt', 'a+') as file:
            file.write(f'{self.ruta_archivo}\n')

    def agregarPelicula(self):

        pass

    def listarPeliculas(self):
        pass

    def eliminarCatalogo(self):
        pass


catalogoPrueba = CatalogoPelicula("catalogo1")

catalogoPrueba.crearCatalogo("catalogo1")
