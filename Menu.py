def Menu():
    print("Selecciona el algoritmo de ordenamiento:")
    print("1 Merge Sort ")
    print("2 Gnome Sort ")
    print("3 Quick Sort")
    print("4  Radix Sort ")
    print("5 Shell Sort ")
    print("6 Selection Sort ")
    print("7 Heap Sort ")
    print("8 salir del programa")
    choice = input("Ingrese el número de algoritmo que desea ejecutar")
    return int (choice)


def main():
    choice = Menu()
    if choice == 1:
        pass 
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    elif choice == 6:
            pass
    elif choice == 7:
                # Llamar a la función que implementa Heap Sort
             pass
    elif choice == 8:
        print("Saliendo del programa...")
        return
    else:
         print("Opción no válida. Por favor, seleccione un número del 1 al 8.")

          