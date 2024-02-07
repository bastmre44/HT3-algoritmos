

def gnome_sort(arr):
    index = 0  # índice para recorrer la lista
    n = len(arr)  #  la longitud de la lista
    while index < n:  # Mientras el índice sea menor que la longitud de la lista
        if index == 0:  # Si el índice es 0, incrementamos para evitar un índice negativo
            index += 1
        if arr[index] >= arr[index - 1]:  # Si el elemento actual es mayor o igual que el anterior
            index += 1  # Avanzamos al siguiente elemento
        else:  # Si el elemento actual es menor que el anterior
            # Intercambiamos los elementos y retrocedemos un índice
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1
    return arr  # Devolvemos la lista ordenada

# Ejemplo de uso:
my_list = [5, 3, 8, 4, 2]
print("Lista original:", my_list)
sorted_list = gnome_sort(my_list)
print("Lista ordenada:", sorted_list)