# EJERCICIO - NESTED SUM

def suma_anidada(lst):
    """
    Suma todos los números de una lista que puede tener
    listas anidadas a cualquier profundidad.
    """
    # CASO BASE: lista vacía
    if len(lst) == 0:
        return 0

    primero = lst[0]
    resto = lst[1:]

    # Progreso: Si el primer elemento es un número, lo sumamos directo
    if isinstance(primero, (int, float)):
        return primero + suma_anidada(resto)

    # Progreso: Si el primer elemento es otra lista, sumamos recursivamente su contenido
    elif isinstance(primero, list):
        return suma_anidada(primero) + suma_anidada(resto)

    else:
        # Progreso: Ignorar elementos no numéricos ni lista
        return suma_anidada(resto)


datos = [1, [2, 3], [4, [5, 6]], 7]
print(suma_anidada(datos))  # 28
