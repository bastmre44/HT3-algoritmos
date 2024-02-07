def menu():
    print("Seleccione el algoritmo de ordenamiento:")
    print("1. Gnome sort")
    print("2. Merge sort")
    print("3. Quick sort")
    print("4. Radix Sort")
    print("5. Selection Sort")
    print("6. Shell Sort")
    print("7. Heap Sort")
    print("8. Salir")
    choice = input("Ingrese el número correspondiente al algoritmo o '8' para salir: ")
    return int(choice)

def gnome_sort(arr, ascending=True):
    index = 0   #Inicia desde 0 
    n = len(arr)  #se define el largo de la lista 
    while index < n:  #si el indice es menor que la lista se sigue el ciclo 
        if index == 0:
            index += 1
        if arr[index] >= arr[index - 1]:
            index += 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1
    if not ascending:
        arr.reverse()
    return arr

def main():
    ascending = input("¿Desea ordenar los datos de manera ascendente? (Sí/No): ").lower()
    ascending = ascending.startswith('s')
    
    file_name = "random_numbers.txt"  # Nombre del archivo con los datos
    with open(file_name, 'r', encoding='utf-8') as file:
        data = [int(line.strip()) for line in file.readlines()]

    while True:
        choice = menu()
        if choice == 1:
            print("Lista original:", data)  # Imprimir lista original
            sorted_list = gnome_sort(data.copy(), ascending=ascending)
            print("Lista ordenada con Gnome sort:", sorted_list)
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
           
            pass
        elif choice == 8:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione un número del 1 al 8.")

if __name__ == "__main__":
    main()
