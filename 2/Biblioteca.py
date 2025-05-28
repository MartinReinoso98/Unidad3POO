from Libro import Libro
class Biblioteca:
    __nombre: str
    __direccion: str
    __telefono: str
    __listaLibros: list
    
    def __init__(self, Nombre, Direccion, Telefono):
        self.__nombre = Nombre
        self.__direccion = Direccion
        self.__telefono = Telefono
        self.__listaLibros = []
    
    def getNombre(self):
        return self.__nombre
    
    def getDireccion(self):
        return self.__direccion
    
    def getTelefono(self):
        return self.__telefono
    
    def agregarLibro(self, unLibro):
        self.__listaLibros.append(unLibro)
        
    def eliminarLibro(self,nombreLibr):
        i=0
        bandera = False
        while not bandera and i < len(self.__listaLibros):
            if self.__listaLibros[i].getTitulo == nombreLibr:
                del self.__listaLibros[i]
                print(f"Libro con el titulo {nombreLibr} eliminado")
            else:
                i+=1
        print(f"No se encontro el libro {nombreLibr} eliminar")
            