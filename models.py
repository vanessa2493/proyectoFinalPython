# Import libraries

import os


# Create class Pelicula and CatalogoPelicula

class Pelicula:
    """
    Represents a movie with a given name.

    This class provides a simple representation of a movie with its name.
    The movie name can be set and retrieved using the 'nombrePelicula' property.

    Attributes:
        __nombrePelicula (str): The private attribute to store the name of the movie.

    Methods:
        __init__(self, nombrePelicula: str): Initializes a Pelicula instance with the given movie name.
        __str__(self): Returns a string representation of the Pelicula object.

    Properties:
        nombrePelicula (str): Gets or sets the name of the movie.

    """

    def __init__(self, nombrePelicula: str):
        """
        Initializes a Pelicula instance with the given movie name.

        Args:
            nombrePelicula (str): The name of the movie.
        """
        self.__nombrePelicula = nombrePelicula

    def __str__(self):
        """
        Returns a string representation of the Pelicula object.

        Returns:
            str: A string in the format "nombrePelicula:<movie_name>".
        """
        return f"nombrePelicula:{self.nombrePelicula}"

    @property
    def nombrePelicula(self):
        """
        Gets the name of the movie.

        Returns:
            str: The name of the movie.
        """
        return self.__nombrePelicula

    @nombrePelicula.setter
    def nombrePelicula(self, nombrePelicula):
        """
        Sets the name of the movie.

        Args:
            nombrePelicula (str): The new name for the movie.
        """
        self.__nombrePelicula = nombrePelicula


class CatalogoPelicula:
    """
    Represents a catalog of movies.

    This class provides functionality to manage a catalog of movies.
    Movies can be added to the catalog, listed, and the catalog itself can be deleted.

    Attributes:
        nombreCatalogo (str): The name of the catalog.
        ruta_archivo (str): The file path where the catalog data is stored.

    Methods:
        __init__(self, nombreCatalogo: str): Initializes a CatalogoPelicula instance with the given catalog name.
        __str__(self): Returns a string representation of the CatalogoPelicula object.
        __crearCatalogo(self, nombreCatalogo: str): Private method to create a new catalog file.
        verificarExistenciaCatalogo(self): Checks if the catalog file exists and creates it if not.
        agregarPelicula(self, pelicula: Pelicula): Adds a movie to the catalog.
        listarPeliculas(self): Lists the movies in the catalog.
        eliminarCatalogo(self): Deletes the catalog file.

    """

    def __init__(self, nombreCatalogo: str):
        """
        Initializes a CatalogoPelicula instance with the given catalog name.

        Args:
            nombreCatalogo (str): The name of the catalog.
        """
        self.nombreCatalogo = nombreCatalogo
        self.ruta_archivo = f'{self.nombreCatalogo}.txt'

    def __str__(self):
        """
        Returns a string representation of the CatalogoPelicula object.

        Returns:
            str: A string with the catalog name and file path.
        """
        return f"nombreCatalogo:{self.nombreCatalogo}, ruta_archivo: {self.ruta_archivo}"

    def __crearCatalogo(self, nombreCatalogo: str):
        """
        Private method to create a new catalog file.

        Args:
            nombreCatalogo (str): The name of the catalog.
        """
        with open(f'{nombreCatalogo}.txt', 'a+') as file:
            file.write(f'{self.nombreCatalogo}\n')

    def verificarExistenciaCatalogo(self):
        """
        Checks if the catalog file exists and creates it if not.
        """
        if os.path.exists(f'{self.nombreCatalogo}.txt'):
            print(f'El catálogo {self.nombreCatalogo} ya existe\n')
        else:
            self.__crearCatalogo(self.nombreCatalogo)
            print(f'Se creó el catálogo: {self.nombreCatalogo}\n')

    def agregarPelicula(self, pelicula: Pelicula):
        """
        Adds a movie to the catalog.

        Args:
            pelicula (Pelicula): The movie object to add to the catalog.
        """
        self.verificarExistenciaCatalogo()

        with open(f'{self.nombreCatalogo}.txt', 'a+') as file:
            file.write(f'{pelicula.nombrePelicula}\n')

    def listarPeliculas(self):
        """
        Lists the movies in the catalog.
        """
        with open(f'{self.nombreCatalogo}.txt', 'r') as file:
            lines = file.readlines()
            if len(lines) > 1:
                print("Las películas en este catálogo son: \n")
                for line in lines[1:]:
                    print(line.strip())
                print("\n")
            else:
                print("No hay películas en este catálogo")

    def eliminarCatalogo(self):
        """
        Deletes the catalog file.
        """
        os.remove(f'{self.nombreCatalogo}.txt')
        print(f'El catálogo {self.nombreCatalogo} ha sido eliminado\n')
