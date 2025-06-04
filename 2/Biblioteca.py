class Biblioteca:
    __nombre: str
    __direccion: str
    __telefono: str
    __listaLibros: list

    def __init__(self, nom, dir, tel):
        self.__nombre = nom
        self.__direccion = dir
        self.__telefono = tel
        self.__listaLibros = []

    def agregarLibro(self, unLibro): # se recibe como parametro
        self.__listaLibros.append(unLibro)

    def getNombre(self):
        return self.__nombre
    
    def getDireccion(self):
        return self.__direccion
    
    def getTelefono(self):
        return self.__telefono
    
    def eliminarLibroPorISBN(self, isbn):
        bandera = False
        i = 0
        while not bandera and i < len(self.__listaLibros):
            if self.__listaLibros[i].getISBN() == isbn:
                del self.__listaLibros[i]
                bandera = True
            else:
                i += 1

        if bandera == True:
            print("\nLibro eliminado")

    def buscarLibroPorTitulo(self, titulo):
        i = 0
        while i < len(self.__listaLibros):
            if self.__listaLibros[i].getTitulo() == titulo:
                return self.__listaLibros[i]
            else:
                i += 1

    def mostrarLibros(self, nomBiblio):
        print()
        print(f"Libros de la {nomBiblio}")
        for libro in self.__listaLibros:
            print(f"- {libro.getTitulo()}")
            