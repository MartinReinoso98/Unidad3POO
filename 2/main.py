from ManejadorBiblioteca import ManejadorBiblioteca

def main(GH):
    opcion = 0
    while (opcion != 5):
        print("Menu de opciones")
        print("[1] Agregar libro")
        print("[2] Eliminar libro")
        print("[3] Mostrar informacion de un libro")
        print("[4] Listar")
        print("[5] Salir")
        
        opcion=int(input("Ingrese una opcion: "))

        if opcion == 1:
            nomBiblioteca = input("\nIngrese el nombre de la biblioteca: ")
            GB.incisoA(nomBiblioteca)
            
        elif opcion == 2:
            nomBiblioteca = input("\nIngrese el nombre de la biblioteca: ")
            isbn = input("Ingrese el ISBN del libro: ")
            GB.incisoB(nomBiblioteca,isbn)

        elif opcion == 3:
            TituloLibro = input("\nIngrese el titulo del libro: ")
            GB.incisoC(TituloLibro)
        
        elif opcion == 4:
            GB.incisoD()

        else:
            print("Opcion invalida")

            
if __name__ == '__main__':
    GB = ManejadorBiblioteca()
    GB.cargarBibliotecas()
    main(GB)