# proyectoFinalPython

this is the final project of Python ADA Course

# Movie Catalog App

The Movie Catalog App is an application that allows users to manage a catalog of movies. Users can create, select, list, and delete movie catalogs, as well as add and list movies within each catalog.

## Table of Contents
1. Description
2. Getting Started
3. Usage
4. Features


 ## Getting Started
 Clone the repository:
 git clone https://github.com/vanessa2493/proyectoFinalPython/

Run the application by executing the app.py script:
- python app.py

## Usage
The Movie Catalog App provides the following options:

1. Add or Select Catalog: Create a new catalog or select an existing one by providing its name.
2. List Catalogs: Display the names of all available catalogs.
3. Add Movie: Add a movie to the selected catalog.
4. List Movies: List all movies in the selected catalog.
5. Delete Catalog: Delete the selected catalog along with its movies.
6. Exit: Exit the application.

   
## Features
- Create and manage multiple movie catalogs.
- Add movies to selected catalogs.
- List movies within a catalog.
- Delete catalogs along with their movies.

###  Variables
- opcion: Stores the user's selected menu option.
- catalogo: Holds the currently selected catalog instance.

### Libraries
- os: Used to interact with the operating system, including file operations.
- models: Contains the classes CatalogoPelicula and Pelicula defined in the models.py file.

### Functions
- CatalogoPelicula.__crearCatalogo(self, nombreCatalogo: str): Private method to create a new catalog file.
- CatalogoPelicula.verificarExistenciaCatalogo(self): Checks if the catalog file exists and creates it if not.
- CatalogoPelicula.agregarPelicula(self, pelicula: Pelicula): Adds a movie to the catalog.
- CatalogoPelicula.listarPeliculas(self): Lists the movies in the catalog.
- CatalogoPelicula.eliminarCatalogo(self): Deletes the catalog file.
  
