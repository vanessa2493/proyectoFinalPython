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


class CatalogoPelicula(Pelicula):
    def __init__(self, nombreCatalogo, ruta_archivo, nombrePelicula):
        super().__init__(nombrePelicula)
        self.nombreCatalogo = nombreCatalogo
        self.ruta_archivo = ruta_archivo

    def __str__(self):
        return f"nombreCatalogo:{self.nombreCatalogo}, ruta_archivo: {self.ruta_archivo}"
