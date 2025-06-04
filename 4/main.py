from ManejadorPlanes import ManejadorPlanes

def main(GP):
    opcion = 0
    while (opcion != 5):
        print("Menu de opciones")
        print("[1] Mostrar por pantalla el tipo de plan")
        print("[2] Mostrar y contar la cantidad de planes de una cobertura geografica")
        print("[3] Mostrar el/los nombres de las companias que ofrecen esa cantidad de canales internacionales")
        print("[4] Mostrar tipo de plan, nombre de la compania, duracion del plan, cobertura e importe final")
        print("[5] SALIR")

        opcion=int(input("Ingrese una opcion: "))

        if opcion == 1:
            try:
                posicion=int(input("Ingrese la posicion de la lista a mostrar: "))
                GP.incisoA(posicion-1)
            except IndexError:
                print("Posicion fuera de rango")

        elif opcion == 2:
            cobertura=input("Ingrese el area de cobertura: ")
            GP.incisoB(cobertura)

        elif opcion == 3:
            cantidad=int(input("Ingrese la cantidad de canales internacionales: "))
            GP.incisoC(cantidad)
        
        elif opcion == 4:
            GP.incisoD()
            
if __name__ == '__main__':
    GP = ManejadorPlanes()
    GP.cargarPlanes()
    GP.mostrarPlanes()
    main(GP)