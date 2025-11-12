# EJERCICIO - BUSQUEDA BINARIA

def binary_search_recursive(numbers, target, low=0, high=None):
    # Inicializamos high en la primera llamada
    if high is None:
        high = len(numbers) - 1

    # CASO BASE 1: rango vacío ⇒ no está
    if low > high:
        return -1

    mid = (low + high) // 2

    # CASO BASE 2: lo encontramos
    if numbers[mid] == target:
        return mid

    # LLAMADAS RECURSIVAS (progreso):
    # descartamos la mitad donde seguro no está
    if numbers[mid] < target:
        # Buscar en la mitad derecha
        return binary_search_recursive(numbers, target, mid + 1, high)
    else:
        # Buscar en la mitad izquierda
        return binary_search_recursive(numbers, target, low, mid - 1)


# Uso con la lista de la imagen
numbers = [1, 3, 5, 7, 9, 11, 13, 15]
target = 13

index = binary_search_recursive(numbers, target)
print(index)  # debería imprimir 6

"""
Árbol de ejecución para numbers = [1,3,5,7,9,11,13,15] y target = 13

Llamada 1: low = 0, high = 7
    mid = (0 + 7) // 2 = 3  → numbers[3] = 7  (< 13)
    ⇒ recursión a la mitad derecha

    Llamada 2: low = 4, high = 7
        mid = (4 + 7) // 2 = 5 → numbers[5] = 11 (< 13)
        ⇒ recursión a la mitad derecha

        Llamada 3: low = 6, high = 7
            mid = (6 + 7) // 2 = 6 → numbers[6] = 13 (== target)
            ⇒ caso base: devolver 6

O alternativamente (en formato de arbol resumido):

binary_search_recursive(numbers, 13, 0, 7)
└── binary_search_recursive(numbers, 13, 4, 7)
    └── binary_search_recursive(numbers, 13, 6, 7)
        └── return 6
"""
