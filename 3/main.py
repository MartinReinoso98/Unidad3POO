from ManejadorMatricula import ManejadorMatricula
from ManejadorProgramaCapacitacion import ManejadorProgramaCapacitacion
from ManejadorEmpleado import ManejadorEmpleado

def menu():
      op = input("""Ingrese opcion:
                     1_ Informar por id de empleado
                     2_ Informar por nombre de programa
                     3_ Informar empleados no matriculados
                     0_ Para finalizar: """)
      return op

if __name__ == '__main__':
    GPC = ManejadorProgramaCapacitacion()
    GPC.cargarProgramaCapacitacion()
    GE = ManejadorEmpleado()
    GE.cargarEmpleado()
    GM = ManejadorMatricula()
    GM.cargarMatricula(GPC,GE)
    
    op = menu()
    if(op == '1'):
        Id=int(input("Ingrese el id del empleado: "))
        GM.incisoA(Id)
    elif(op == '2'):
        NombrePrograma = input("Ingrese el nombre del programa: ")
        GM.incisoB(NombrePrograma)
    elif(op == '3'):
        GM.incisoC()