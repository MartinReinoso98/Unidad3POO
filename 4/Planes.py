import abc
from abc import ABC

class Planes(ABC):
    __nombreC : str
    __duracion : int
    __cobertura : str
    __precioBase : float
    
    def __init__(self,NombreC,Duracion,Cobertura,PrecioBase):
        self.__nombreC=NombreC
        self.__duracion=Duracion
        self.__cobertura=Cobertura
        self.__precioBase=PrecioBase
        
    # Getters
    def getNombreComp(self):
        return self.__nombreC
    
    def getDuracion(self):
        return self.__duracion
    
    def getCobertura(self):
        return self.__cobertura
    
    def getPrecioBase(self):
        return self.__precioBase
    
    def __str__(self):
        return f"Plan {self.__nombreC} - Duracion {self.__duracion} meses - Cobertura {self.__cobertura} - Precio base {self.__precioBase}"
    
    @abc.abstractmethod 
    def calculoFinal(self):
        pass
    
    def mostrarPlanes(self):
        print(f"Nombre de la compania: {self.getNombreComp()}")
        print(f"Duracion del plan: {self.getDuracion()} meses")
        print(f"Cobertura geografica: {self.getCobertura()}")
        print(f"Importe final: {self.calculoFinal():.2f}")
        print("-----------------------------")