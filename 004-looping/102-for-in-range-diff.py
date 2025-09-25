"""
  Un semaforo inteligente en una interseccion de calles cuenta con un sensor
  la cantidad de vehiculos que atraviesan la interseccion. 

  Los resultados del sensor son almacenados en una lista, donde cada elemento
  representa la cantidad total de vehiculos que han pasado por la interseccion
  desde que se inicio el conteo.

  La posicion i-ésima de la lista representa la cantidad de vehiculos
  que han pasado desde el inicio del conteo hasta el el dia i.

  Escriba un programa que dada esa lista calcule la cantidad de vehiculos
  que han pasado por la interseccion en un dia determinado.
"""

total_observations = [10, 20, 30, 50, 80, 130, 210]

daily_vehicles = [total_observations[0]]

for i in range(len(total_observations) - 1):
    daily_vehicles.append(total_observations[i + 1] - total_observations[i])

print(daily_vehicles)
