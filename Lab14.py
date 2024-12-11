# Función para solicitar la información de las tareas
def obtener_informacion_tareas(num_tareas):
    nombres_tareas = []
    ponderaciones = []
    calificaciones = []
    
    for i in range(num_tareas):
        nombre = input(f"Ingrese el nombre de la tarea {i + 1}: ")
        ponderacion = float(input(f"Ingrese el valor total de la tarea {i + 1} (en porcentaje %): "))
        calificacion = float(input(f"Ingrese la calificación obtenida en la tarea {i + 1}: "))
        
        # Almacenar los valores
        nombres_tareas.append(nombre)
        ponderaciones.append(ponderacion)
        calificaciones.append(calificacion)
    
    return nombres_tareas, ponderaciones, calificaciones

# Función para calcular la calificación final ponderada
def calcular_calificacion_final(ponderaciones, calificaciones):
    calificacion_final = 0
    for i in range(len(ponderaciones)):
        calificacion_final += (calificaciones[i] * ponderaciones[i]) / 100  # Ponderación en porcentaje
    
    return calificacion_final

# Función para mostrar el resumen y la calificación final
def mostrar_resumen(nombres_tareas, ponderaciones, calificaciones, calificacion_final):
    print("\nResumen del desempeño:")
    for i in range(len(nombres_tareas)):
        print(f"Tarea: {nombres_tareas[i]}")
        print(f"  Calificación obtenida: {calificaciones[i]}")
        print(f"  Ponderación: {ponderaciones[i]}%")
        print()

    print(f"Calificación final del curso: {calificacion_final:.2f}")
    if calificacion_final >= 3.0:
        print("¡Felicidades! Has aprobado el curso. 🎉")
    else:
        print("Lo siento, no has aprobado el curso. 😢")
        print("Recuerda que la calificación mínima para aprobar es 3.0.")
        print("¡Ánimo! Puedes intentarlo de nuevo. 💪")

# Función principal que organiza todo el flujo
def main():
    # Solicitar la cantidad de tareas
    num_tareas = int(input("Ingrese el número de entregas en el curso: "))
    
    # Obtener la información de las tareas
    nombres_tareas, ponderaciones, calificaciones = obtener_informacion_tareas(num_tareas)
    
    # Calcular la calificación final
    calificacion_final = calcular_calificacion_final(ponderaciones, calificaciones)
    
    # Mostrar el resumen y la calificación final
    mostrar_resumen(nombres_tareas, ponderaciones, calificaciones, calificacion_final)
    
    # Información adicional
    print(f"\nIU Digital de Antioquia - 2024-2")
    print(f"Powered by Python 🐍")
    print(f"By: @JPDZSoftware")

# Ejecutar la función principal
main()
