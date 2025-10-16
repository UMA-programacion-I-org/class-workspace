"""
Una empresa registra, para cada día, un movimiento neto en su caja: depósitos como enteros positivos, 
egresos como enteros negativos, y días sin movimiento como 0. Se parte de saldo inicial 0. 
Los datos se entregan como una lista de enteros movs.

Ejemplo de entrada: movs = [200, -50, -50, 0, 100, -300, -20, -20, 0, 50]

Dado movs, se desea:

1. Primer sobregiro: Detectar si el saldo acumulado (sumando día a día) se vuelve negativo en algún momento.
  - Si ocurre, reportar el primer índice de día en que el saldo es < 0 y el saldo en ese instante.
  - Si nunca se vuelve negativo, reportar −1.

2. Capital mínimo para no sobregirar: Calcular el menor capital inicial no negativo C tal que, si se comienza con saldo C 
    y se aplican en orden los movimientos de movs, el saldo nunca es negativo en ningún día.
  - Reportar dicho C.

3. Validaciones y casos borde:
  - Si movs contiene algún valor que no sea entero, la entrada es inválida: debe reportarse el primer índice inválido.
  - La lista vacía [] debe producir:
    - Para (Primer sobregiro): −1 (no hay sobregiro).
    - Para (Capital mínimo): capital mínimo 0.
    - Los ceros cuentan como movimientos válidos y no alteran por sí mismos el signo del saldo.

Recuerde mantener su código organizado con funciones.
"""


def validate_movs(movs):
    """
    Validates that movs is a list of *integers* (no floats, no bools).
    Raises ValueError with the first invalid index if any element is invalid.
    """
    if not isinstance(movs, list):
        raise ValueError("Input must be a list named 'movs'")

    for i in range(len(movs)):
        if not isinstance(movs[i], int):
            raise ValueError(f"Invalid element at index {i}: not an int")


def first_overdraft(movs):
    """
    Returns (day_index, balance_at_overdraft) for the first time the running
    balance becomes negative.
    If no overdraft occurs, returns (-1, None).
    """
    balance = 0

    for day in range(len(movs)):
        balance += movs[day]

        if balance < 0:
            return day, balance

    return -1, None


def min_initial_capital(movs):
    """
    Returns the minimal non-negative initial capital C such that
    starting from C, the running balance never becomes negative.

    Formula: C = max(0, -min_prefix_sum).
    """
    balance = 0
    min_prefix = 0
    for delta in movs:
        balance += delta

        if balance < min_prefix:
            min_prefix = balance

    return max(0, -min_prefix)


def analyze_cash_flow(movs):
    """
    Orchestrates validation and computations.

    Returns a tuple with:
    - first_overdraft_index: int
    - first_overdraft_balance: int | None
    - min_initial_capital: int
    """
    validate_movs(movs)

    if not movs:
        return -1, None, 0

    od_day, od_bal = first_overdraft(movs)
    C = min_initial_capital(movs)

    return od_day, od_bal, C


if __name__ == "__main__":
    movs = [200, -50, -50, 0, 100, -300, -20, -20, 0, 50]

    try:
        od_day, od_bal, C = analyze_cash_flow(movs)
        print(f"First overdraft: day {od_day}, balance {od_bal}")
        print(f"Minimum initial capital to avoid overdraft: {C}")
    except ValueError as e:
        print("Validation error:", e)
