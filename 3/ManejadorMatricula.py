import csv
from Matricula import Matricula

class ManejadorMatricula:
    __ListaMatriculas: list
    
    def __init__(self):
        self.__ListaMatriculas = []
    
    def cargarMatricula(self, GPC,GE):
        with open("matriculas.csv", "r") as archivo:
            reader = csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader:
                Fecha=fila[0]
                Empleado=GE.buscarEmpleado(fila[1])
                Programa=GPC.buscarProgrma(fila[2])
                if (Empleado != None and Programa != None):
                    unaMatricula = Matricula(Fecha,Empleado,Programa)
                    self.__ListaMatriculas.append(unaMatricula)
                print("Matricula cargada correctamente")
        archivo.close()
        
    def incisoA(self,Id):
        for Matricula in self.__ListaMatriculas:
            if Id == Matricula.getEmpleado().getIdEmpleado():
                print(f"{Matricula.getPrograma().getDuracion()}")

    def incisoB(self,NombrePrograma):
        for Matricula in self.__ListaMatriculas:
            if NombrePrograma == Matricula.getPrograma().getNombre():
                print(f"{Matricula.getEmpleado()}")
    
    def incisoC(self):
        for Matricula in self.__ListaMatriculas:
            if Matricula.getEmpleado() not in self.__ListaMatriculas:
                print(f"{Matricula.getEmpleado().getNombreYAp()} no ha sido matriculado en ningun programa")
 
 
            