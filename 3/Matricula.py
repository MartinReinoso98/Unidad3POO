class Matricula:
    __fecha = str
    __empleado: object
    __programa: object

    def __init__(self, Fecha, Empleado, Programa):
        self.__fecha = Fecha
        self.__empleado = Empleado
        self.__programa = Programa
    
    # Getters
    def getFecha(self):
        return self.__fecha

    def getEmpleado(self):
        return self.__empleado

    def getPrograma(self):
        return self.__programa
