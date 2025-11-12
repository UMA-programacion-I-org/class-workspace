# Guía de ejercicios de estructuras

Para resolver los siguientes ejercicios puede utilizar ciclos o comprensiones, recomendamos fuertemente comprender como resolverlos con comprensiones.

## 1. **Empleados – filtrar por salario.**

Una empresa almacena a sus empleados en un diccionario `employee_id -> (nombre, apellido, edad, rol, salario, depto)`:

```python
employees = {
    "E-101": ("Ana", "Bretton", 27, "Dev", 1800.0, "IT"),
    "E-102": ("Luis", "García", 31, "Ops", 1400.0, "IT"),
    "E-103": ("Nora", "Silva",  29, "QA",  1600.0, "IT"),
}
```

Se desea calcular la lista de tuplas `(employee_id, nombre)` de aquellos empleados que ganan más de `1500`.

## 2. **Red de amistades – grados.**

Una red social guarda amistades en un diccionario `user_id -> set(amigos)` sin duplicados:

```python
friends = {"u1": set(["u2", "u3"]), "u2": set(["u1"]), "u3": set(["u1"]), "u4": set()}
```

Se desea calcular el **grado** (cantidad de amigos) de cada usuario como un diccionario `user_id -> grado`.

## 3. **Agenda plana – eventos matutinos.**

Un equipo lleva su agenda como tuplas planas `(fecha, inicio, fin, título)` en una lista:

```python
eventos = [
    ("2025-11-12", "09:00", "10:00", "Daily standup"),
    ("2025-11-12", "11:30", "12:00", "Revisión bugs"),
    ("2025-11-12", "15:00", "16:00", "1:1 con Ana"),
]
```

Se desea calcular los eventos de la fecha `"2025-11-12"` cuyo `inicio < "12:00"`.

## 4. **Libros – índice por autor.**

Una biblioteca registra libros como filas `(book_id, título, año, autor)`:

```python
libros = [
    ("B-10", "Algoritmos",  2020, "Knuth"),
    ("B-11", "Estructuras", 2018, "Knuth"),
    ("B-12", "Pythonic",    2022, "Luciano"),
]
```

Se desea construir el índice `indice_por_autor` tal que `autor -> {book_id, título, año}`.

## 5. **Pedidos e ítems – total por pedido.**

Un e-commerce guarda pedidos en una lista `(order_id, customer_id)` y sus ítems por separado `(order_id, product_id, cantidad, precio_unitario)`:

```python
orders = [("O-001", "C-77"), ("O-002", "C-88")]   # (order_id, customer_id)
order_items = [("O-001", "P-001", 2, 20.0),
               ("O-001", "P-002", 1, 12.0),
               ("O-002", "P-002", 3, 12.0)]
```

Se desea calcular `total_por_pedido` un diccionario tal que  `order_id -> total` siendo el total la suma de `cantidad * precio_unitario` de todos los items de la orden `order_id`.

## 6. **Sensores – ids sobre umbral.**

Un sistema IoT guarda las lecturas mas recientes de sensores de una planta eléctrica en un diccionario `sensor_id -> (lat, lon, timestamp, value)`:

```python
sensors = {
    "SEN-A": (10.495, -66.879, "2025-11-12T10:30", 23.4),
    "SEN-B": (10.501, -66.870, "2025-11-12T10:31", 24.1),
    "SEN-C": (10.503, -66.860, "2025-11-12T10:35", 25.2),
}
```

Se desea obtener el conjunto de `sensor_id` tales que `value > umbral` donde `umbral` es `24.0`.

## 7. **Visitas por día – únicos.**

Un sitio web registra visitas como tuplas `(fecha, user_id)` en una lista plana:

```python
visitas = [
    ("2025-11-10", "u1"), ("2025-11-10", "u2"), ("2025-11-10", "u3"),
    ("2025-11-11", "u2"), ("2025-11-11", "u3"),
]
```

Se desea calcular `unicos_por_dia`, un diccionario tal que `fecha -> cantidad_de_usuarios_distintos`.