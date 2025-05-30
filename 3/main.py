from ManejadorMatricula import ManejadorMatricula
from ManejadorProgramaCapacitacion import ManejadorProgramaCapacitacion
from ManejadorEmpleado import ManejadorEmpleado

def main(GPC, GE, GM):
    opcion = 0
    while (opcion != 4):
        print("\n--- MENU DE OPCIONES ---")
        print("1. Informar duracion de programas por ID de empleado")
        print("2. Mostrar empleados matriculados en un programa")
        print("3. Mostrar empleados sin matriculas")
        print("4. Salir")
        opcion = int(input("Ingrese una opcion: "))
        
        if(opcion == 1):
            Id=int(input("Ingrese el id del empleado: "))
            GM.incisoA(Id)

        elif(opcion == 2):
            NombrePrograma = input("Ingrese el nombre del programa: ")
            GM.incisoB(NombrePrograma)

        elif(opcion == 3):
            GE.incisoC(GM)

if __name__ == '__main__':
    GPC = ManejadorProgramaCapacitacion()
    GPC.cargarPrograma()
    GE = ManejadorEmpleado()
    GE.cargarEmpleado()
    GM = ManejadorMatricula()
    GM.cargarMatricula(GE, GPC)
    main(GPC, GE, GM)