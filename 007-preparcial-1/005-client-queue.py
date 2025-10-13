"""
Una empresa atiende clientes en una ventanilla única. Cada cliente tarda un tiempo fijo de servicio de t = 5 minutos. 
Los clientes llegan a lo largo del día y forman cola si la ventanilla está ocupada.

Entrada:

Una sola lista arrivals de enteros no negativos, en minutos desde la apertura (por ejemplo, 0 es justo al abrir). 
La lista está en orden no decreciente (si dos clientes llegan a la misma vez, el que aparece primero en la lista se atiende primero). 
Ejemplo: arrivals = [0, 0, 3, 7, 7, 20].

Se desea:

1. Validación:
- Verificar que todos los elementos de arrivals sean enteros ≥ 0.
- Verificar que la lista esté en orden no decreciente.
- Si hay un error, reportar el primer índice (0-based) donde ocurre (valor negativo, no entero, o ruptura de orden) y terminar.

2. Tiempos de espera individuales:
- Construir la lista waits tal que waits[i] sea el tiempo de espera (en minutos) del cliente i antes de empezar a ser atendido.

Recomendación sobre el cálculo de waits:
  - Sea finish el minuto en que la ventanilla queda libre tras el cliente anterior (inicialmente finish = 0).
  - Para el cliente i que llega en arrivals[i]:
    start_i = max(arrivals[i], finish)
    waits[i] = start_i − arrivals[i]
    finish = start_i + t (con t = 5)

3. Indicadores de operación:
- Promedio de espera (con 2 decimales).
- Máxima espera y el índice de cliente que la experimenta; en caso de empates, el primero.

Recuerde mantener su código organizado con funciones.
"""

T_SERVICE = 5  # fixed service time in minutes


def validate_arrivals(arrivals):
    """
    Validate that:
      - arrivals is a list
      - every element is an *exact* int
      - every element is >= 0
      - the list is non-decreasing (arrivals[i] >= arrivals[i-1])
    On the first error, raise ValueError("index: reason").
    """
    if not isinstance(arrivals, list):
        raise ValueError("Input must be a list named 'arrivals'")

    prev = None
    for i in range(len(arrivals)):
        if not isinstance(arrivals[i], int):
            raise ValueError(f"{i}: not an int")

        if arrivals[i] < 0:
            raise ValueError(f"{i}: negative value")

        if prev is not None and arrivals[i] < prev:
            raise ValueError(f"{i}: out of non-decreasing order")

        prev = arrivals[i]


def compute_waits(arrivals, t=T_SERVICE):
    """
    Build waits[] where waits[i] is the waiting time before service.
    Uses the recommended recurrence:
      finish = 0
      for each arrival a:
          start_i = max(a, finish)
          waits[i] = start_i - a
          finish = start_i + t
    Returns waits (list of ints).
    """
    waits = []
    finish = 0

    for a in arrivals:
        start_i = a if a >= finish else finish
        waits.append(start_i - a)
        finish = start_i + t

    return waits


def stats_from_waits(waits):
    """
    Compute:
      - average wait rounded to 2 decimals (float)
      - maximum wait (int) and the first index where it occurs
    For empty waits:
      - avg_wait = 0.00
      - max_wait = 0
      - max_index = -1
    """
    n = len(waits)
    if n == 0:
        return 0.00, 0, -1

    total = 0
    max_wait = waits[0]
    max_index = 0
    for i in range(len(waits)):
        total += waits[i]
        if waits[i] > max_wait:
            max_wait = waits[i]
            max_index = i

    avg_wait = round(total / n, 2)
    return avg_wait, max_wait, max_index


def analyze_queue(arrivals, t=T_SERVICE):
    """
    Orchestrates the process:
      - validate arrivals
      - compute waits
      - compute indicators
    Returns a tuple: (waits, avg_wait, max_wait, max_index)
    Raises ValueError on the first validation error with "index: reason".
    """
    validate_arrivals(arrivals)
    waits = compute_waits(arrivals, t)
    avg_wait, max_wait, max_index = stats_from_waits(waits)
    return waits, avg_wait, max_wait, max_index


if __name__ == "__main__":
    arrivals = [0, 0, 3, 7, 7, 20]
    try:
        waits, avg_wait, max_wait, max_index = analyze_queue(arrivals)

        print("arrivals:", arrivals)
        print("waits   :", waits)
        print("avg_wait:", avg_wait)
        print("max_wait:", max_wait, "at index", max_index)
    except ValueError as e:
        print("Validation error:", e)
