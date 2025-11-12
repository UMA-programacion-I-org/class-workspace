## 1. **Traza de una matriz (diagonal principal).**

La **traza** es la suma de los elementos `A[i][i]` (la **diagonal principal**). En matrices no cuadradas, se usa `min(m, n)`.

```python
A = [[2, 5, 1],
     [0, 3, 4]]
# Diagonal principal: A[0][0]=2, A[1][1]=3 => 2+3 = 5
# trace(A) -> 5
```

Se desea Implementar `trace(A)`.

## 2. **Diagonal secundaria.**

La **diagonal secundaria** va de la esquina superior derecha a la inferior izquierda: posiciones `(i, n-1-i)`. En no cuadradas, se usa `min(m, n)`.

```python
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
# Secundaria: 3 + 5 + 7 = 15
# secondary_diagonal_sum(A) -> 15
```

Se desea Implementar `secondary_diagonal_sum(A)`.

## 3. **Matriz simétrica.**

Una matriz cuadrada es **simétrica** si `A[i][j] == A[j][i]` para todo `i, j` (equivale a `A == transpose(A)`).

```python
A = [[1, 2],
     [2, 3]]
# is_symmetric(A) -> True
```

Se desea Implementar `is_symmetric(A)` que retorne `True/False`.

## 4. **Matriz triangular superior.**

Una matriz es **triangular superior** si todos los elementos **debajo** de la diagonal principal son 0 (es decir, `A[i][j] == 0` cuando `i > j`).

```python
A = [[3, 1, 4],
     [0, 5, 9],
     [0, 0, 2]]
# is_upper_triangular(A) -> True
```

Se desea Implementar `is_upper_triangular(A)` que retorne `True/False`.

## 5. **Multiplicación por escalar.**

Dado un escalar `k`, la matriz resultante es `B[i][j] = k * A[i][j]`.

```python
A = [[1, 2],
     [3, 4]]
k = 3
# scalar_multiply(A, k) -> [[3, 6], [9, 12]]
```

Se desea Implementar `scalar_multiply(A, k)`.

## 6. **Máximo y posición.**

Se pide encontrar el **valor máximo** de `A` y su **posición** `(i, j)` (índices base 0).

```python
A = [[1, 7],
     [5, 2]]
# max_element_and_pos(A) -> (7, 0, 1)
```

Se desea Implementar `max_element_and_pos(A)` que retorne `(max_value, i, j)`.

## 7. **Contar ocurrencias de un valor.**

Se pide contar cuántas veces aparece un **valor `x`** en la matriz.

```python
A = [[2, 2, 3],
     [4, 2, 5]]
x = 2
# count_value(A, x) -> 3
```

Se desea Implementar `count_value(A, x)`.

## 8. **Suma del borde (perímetro).**

El **borde** son los elementos de la primera y última fila, y de la primera y última columna (sin **doble contar** las esquinas).

```python
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
# Borde: 1+2+3 + 6+9+8 + 7+4 = 40
# border_sum(A) -> 40
```

Se desea Implementar `border_sum(A)`.

## 9. **Fila con mayor suma.**

Se pide devolver el **índice** de la fila con **mayor suma** (si hay empate, el primero).

```python
A = [[1, 1, 10],
     [5, 5, 0],
     [3, 3, 3]]
# Sumas: 12, 10, 9 -> índice 0
# row_with_max_sum(A) -> 0
```

Se desea Implementar `row_with_max_sum(A)`.
