import csv
from Matricula import Matricula

class ManejadorMatricula:
    __ListaMatriculas: list
    
    def __init__(self):
        self.__ListaMatriculas = [] 
    
    def cargarMatricula(self, GE,GPC):
        with open("matriculas.csv", "r") as archivo:
            reader = csv.reader(archivo, delimiter=";")
            next(reader)
            for fila in reader:
                fecha = fila[0]
                empleado = GE.buscarEmpleado(fila[1])
                programa = GPC.buscarPrograma(fila[2])
                if (empleado is not None and programa is not None):
                    unaMatricula = Matricula(fecha, empleado, programa)
                    self.__ListaMatriculas.append(unaMatricula)
                    
                
        archivo.close()
            
    def incisoA(self, ID):
        for matricula in self.__ListaMatriculas:
            if matricula.getEmpleado().getIdEmpleado() == ID:
                print(f"Programa: {matricula.getPrograma().getNombre()}, Duracion: {matricula.getPrograma().getDuracion()}")
        

    def incisoB(self, NombrePrograma):
        for matricula in self.__ListaMatriculas:
            if matricula.getPrograma().getNombre() == NombrePrograma:
                print(f"Empleado: {matricula.getEmpleado().getNombreYAp()}")
    
    def buscarEmp(self, Nombre):
        i = 0
        bandera = False
        resultado = None
        while i < len(self.__ListaMatriculas) and not bandera:
            if Nombre == self.__ListaMatriculas[i].getEmpleado().getNombreYAp():
                bandera = True
            else:
                i += 1
                
        if bandera:
            resultado = self.__ListaMatriculas[i]
        return resultado

