class Libro:
    __titulo:str
    __autor:str
    __isbn:str
    __genero:str

    def __init__(self,Titulo,Autor,Isbn,Genero):
        self.__titulo=Titulo
        self.__autor=Autor
        self.__isbn=Isbn
        self.__genero=Genero
        
    def getTitulo(self):
        return self.__titulo
    
    def getAutor(self):
        return self.__autor
    
    def getIsbn(self):
        return self.__isbn
    
    def getGenero(self):
        return self.__genero