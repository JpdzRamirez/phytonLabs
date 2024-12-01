# Factores de conversión
conversiones = [
    1000,          # Kilómetro a metro
    0.01,          # Centímetro a metro
    0.62,          # Kilómetro por hora a millas por hora
    20,            # Nota en Educatic a nota en Canvas
    0.05,          # Nota en Canvas a nota en Educatic
    1,             # Mililitro a centímetro cúbico
    4.418,         # Dólar (USA) a peso colombiano 
    0.00023,       # Peso colombiano a dólar (USA) 
    0.45,          # Libra a kilogramo
    17987539.67    # Minuto luz a kilómetro
]

# Descripciones de las conversiones
descripciones = [
    "Kilómetro a metro",
    "Centímetro a metro",
    "Kilómetro por hora a millas por hora",
    "Nota en Educatic a nota en Canvas",
    "Nota en Canvas a nota en Educatic",
    "Mililitro a centímetro cúbico",
    "Dólar (USA) a peso colombiano",
    "Peso colombiano a dólar (USA)",
    "Libra a kilogramo",
    "Minuto luz a kilómetro"
]

while True:
    # Mostrar opciones al usuario
    print("\nSeleccione el tipo de conversión:")
    for i, descripcion in enumerate(descripciones):
        print(f"{i}. {descripcion}")
    print(f"{len(descripciones)}. Salir")  # Opción para salir

    # Solicitar al usuario la conversión
    opcion = int(input("Ingrese el índice de la conversión que desea realizar: "))

    # Verificar si el usuario eligió salir
    if opcion == len(descripciones):
        print("Saliendo del programa. ¡Hasta luego!")
        break

    # Validar si la opción es válida
    if 0 <= opcion < len(conversiones):
        # Verificar si el factor está disponible
        if conversiones[opcion] is not None:
            # Solicitar el valor a convertir
            valor = float(input(f"Ingrese el valor en {descripciones[opcion].split(' a ')[0]}: "))
            
            # Realizar la conversión
            resultado = valor * conversiones[opcion]
            print(f"El resultado de la conversión es: {resultado:.2f} {descripciones[opcion].split(' a ')[1]}")
        else:
            print("Esta conversión requiere un valor actualizado manualmente. Inténtelo más tarde.")
    else:
        print("Opción no válida. Por favor, intente nuevamente.")