from Biblioteca import Biblioteca
from Libro import Libro
import csv

class ManejadorBiblioteca:
    __listaBibliotecas: list
    
    def __init__(self):
        self.__listaBibliotecas=[]
    
    def agregarBiblioteca(self,unaBiblioteca):
        self.__listaBibliotecas.append(unaBiblioteca)
        
    def cargarBiblioteca(self):
        i=-1
        with open("Biblioteca.csv", "r") as archivo:
            reader=csv.reader(archivo,delimiter=';')
            for fila in reader:
                if len(fila) == 3:
                    unaBiblio=Biblioteca(fila[0],fila[1],fila[2])
                    self.agregarBiblioteca(unaBiblio)
                    i+=1
                else:
                    Titulo=fila[0]
                    Autor=fila[1]
                    Isbn=fila[2]
                    Genero=fila[3]
                    unLibro=Libro(Titulo,Autor,Isbn,Genero)
                    self.__listaBibliotecas[i].agregarLibro(unLibro)
        archivo.close()
                    
    def incisoA(self, nombreBib):
        i=0
        bandera = False
        while not bandera and i < len(self.__listaBibliotecas):
            if self.__listaBibliotecas[i].getNombre == nombreBib:
                TituloAg=input("Ingrese el nombre titulo del libro a agregar: ")
                AutorAg=input("Ingrese el autor del libro a agregar: ")
                IsbnAg=input("Ingrese el ISBN del libro a agregar: ")
                GeneroAg=input("Ingrese el genero del libro a agregar: ")
                unLibro=Libro(TituloAg,AutorAg,IsbnAg,GeneroAg)
                self.__listaBibliotecas[i].agregarLibro(unLibro)
                bandera = True
            else:
                i+=1
                
    def incisoB(self,nombreBiblio,nombreLibr):
        i=0
        bandera = False
        while not bandera and i < len(self.__listaBibliotecas):
            if self.__listaBibliotecas[i].getNombre == nombreBiblio:
                bandera = True
                self.__listaBibliotecas[i].eliminarLibro(nombreLibr)
            else:
                i+=1
    
    def incisoC(self,tituloLibro):
        i=0
        j=0
        bandera = False
        while not bandera and i < len(self.__listaBibliotecas):
            while j < len(Biblioteca.__listaLibros):
                if Biblioteca.__listaLibros[j].getTitulo == tituloLibro:
                    bandera = True
                    print(f"Nombre de la biblioteca: {self.__listaBibliotecas[i].getNombre}")
                    print(f"Autor: {Biblioteca.__listaLibros[j].getAutor}")
                    print(f"Genero: {Biblioteca.__listaLibros[j].getGenero}")
                else:
                    j+=1
            i+=1
    
    def incisoD(self):
        for biblioteca in self.__listaBibliotecas:
            print(f"Nombre de la biblioteca: {biblioteca.getNombre()}")
            print(f"Direccion: {biblioteca.getDireccion()}")
            print(f"Telefono: {biblioteca.getTelefono()}")
            print("Libros disponibles:")
            for libro in Biblioteca.__listaLibros:
                print(f" Titulo: {libro.getTitulo()} escrito por: {libro.getAutor()} con ISBN: {libro.getIsbn()} y del genero: {libro.getGenero()})")
            print("\n")