import csv
from ProgramaCapacitacion import ProgramaCapacitacion

class ManejadorProgramaCapacitacion:
    __ListaProgramas: list

    def __init__(self):
        self.__ListaProgramas = []
    
    def cargarProgramaCapacitacion(self):
        with open("programas.csv", "r") as archivo:
            reader = csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader:
                Nombre=fila[0]
                Codigo=int(fila[1])
                Duracion=int(fila[2])
                unPrograma = ProgramaCapacitacion (Nombre,Codigo,Duracion)
                self.__ListaProgramas.append(unPrograma)
        archivo.close()
    
    def buscarPrograma(self,nombre):
        i=0
        bandera=False
        objetoPrograma=None
        while i < len(self.__ListaProgramas) and bandera == False:
            if nombre == self.__ListaProgramas[i].getNombre():
                bandera=True
            else:
                i+=1
                
        if bandera == True:
            objetoPrograma=self.__ListaProgramas[i]
        
        return objetoPrograma
