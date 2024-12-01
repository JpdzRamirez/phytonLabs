# Solicitar la cantidad de tareas
num_tareas = int(input("Ingrese la cantidad de tareas en el curso: "))

# Inicializar las listas para almacenar los nombres, ponderaciones y calificaciones
nombres_tareas = []
ponderaciones = []
calificaciones = []

# Solicitar la información para cada tarea
for i in range(num_tareas):
    # Solicitar el nombre de la tarea
    nombre = input(f"Ingrese el nombre de la tarea {i + 1}: ")
    # Solicitar la ponderación de la tarea
    ponderacion = float(input(f"Ingrese la ponderación de la tarea {i + 1} (en porcentaje): "))
    # Solicitar la calificación obtenida en la tarea
    calificacion = float(input(f"Ingrese la calificación obtenida en la tarea {i + 1}: "))
    
    # Almacenar los valores
    nombres_tareas.append(nombre)
    ponderaciones.append(ponderacion)
    calificaciones.append(calificacion)

# Calcular la calificación final ponderada
calificacion_final = 0
for i in range(num_tareas):
    calificacion_final += (calificaciones[i] * ponderaciones[i]) / 100  # Ponderación en porcentaje

# Mostrar el resumen del desempeño
print("\nResumen del desempeño:")
for i in range(num_tareas):
    print(f"Tarea: {nombres_tareas[i]}")
    print(f"  Calificación obtenida: {calificaciones[i]}")
    print(f"  Ponderación: {ponderaciones[i]}%")
    print()

# Mostrar la calificación final
print(f"Calificación final del curso: {calificacion_final:.2f}")
