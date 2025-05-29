class ProgramaCapacitacion:
    __nombre: str
    __codigo: int
    __duracion: int
    def __init__(self, Nombre, Codigo, Duracion):
        self.__nombre = Nombre
        self.__codigo = Codigo
        self.__duracion = Duracion

    # Getters
    def getNombre(self):
        return self.__nombre
    
    def getCodigo(self):
            return self.__codigo

    def getDuracion(self):
        return self.__duracion