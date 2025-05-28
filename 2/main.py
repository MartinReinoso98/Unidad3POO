from ManejadorBiblioteca import ManejadorBiblioteca

def menu():
    op=input("""Ingrese opcion:
                     1_ Agregar libro
                     2_ Eliminar libro
                     3_ Mostrar biblioteca, nombre del autor y genero para un titulo de un libro
                     4_ Listar libros
                     0_ Para finalizar: """)
    return op

if __name__ == '__main__':
    GB = ManejadorBiblioteca
    
    op = menu()
    if(op == '1'):
        NombreBib = input("Ingrese el nombre de la biblioteca a cual se quiera agregar: (1 - 2): ") # 1 es Central y 2 Popular
        GB.incisoA(NombreBib)

    elif(op == '2'):
        NombreBiblio = input("Ingrese el nombre de la biblioteca a cual se quiera eliminar un libro: (1 - 2): ") # 1 es Central y 2 Popular
        NombreLibr = input("Ingrese el nombre del libro el cual se quiere eliminar: ")
        GB.incisoB(NombreBiblio,NombreLibr)

    elif(op == '3'):
        tituloLibro = input("Ingrese el titulo: ")
        GB.incisoC(tituloLibro)
    
    elif(op == '4'):
        GB.incisoD()