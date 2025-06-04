import csv
from Hoteles import Hotel

class ManejadorHotel:
    def __init__(self):
        self.__listaHoteles = []

    def agregarHotel(self, unHotel):
        self.__listaHoteles.append(unHotel)
        print("Hotel cargado")

    def cargarHoteles(self):
        with open("Hoteles.csv","r") as archivo:
            reader = csv.reader(archivo, delimiter=';')
            hotel = None
            for fila in reader:
                if len(fila) == 3:
                    hotel = Hotel(fila[0], fila[1], fila[2])
                    self.agregarHotel(hotel)
                elif len(fila) == 5 and hotel is not None:
                    num = int(fila[0])
                    piso = int(fila[1])
                    tipo = fila[2]
                    precio = float(fila[3])
                    disp = fila[4] == "True"
                    hotel.agregarHabitacion(num, piso, tipo, precio, disp)

    def incisoA(self, nomHotel):
        for hotel in self.__listaHoteles:
            if hotel.getNombre()== nomHotel:
                num = int(input("Ingrese el número de habitacion: "))
                piso = int(input("Ingrese el piso: "))
                tipo = input("Ingrese el tipo de habitacion: ")
                precio = float(input("Ingrese el precio por noche: $"))
                hotel.agregarHabitacion(num, piso, tipo, precio, True)

    def incisoB(self, nomHotel):
        for hotel in self.__listaHoteles:
            if hotel.getNombre() == nomHotel:
                habitaciones = hotel.getHabitaciones()
                numHabitacion = int(input("Ingrese el numero de habitacion: "))
                for hab in habitaciones:
                    if hab.getNumero() == numHabitacion:
                        if hab.getDisponibilidad():
                            hab.setDisponibilidad(False)
                            print("Habitacion reservada")
                        else:
                            print("Habitacion no disponible")


    def incisoC(self, nomHotel):
        for hotel in self.__listaHoteles:
            if hotel.getNombre() == nomHotel:
                numHabitacion = int(input("Ingrese el numero de la habitacion que desea liberar: "))
                hotel.liberarHabitacion(numHabitacion)
    
    def incisoD(self, tipo):
        encontrado = False
        for hotel in self.__listaHoteles:
            if hotel.mostrarNumeroYPiso(tipo, hotel.getNombre()):
                encontrado = True
        if not encontrado:
            print("No existen habitaciones con el tipo ingresado")

    def incisoE(self):
        for hotel in self.__listaHoteles:
            hotel.mostrarCantLibresPorPiso()


    def incisoF(self):
        for hotel in self.__listaHoteles:
            hotel.listarHabitaciones()
