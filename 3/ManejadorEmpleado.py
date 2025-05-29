import csv
from Empleado import Empleado

class ManejadorEmpleado:
    __ListaEmpleados: list

    def __init__(self):
        self.__ListaEmpleados = []

    def cargarEmpleado(self):
        with open("empleados.csv", "r") as archivo:
            reader = csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader:
                NombreYApellido=fila[0]
                IdEmp=int(fila[1])
                PuestoEmp=fila[2]
                unEmpleado = Empleado(NombreYApellido,IdEmp,PuestoEmp)
                self.__ListaEmpleados.append(unEmpleado)
        archivo.close()
        
    def buscarEmpleado(self,nombre):
        i=0
        bandera=False
        objetoEmpleado=None
        while i < len(self.__ListaEmpleados) and bandera == False:
            if nombre == self.__ListaEmpleados[i].getNombreYAp():
                bandera=True
            else:
                i+=1
                
        if bandera == True:
            objetoEmpleado=self.__ListaEmpleados[i]
        
        return objetoEmpleado
    
    def buscarIncisoC(self,nombre1):
        i=0
        bandera=False
        empleadoBuscado=None
        while i < len(self.__ListaEmpleados) and bandera == False:
            if nombre1 == self.__ListaEmpleados[i].getNombreYAp():
                bandera=True
            else:
                i+=1
                
        if bandera == True:
            empleadoBuscado=self.__ListaEmpleados[i]

        return empleadoBuscado
                
        
