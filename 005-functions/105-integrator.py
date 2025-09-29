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

IVA_RATE = 0.16
IGTF_RATE = 0.03

num_people = int(input("ingrese el numero de personas en la mesa: "))
plate_price = float(input("ingrese el precio del plato ordenado: "))
is_usd = input("El pago es en dólares? (s/n)").lower() == "s"

if num_people <= 0:
    raise ValueError("Debe haber al menos una persona en la mesa")

if plate_price <= 0:
    raise ValueError("El precio del plato debe ser positivo")


def compute_subtotal(num_people, price):
    return num_people * price


def compute_IVA(subtotal):
    return subtotal * IVA_RATE


def compute_igtf(subtotal, is_usd_payment=False):
    return subtotal * IGTF_RATE if is_usd_payment else 0


def compute_tax(subtotal, is_usd_payment=False):
    return compute_IVA(subtotal) + compute_igtf(subtotal, is_usd_payment)


def compute_total(num_people, price, is_usd_payment=False):
    subtotal = compute_subtotal(num_people, price)
    tax = compute_tax(subtotal, is_usd_payment)

    return subtotal + tax


subtotal = compute_subtotal(num_people, plate_price)
iva = compute_IVA(subtotal)
igtf = compute_igtf(subtotal, is_usd_payment=is_usd)
total = compute_total(num_people, plate_price, is_usd_payment=is_usd)

print()

print("Reporte de cuenta:")
print(f"- Subtotal: {round(subtotal, 2)}")
print(f"- IVA: {round(iva, 2)}")
print(f"- IGTF: {round(igtf, 2)}")
print(f"TOTAL: {total}")
