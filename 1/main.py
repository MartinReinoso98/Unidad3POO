from ManejadorHotel import ManejadorHotel

def main(GH):
    opcion = 0
    while (opcion != 7):
        print("[1] Agregar habitaciones al hotel")
        print("[2] Reservar habitación")
        print("[3] Liberar habitación")
        print("[4] Mostrar número y piso de las habitaciones de un tipo")
        print("[5] Mostrar cantidad de habitaciones libres por piso")
        print("[6] Mostrar listado de habitaciones")
        print("[7] Salir")
        
        opcion=int(input("Ingrese una opcion: "))

        if opcion == 1:
            nomHotel = input("\nIngrese el nombre del hotel: ")
            GH.incisoA(nomHotel)
            
        elif opcion == 2:
            nomHotel = input("\nIngrese el nombre del hotel: ")
            GH.incisoB(nomHotel)

        elif opcion == 3:
            nomHotel = input("\nIngrese el nombre del hotel: ")
            GH.incisoC(nomHotel)
        
        elif opcion == 4:
            tipoHab = input("\nIngrese el tipo de habitación: ")
            GH.incisoD(tipoHab)
        
        elif opcion == 5:
            GH.incisoE()

        elif opcion == 6:
            GH.incisoF()

        else:
            print("Error -- Opcion invalida")

            
if __name__ == '__main__':
    GH = ManejadorHotel()
    GH.cargarHoteles()
    main(GH)