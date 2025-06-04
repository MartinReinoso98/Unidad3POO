from Planes import Planes
class Television(Planes):
    __canalesN : int
    __canalesI : int
    
    def __init__(self, nombreC, duracion, cobertura, precioBase, CanalesNac, CanalesInt):
        super().__init__(nombreC, duracion, cobertura, precioBase)
        self.__canalesN = CanalesNac
        self.__canalesI = CanalesInt
    
    # Getters
    def getCanalesNac(self):
        return self.__canalesN
    
    def getCanalesInt(self):
        return self.__canalesI
    
    def calculoFinal(self):
        importeFinal = 0
        importeFinal += super().getPrecioBase() * 1.15
        
        return importeFinal
        