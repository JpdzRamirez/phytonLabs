def binario_a_decimal(binario):
    decimal = 0
    for i, bit in enumerate(reversed(binario)):
        decimal += int(bit) * (2 ** i)
    return decimal

def hexadecimal_a_decimal(hexadecimal):
    hex_digitos = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                   '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    decimal = 0
    for i, digito in enumerate(reversed(hexadecimal.upper())):
        decimal += hex_digitos[digito] * (16 ** i)
    return decimal

def decimal_a_binario(decimal):
    binario = []
    while decimal > 0:
        binario.append(str(decimal % 2))
        decimal //= 2
    return ''.join(reversed(binario)) if binario else '0'

def decimal_a_hexadecimal(decimal):
    hex_digitos = '0123456789ABCDEF'
    hexadecimal = []
    while decimal > 0:
        hexadecimal.append(hex_digitos[decimal % 16])
        decimal //= 16
    return ''.join(reversed(hexadecimal)) if hexadecimal else '0'

def binario_a_hexadecimal(binario):
    decimal = binario_a_decimal(binario)
    return decimal_a_hexadecimal(decimal)

def hexadecimal_a_binario(hexadecimal):
    decimal = hexadecimal_a_decimal(hexadecimal)
    return decimal_a_binario(decimal)

# Opciones del menú
opciones = [
    "Binario a Decimal",
    "Hexadecimal a Decimal",
    "Decimal a Binario",
    "Decimal a Hexadecimal",
    "Binario a Hexadecimal",
    "Hexadecimal a Binario",
    "Salir"
]

while True:
    # Mostrar menú de opciones
    print("\nSeleccione la conversión que desea realizar:")
    for i, opcion in enumerate(opciones):
        print(f"{i}. {opcion}")
    
    # Solicitar opción al usuario
    opcion = int(input("Ingrese el número de la opción: "))

    if opcion == 6:  # Salir
        print("Saliendo del programa. ¡Hasta luego!")
        break

    # Solicitar el valor a convertir
    valor = input("Ingrese el valor a convertir: ")

    # Realizar la conversión según la opción seleccionada
    if opcion == 0:  # Binario a Decimal
        resultado = binario_a_decimal(valor)
    elif opcion == 1:  # Hexadecimal a Decimal
        resultado = hexadecimal_a_decimal(valor)
    elif opcion == 2:  # Decimal a Binario
        resultado = decimal_a_binario(int(valor))
    elif opcion == 3:  # Decimal a Hexadecimal
        resultado = decimal_a_hexadecimal(int(valor))
    elif opcion == 4:  # Binario a Hexadecimal
        resultado = binario_a_hexadecimal(valor)
    elif opcion == 5:  # Hexadecimal a Binario
        resultado = hexadecimal_a_binario(valor)
    else:
        print("Opción no válida. Intente nuevamente.")
        continue

    # Mostrar el resultado
    print(f"El resultado de la conversión es: {resultado}")
