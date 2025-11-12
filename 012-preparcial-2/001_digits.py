# EJERCICIO – SUMA DIGITOS

def suma_digitos(n):
    """
    Devuelve la suma de los dígitos de un entero no negativo n.
    Ejemplo: suma_digitos(2041) = 2 + 0 + 4 + 1 = 7
    """
    # Caso base: si n tiene un solo dígito (0–9), la suma es el mismo número
    if n < 10:
        return n

    # Progreso:
    # - ultimo = n % 10  -> último dígito
    # - resto = n // 10  -> n sin el último dígito
    ultimo = n % 10
    resto = n // 10

    # Llamada recursiva sobre un número más pequeño (resto),
    # garantizando progreso hacia el caso base.
    return suma_digitos(resto) + ultimo


"""
Arbol de llamadas para n = 2041

suma_digitos(2041)
└── suma_digitos(204) + 1
    └── suma_digitos(20) + 4
        └── suma_digitos(2) + 0
            └── 2   (caso base)
"""


def suma_digitos_iterativa(n):
    """
    Versión iterativa de suma_digitos.
    """
    total = 0
    while n > 0:
        ultimo = n % 10       # tomo el último dígito
        total += ultimo       # lo sumo al acumulador
        n = n // 10           # "recorto" el número
    return total
