from Planes import Planes
class Telefonia(Planes):
    __tipoLlamadas: str
    __cantMin: int
    
    def __init__(self, nombreC, duracion, cobertura, precioBase, TipoLlamada, CantMin):
        super().__init__(nombreC, duracion, cobertura, precioBase)
        self.__tipoLlamadas = TipoLlamada
        self.__cantMin = CantMin
        
    # Getters   
    def getTipoLlamada(self):
        return self.__tipoLlamadas
    
    def getCantMin(self):
        return self.__cantMin
    
    def calculoFinal(self):
        importeFinal = 0
        
        if super().getCobertura() == "Nacional e Internacional":
            importeFinal += super().getPrecioBase() * 1.20
        
        elif super().getCobertura() == "Nacional":
            importeFinal += super().getPrecioBase() * 1.20
            
        elif super().getCobertura() == "Locales":
            importeFinal += super().getPrecioBase() * 0.925
        
        return importeFinal