class Empleado:
    __nombreYap: str
    __idEmpleado: int
    __puesto: str
    
    def __init__(self,NombreYAp,IdEmpleado,Puesto):
        self.__nombreYap = NombreYAp
        self.__idEmpleado = IdEmpleado
        self.__puesto = Puesto

    #Getters
    def getNombreYAp(self):
        return self.__nombreYap

    def getIdEmpleado(self):
        return self.__idEmpleado

    def getPuesto(self):
        return self.__puesto