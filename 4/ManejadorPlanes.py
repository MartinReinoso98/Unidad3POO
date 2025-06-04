import csv
from Planes import Planes
from Telefonia import Telefonia
from Television import Television

class ManejadorPlanes:
    __ListaPlanes: list
    
    def __init__(self):
        self.__ListaPlanes = []

    def cargarPlanes(self):
        with open("planes.csv", "r") as archivo:
            reader = csv.reader(archivo,delimiter=";")
            next(reader)
            for fila in reader:
                try:
                    if fila[0] == 'T':
                        unPlanTelevision = Television(fila[1],int(fila[2]),fila[3],int(fila[4]),int(fila[7]),int(fila[8]))
                        self.__ListaPlanes.append(unPlanTelevision)
                    elif fila[0] == 'M':
                        unPlanTelefonia = Telefonia(fila[1],int(fila[2]),fila[3],int(fila[4]),fila[5],int(fila[6]))
                        self.__ListaPlanes.append(unPlanTelefonia)
                except IndexError:
                    print("Error en una posicion de una fila")
            archivo.close()

    def mostrarPlanes(self):
        longitud = len(self.__ListaPlanes)
        for i in range(longitud):
            print(self.__ListaPlanes[i])
        
    def incisoA(self, posicion):
        if (isinstance(self.__ListaPlanes[posicion], Telefonia)):
            print(f"Tipo de plan: {self.__ListaPlanes[posicion]}")
        else:
            if (isinstance(self.__ListaPlanes[posicion], Television)):
                print(f"Tipo de plan: {self.__ListaPlanes[posicion]}")    

    def incisoB(self,cobertura):
        cont = 0
        longitud = len(self.__ListaPlanes)
        for i in range(longitud):
            if cobertura == self.__ListaPlanes[i].getCobertura():
                print(f"El plan es: {self.__ListaPlanes[i].getNombreComp()}")
                cont += 1

        print("La cantidad de planes en la cobertura", cobertura, "son:", cont)
    
    def incisoC(self, cantidad):
        for plan in self.__ListaPlanes:
            if isinstance(plan, Television) and plan.getCanalesInt() >= cantidad:
                print(f"El nombre de la compañía que ofrece la misma cantidad o mas canales internacionales es: {plan.getNombreComp()}")


    def incisoD(self):
        for plan in self.__ListaPlanes:
            plan.mostrarPlanes()
