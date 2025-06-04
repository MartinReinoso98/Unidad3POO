class Habitacion:
    def __init__(self, numero, piso, tipo, precio, disponible):
        self.__numero = numero
        self.__piso = piso
        self.__tipo = tipo
        self.__precio = precio
        self.__disponibilidad = disponible

    def setDisponibilidad(self, disp):
        self.__disponibilidad = disp

    def getNumero(self):
        return self.__numero

    def getPiso(self):
        return self.__piso

    def getTipo(self):
        return self.__tipo

    def getPrecio(self):
        return self.__precio

    def getDisponibilidad(self):
        return self.__disponibilidad

    def __str__(self):
        estado = "Libre" if self.__disponibilidad else "Ocupada"
        return f"Habitación {self.__numero} - Piso {self.__piso} - Tipo: {self.__tipo} - Estado: {estado}"
