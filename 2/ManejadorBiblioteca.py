import csv
from Biblioteca import Biblioteca
from Libro import Libro

class ManejadorBiblioteca:
    __listaBiblioteca: list

    def __init__(self):
        self.__listaBiblioteca = []

    def agregarBiblioteca(self, unaBiblio):
        self.__listaBiblioteca.append(unaBiblio)
        
    def cargarBibliotecas(self):
        archivo = open('Biblioteca.csv', "r")
        reader = csv.reader(archivo, delimiter=';')
        biblioteca = None  # inicializa
        
        for fila in reader:
            if len(fila) == 3:
                biblioteca = Biblioteca(fila[0], fila[1], fila[2])
                self.agregarBiblioteca(biblioteca)

            elif len(fila) == 4 and biblioteca is not None:
                libro = Libro(fila[0], fila[1], fila[2], fila[3])
                biblioteca.agregarLibro(libro)

        archivo.close()

    def buscarBiblioteca(self, nomBiblio):
        i = 0
        while i < len(self.__listaBiblioteca):
            if self.__listaBiblioteca[i].getNombre() == nomBiblio:
                return self.__listaBiblioteca[i]
            else:
                i += 1
            
    def incisoA(self, nomBiblio):
        biblio = self.buscarBiblioteca(nomBiblio)
        if biblio is not None:
            titulo = input("Ingrese el titulo del libro: ")
            autor = input("Ingrese el autor: ")
            isbn = input("Ingrese el ISBN: ")
            genero = input("Ingrese el genero: ")
            unLibro = Libro(titulo, autor, isbn, genero)
            biblio.agregarLibro(unLibro)

    def incisoB(self, nomBiblio, isbn):
        biblio = self.buscarBiblioteca(nomBiblio)
        if biblio:
            biblio.eliminarLibroPorISBN(isbn)

    def incisoC(self, titulo):
        bandera = False
        for biblio in self.__listaBiblioteca: # con for en caso de que mas de una biblioteca tenga el mismo libro
            libro = biblio.buscarLibroPorTitulo(titulo)
            if libro is not None:
                print(f"- Biblioteca en la que se encuentra: {biblio.getNombre()}")
                print(f"- Autor: {libro.getAutor()}")
                print(f"- Genero: {libro.getGenero()}")
                print(f"- ISBN: {libro.getISBN()}")
                bandera = True

        if not bandera:
            print("No se encontro el libro con el titulo ingresado")

    def incisoD(self):
        for biblio in self.__listaBiblioteca:
            biblio.mostrarLibros(biblio.getNombre())