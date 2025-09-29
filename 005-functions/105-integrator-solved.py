"""
El restaurante “Arepas por igual” tiene un menú algo peculiar. 
Ofrecen múltiples variantes de arepas con distintos rellenos, 
pero tienen la peculiaridad de que todos los miembros de una 
mesa deben pedir la misma arepa con el mismo relleno.

Como todos los miembros de una mesa deben ordenar el mismo plato, 
la cuenta se construye multiplicando el numero de personas en la mesa 
y el precio del plato que pidieron todos.

Se requiere escribir un algoritmo que dada la cantidad de personas en una 
mesa y el precio del plato que ordenaron muestre un reporte de la cuenta con:
- El subtotal de la cuenta
- El monto de impuesto IVA
- El monto de IGTF si el pago es en dólares
- El total de la cuenta

Todos los montos del reporte de cuenta deben estar redondeados a dos decimales 
"""

num_people = int(input("Ingrese el número de personas en la mesa: "))
plate_price = float(input("Ingrese el precio del plato: "))
is_usd_payment = input("¿El pago es en dólares? (s/n): ").lower() == 's'

IVA_RATE = 0.16
IGTF_RATE = 0.03


def calculate_subtotal(num_people, plate_price):
    return num_people * plate_price


def calculate_iva(subtotal):
    return subtotal * IVA_RATE


def calculate_igtf(subtotal, is_usd_payment):
    return subtotal * IGTF_RATE if is_usd_payment else 0


def calculate_tax(subtotal, is_usd_payment):
    iva = calculate_iva(subtotal)
    igtf = calculate_igtf(subtotal, is_usd_payment)

    return iva + igtf


def calculate_total(subtotal, tax):
    return subtotal + tax


subtotal = round(calculate_subtotal(num_people, plate_price), 2)
tax = round(calculate_tax(subtotal, is_usd_payment), 2)
total = round(calculate_total(subtotal, tax), 2)

print()

print("--- Reporte de la Cuenta ---")
print(f"Subtotal: {subtotal}")
print(f"IVA: {calculate_iva(subtotal)}")
print(f"IGTF: {calculate_igtf(subtotal, is_usd_payment)}")
print(f"Total: {total}")
