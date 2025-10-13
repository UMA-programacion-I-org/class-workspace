"""
Se recibe un entero N ≥ 1. Para cada k en el rango 1..N, se define:

1. Divisores propios de k: enteros positivos d tales que d < k y d divide a k.
2. Suma de divisores propios: s(k) = ∑ d (sobre todos los divisores propios de k).
3. Clasificación de k:
  - Perfecto si s(k) = k.
  - Abundante si s(k) > k.
  - Deficiente si s(k) < k.

Se desea:

1. Conteos por categoría: Determinar cuántos números en 1..N son perfectos, cuántos abundantes 
                          y cuántos deficientes.

2. Exceso máximo: Calcular el exceso e(k) = s(k) − k para cada k y reportar el k que maximiza e(k) 
                  junto con el valor de e(k) (si hay empates, aceptar el menor k).

3. Primer par amistoso en el rango: Un par (a, b) con a < b es amistoso si s(a) = b y s(b) = a.
  - Si existe al menos un par con b ≤ N, reportar el primer par en orden creciente por a 
    (y luego por b si hay empate).
  - Si no existe tal par en 1..N, reportar (-1, -1).

4. Validaciones y casos borde:
  - Si N no es entero o N < 1, la entrada es inválida.
  - Para N = 1: 1 es deficiente (pues s(1) = 0), no hay pares amistosos y el exceso máximo es e(1) = −1.

Notas:
- Los divisores propios de un número natural son todos sus divisores positivos excepto el mismo número. 
    - Por ejemplo, los divisores propios de 12 son: 1, 2, 3, 4, 6
    
Recuerde mantener su código organizado con funciones.
"""


def validate_N(N):
    """Validate that N is an integer >= 1; raise ValueError otherwise."""
    if not isinstance(N, int):
        raise ValueError("N must be an integer.")
    if N < 1:
        raise ValueError("N must be >= 1.")


def proper_divisors(k):
    """
    Return the list of proper divisors of k.
    Proper divisors are positive divisors strictly less than k.
    Per instructions: iterate from 1 up to k and collect divisors.
    (We use range(1, k) which goes 1..k-1, excluding k itself.)
    """
    divs = []
    for d in range(1, k):
        if k % d == 0:
            divs.append(d)
    return divs


def sum_proper_divisors(k):
    """Return s(k) = sum of proper divisors of k, using the list above."""
    total = 0
    for d in proper_divisors(k):
        total += d
    return total


def classify_counts(N, svals):
    """
    Given svals where svals[k] = s(k), count how many numbers in 1..N are:
    - perfect   (s(k) == k)
    - abundant  (s(k) > k)
    - deficient (s(k) < k)
    Returns perfect_count, abundant_count, deficient_count.
    """
    perfect = 0
    abundant = 0
    deficient = 0
    for k in range(1, N + 1):
        sk = svals[k]
        if sk == k:
            perfect += 1
        elif sk > k:
            abundant += 1
        else:
            deficient += 1
    return perfect, abundant, deficient


def max_excess(N, svals):
    """
    Compute e(k) = s(k) - k and return (k_max, e_max) where e_max is maximal.
    Tie-breaker: choose the smallest k in case of ties.
    """
    best_k = 1
    best_e = svals[1] - 1
    for k in range(2, N + 1):
        e = svals[k] - k
        if e > best_e or (e == best_e and k < best_k):
            best_e = e
            best_k = k
    return best_k, best_e


def first_amicable_pair(N, svals):
    """
    Find the first amicable pair (a, b) with a < b and b <= N,
    in increasing order of 'a' (and then 'b' if needed).
    Condition: s(a) = b and s(b) = a.
    If none exists in 1..N, return (-1, -1).
    """
    for a in range(1, N + 1):
        b = svals[a]
        if b > a and b <= N:
            if svals[b] == a:
                return a, b

    return -1, -1


def analyze_numbers(N):
    """
    Main entry point.
    Returns a tuple:
      (
        (perfect_count, abundant_count, deficient_count),
        (k_max_excess, e_max),
        (amicable_a, amicable_b)   # or (-1, -1) if none
      )

    Notes:
    - Implements the required "iterate 1..k collecting divisors" approach.
    - Uses only lists/tuples (no dictionaries).
    - Time complexity is O(N^2) due to the divisor enumeration rule.
    """
    validate_N(N)

    # Precompute s(k) for k = 1..N into a list (index 0 unused for convenience).
    svals = [0] * (N + 1)
    for k in range(1, N + 1):
        svals[k] = sum_proper_divisors(k)

    counts = classify_counts(N, svals)         # (perfect, abundant, deficient)
    k_max_e, e_max = max_excess(N, svals)      # (k, e(k))
    amicable = first_amicable_pair(N, svals)   # (a, b) or (-1, -1)

    return counts, (k_max_e, e_max), amicable


if __name__ == "__main__":
    N = 30
    counts, (k_max, e_max), (a, b) = analyze_numbers(N)

    print("Counts (perfect, abundant, deficient):", counts)
    print("Max excess -> k:", k_max, " e(k):", e_max)
    print("First amicable pair up to N:", (a, b))
