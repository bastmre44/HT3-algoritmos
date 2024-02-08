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
    index = 0
    n = len(arr)
    while index < n:
        if index == 0:
            index += 1
        if arr[index] >= arr[index - 1]:
            index += 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1
            if index == 0:
                index = 1  # Si retrocede al inicio, asegúrate de avanzar al siguiente elemento
    if not ascending:
        arr.reverse()
    return arr



#///////////////////////////////////////////////////////////////////////////////////////////////////////////
#algoritmo opción 2 

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Dividir el arreglo en mitades
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Aplicar merge sort recursivamente a cada mitad
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Combinar las dos mitades ordenadas
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index, right_index = 0, 0
    
    # Combinar elementos ordenadamente
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    # Agregar elementos restantes de la mitad izquierda
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1
    
    # Agregar elementos restantes de la mitad derecha
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1


        #///////////////////////////////////////////////////////////////////////////////////
        #algoritmo para opción 3 
        def quicsk_sort(arr):
            
            if len(arr) <= 1:
                return arr
                # para Seleccionar el pivote como el elemento en la mitad del arreglo
            pivot = arr[len(arr) // 2]
                # Dividir el arreglo en tres partes: menores que el pivote, iguales al pivote y mayores que el pivote

            left = [x for x in arr if x < pivot]  #menores que el pivote 
            middle = [x for x in arr if x == pivot]# iguales al pivote
            right = [x for x in arr if x > pivot] #mayores que el pivote
            
            return quicsk_sort(left) + middle + quicsk_sort(right)
        
        #////////////////////////////////////////////////////////////////////////////////////
        #algoritmo para： 4 Radix Sort
def radix_sort(arr):
   def radix_sort(arr):
    # Encuentra el valor máximo en el arreglo para determinar el número de dígitos
    max_num = max(arr)
    
    # Inicializa el exponente para la base 10
    exp = 1
    
    # Continúa el proceso hasta que todos los dígitos en el valor máximo se hayan procesado
    while max_num // exp > 0:
        # Utiliza un algoritmo de conteo para ordenar el arreglo basándose en el dígito actual (exp)
        
        # Incrementa el exponente para procesar el siguiente dígito
        exp *= 10

        #///////////////////////////////////////////
        ## Algoritmo de ordenamiento Selection Sort
def selection_sort(arr):
    #para recorrer todo el arreglo 
    for i in range(len(arr)):
        #para encontrar el elemento minimo
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
                        # Intercambia el elemento actual con el elemento mínimo encontrado

        arr[i], arr[min_index] = arr[min_index], arr[i]
#///////////////////////////////////////////
# Algoritmo de ordenamiento Shell Sort
def shell_sort(arr):
    n = len(arr)
    gap = n // 2  #tamaño del salto inicial 
    # Selecciona el tamaño inicial del espacio entre los elementos
    while gap > 0:
        # Realiza un algoritmo de inserción para los elementos con un espacio de 'gap'
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # selecciona el valor actual que se está comparando
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2 # Reduce el espacio entre los elementos para la opción iteración

        #///////////////////////////////////////////
      # Algoritmo de ordenamiento Heap sort
      # Algoritmo de ordenamiento Heap Sort
def heapify(arr, n, i):
    largest = i  # Inicializar el nodo raíz como el más grande
    left = 2 * i + 1  # Índice izquierdo
    right = 2 * i + 2  # Índice derecho
    
    # Si el izquierdo es mayor que la raíz
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # Si el derecho es mayor que el más grande hasta ahora
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # Si el nodo raíz no es el más grande, intercambiar con el más grande
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Recursivamente heapify el subárbol afectado
        heapify(arr, n, largest)

   
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
            print("Lista original:", data) # Imprimir lista original
            sorted_list = merge_sort(data.copy())
            print("Lista ordenada con Merge sort:", sorted_list)
            
            pass
        elif choice == 3:
            print("Lista original:", data) # Imprimir lista original
            sorted_list = quicsk_sort(data.copy())
            pass
        elif choice == 4:
            print("Lista original:", data) # Imprimir lista original
            sorted_list = radix_sort(data.copy())
            print("Lista ordenada con Radix sort:", sorted_list)
            pass
        elif choice == 5:
            print("Lista original:", data) # Imprimir lista original
            sorted_list = selection_sort(data.copy())
            print("Lista ordenada con Selection sort:", sorted_list)

            pass
        elif choice == 6:
            print("Lista original:", data) # Imprimir lista original
            sorted_list = shell_sort(data.copy())
            print("Lista ordenada con Shell sort:", sorted_list)

            pass
        elif choice == 7:
            print("Lista original:", data) # Imprimir lista original
            sorted_list =  heapify(data.copy())
            print("Lista ordenada con Heap sort:", sorted_list)
            pass
        elif choice == 8:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione un número del 1 al 8.")

if __name__ == "__main__":
    main()
