from Habitacion import Habitacion

class Hotel:
    def __init__(self, nombre, direccion, ciudad):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__ciudad = ciudad
        self.__habitaciones = []

    def getNombre(self):
        return self.__nombre

    def getDireccion(self):
        return self.__direccion

    def getCiudad(self):
        return self.__ciudad
   
    def getHabitaciones(self):
        return self.__habitaciones

    def agregarHabitacion(self, numero, piso, tipo, precio, disponible):
        habitacion = Habitacion(numero, piso, tipo, precio, disponible)
        self.__habitaciones.append(habitacion)
        
    def liberarHabitacion(self, numero):
        for habitacion in self.__habitaciones:
            if habitacion.getNumero() == numero:
                if habitacion.getDisponibilidad():
                    print("La habitacion ya esta libre")
                else:
                    habitacion.setDisponibilidad(True)
                    print("Habitacion liberada exitosamente")
    
    def mostrarNumeroYPiso(self, tipo, nombre):
        encontrado = False
        for habitacion in self.__habitaciones:
            if habitacion.getTipo() == tipo:
                print(f"Hotel: {nombre}, Habitación: {habitacion.getNumero()}, Piso: {habitacion.getPiso()}")
                encontrado = True
        return encontrado
    
    def mostrarCantLibresPorPiso(self):
        print(f"---Hotel--- {self.getNombre()}")
        for piso in range(1, 5):
            cont = 0
            for habitacion in self.__habitaciones:
                if habitacion.getPiso() == piso and habitacion.getDisponibilidad():
                    cont += 1
            print(f"Piso {piso}: {cont} habitaciones libres")


    def listarHabitaciones(self):
        print(f"{'Número':<15}{'Piso':<10}{'Precio por noche':<20}{'Disponibilidad':<15}")
        for habitacion in self.getHabitaciones():
            numero = habitacion.getNumero()
            piso = habitacion.getPiso()
            precio = habitacion.getPrecio()
            disponible = "Libre" if habitacion.getDisponibilidad() else "Ocupada"
            print(f"{numero:<15}{piso:<10}{precio:<20}{disponible:<15}")



