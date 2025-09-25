import math

# Entradas:
# - score_i , name_i, para i desde 1 hasta 3

name_1 = input("Ingrese el nombre del primer estudiante: ")
name_2 = input("Ingrese el nombre del segundo estudiante: ")
name_3 = input("Ingrese el nombre del tercer estudiante: ")

score_1 = float(input("Ingrese la nota final del primer estudiante: "))
score_2 = float(input("Ingrese la nota final del segundo estudiante: "))
score_3 = float(input("Ingrese la nota final del tercer estudiante: "))

mean = (score_1 + score_2 + score_3) / 3

if mean >= 10:
    print("La mayoria aprobaron")
else:
    print("La mayoria reprobaron")

print()

aproved_1 = score_1 >= 10
aproved_2 = score_2 >= 10
aproved_3 = score_3 >= 10

aproved_msg_1 = "Reprobó"
if aproved_1:
    aproved_msg_1 = "Aprobó"

aproved_msg_2 = "Reprobó"
if aproved_2:
    aproved_msg_2 = "Aprobó"

aproved_msg_3 = "Reprobó"
if aproved_3:
    aproved_msg_3 = "Aprobó"

msg_student_1 = f"El estudiante {name_1} {aproved_msg_1}"
msg_student_2 = f"El estudiante {name_2} {aproved_msg_2}"
msg_student_3 = f"El estudiante {name_3} {aproved_msg_3}"

print(msg_student_1)
print(msg_student_2)
print(msg_student_3)

print()

print(f"Estudiante 1: {name_1}, con nota: {round(score_1)}")
print(f"Estudiante 2: {name_2}, con nota: {round(score_2)}")
print(f"Estudiante 3: {name_3}, con nota: {round(score_3)}")

list_report = [
    f"Estudiante 1: {name_1}, con nota: {round(score_1)}",
    f"Estudiante 2: {name_2}, con nota: {round(score_2)}",
    f"Estudiante 3: {name_3}, con nota: {round(score_3)}"
]
print(list_report)

print(f"Promedio general: {mean}")

names = [name_1, name_2, name_3]
scores = [score_1, score_2, score_3]

if scores[0] > scores[1] and scores[0] > scores[2]:
    print(f"El estudiante con mejor nota es {names[0]}")
elif scores[1] > scores[0] and scores[1] > scores[2]:
    print(f"El estudiante con mejor nota es {names[1]}")
elif scores[2] > scores[0] and scores[2] > scores[1]:
    print(f"El estudiante con mejor nota es {names[2]}")
else:
    print(f"Hay al menos dos estudiantes con la nota maxima")

print()

if scores[0] < scores[1] and scores[0] < scores[2]:
    print(f"El estudiante con peor nota es {names[0]}")
elif scores[1] < scores[0] and scores[1] < scores[2]:
    print(f"El estudiante con peor nota es {names[1]}")
elif scores[2] < scores[0] and scores[2] < scores[1]:
    print(f"El estudiante con peor nota es {names[2]}")
else:
    print(f"Hay al menos dos estudiantes con la nota minima")
