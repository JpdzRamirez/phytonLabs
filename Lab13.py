# Función para calcular la raíz cuadrada sin usar math
def raiz_cuadrada_aproximada(numero, precision=0.00001):
    """Calcula la raíz cuadrada de un número mediante el método de Newton."""
    if numero < 0:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo."
    
    estimacion = numero / 2  # Estimación inicial
    while abs(estimacion**2 - numero) > precision:
        estimacion = (estimacion + numero / estimacion) / 2
    return estimacion

# Función para calcular la distancia entre dos puntos
def calcular_distancia():
    """Calcula la distancia entre dos puntos dados por sus coordenadas."""
    print("\nIngrese las coordenadas del primer punto (x1, y1):")
    x1 = float(input("Ingrese x1: "))
    y1 = float(input("Ingrese y1: "))
    
    print("\nIngrese las coordenadas del segundo punto (x2, y2):")
    x2 = float(input("Ingrese x2: "))
    y2 = float(input("Ingrese y2: "))

    # Fórmula de la distancia
    distancia = raiz_cuadrada_aproximada((x2 - x1)**2 + (y2 - y1)**2)
    return f"{distancia:,.2f}"  # Formato con dos decimales y separador de miles

# Función para calcular múltiples distancias
def calcular_varias_distancias():
    """Solicita varias distancias a calcular llamando la función de distancia."""
    print("\nIngrese la cantidad de distancias que desea calcular:")
    cantidad = int(input("Cantidad de distancias: "))
    resultados = []

    for i in range(cantidad):
        print(f"\nCalculando distancia {i + 1}:")
        resultado = calcular_distancia()
        resultados.append(resultado)

    return resultados

# Función de menú principal
def menu(opcion):
    """Controla el menú principal del programa."""
    if opcion == 1:
        resultado = calcular_distancia()
        return f"La distancia entre los puntos es: {resultado} unidades."
    elif opcion == 2:
        resultados = calcular_varias_distancias()
        return "\n".join([f"Distancia {i + 1}: {res}" for i, res in enumerate(resultados)])
    else:
        return "Opción no válida. Intente nuevamente."

print("Bienvenido al programa de cálculo de distancias")
opcion = -1  # opcion por defecto para ingresar al ciclo

while opcion != 0:
    print()
    print("Opciones disponibles:\n")
    print("1. Calcular la distancia entre dos puntos.")
    print("2. Calcular múltiples distancias entre puntos.")
    print("0. Salir.")
    print("\nIngrese el número de la opción que desea ejecutar (o 0 para salir):")
    opcion = int(input("Opción: "))

    if opcion == 0:
        print()
        print()
        print("\n¡Gracias por usar el programa! Hasta pronto.")
        print(f"IU Digital de Antioquia - 2024-2")
        print(f"Powered by Python 🐍")
        print(f"By: @JPDZSoftware")
    else:
        resultado = menu(opcion)
        print()
        print("**************")
        print("--Resultado---")
        print(f"\n{resultado}")

