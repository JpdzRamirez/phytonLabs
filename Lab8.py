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
        print()
        print(f"El resultado de la conversión es: {resultado}")
        print(f"IU Digital de Antioquia - 2024-2")
        print(f"Powered by Python 🐍")
        print(f"By: @JPDZSoftware")
        break

    # Solicitar el valor a convertir
    valor = input("Ingrese el valor a convertir: ")

    if opcion == 0:  # Binario a Decimal
        decimal = 0
        for i, bit in enumerate(reversed(valor)):
            decimal += int(bit) * (2 ** i)
        resultado = decimal

    elif opcion == 1:  # Hexadecimal a Decimal
        hex_digitos = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                       '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
        decimal = 0
        for i, digito in enumerate(reversed(valor.upper())):
            decimal += hex_digitos[digito] * (16 ** i)
        resultado = decimal

    elif opcion == 2:  # Decimal a Binario
        decimal = int(valor)
        binario = []

        while decimal > 0:
            residuo = decimal % 2  # Residuo de la división entre 2
            binario.append(str(residuo))  # Guardar el residuo
            decimal //= 2  # Reducir el valor dividiéndolo entre 2

        # Construir el binario (invirtiendo la lista)
        if binario:
            resultado = ''.join(reversed(binario))  # Invertir y unir la lista
        else:
            resultado = '0'  # Caso especial para 0



    elif opcion == 3:  # Decimal a Hexadecimal
        decimal = int(valor)
        hex_digitos = '0123456789ABCDEF'
        hexadecimal = []
        while decimal > 0:
            # Calcular el residuo
            residuo = decimal
            while residuo >= 16:
                residuo -= 16
            hexadecimal.append(hex_digitos[residuo])

            # Calcular el cociente
            nuevo_decimal = 0
            multiplicador = 1
            while decimal >= 16:
                decimal -= 16
                nuevo_decimal += multiplicador
                multiplicador += 1
            decimal = nuevo_decimal
            #como los resultados los obtenemos de forma invertida
        if hexadecimal:  # Verificar si la lista 'hexadecimal' tiene elementos
            resultado = ''.join(reversed(hexadecimal))  # Invertir la lista y unir los elementos en un solo string
        else:  # Si la lista está vacía
            resultado = '0'  # El resultado es '0'

    elif opcion == 4:  # Binario a Hexadecimal
        decimal = 0
        for i, bit in enumerate(reversed(valor)):
            decimal += int(bit) * (2 ** i)
        hex_digitos = '0123456789ABCDEF'
        hexadecimal = []
        while decimal > 0:
            residuo = decimal
            while residuo >= 16:
                residuo -= 16
            hexadecimal.append(hex_digitos[residuo])

            nuevo_decimal = 0
            multiplicador = 1
            while decimal >= 16:
                decimal -= 16
                nuevo_decimal += multiplicador
                multiplicador += 1
            decimal = nuevo_decimal
            #como los resultados los obtenemos de forma invertida
        if hexadecimal:  # Verificar si la lista 'hexadecimal' tiene elementos
            resultado = ''.join(reversed(hexadecimal))  # Invertir la lista y unir los elementos en un solo string
        else:  # Si la lista está vacía
            resultado = '0'  # El resultado es '0'


    elif opcion == 5:  # Hexadecimal a Binario
        hex_digitos = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                    '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
        decimal = 0

        # Convertir hexadecimal a decimal
        for i, digito in enumerate(reversed(valor.upper())):
            decimal += hex_digitos[digito] * (16 ** i)

        # Convertir decimal a binario
        binario = []
        while decimal > 0:
            residuo = decimal % 2  # Residuo de la división entre 2
            binario.append(str(residuo))  # Guardar el residuo
            decimal //= 2  # Reducir el valor dividiéndolo entre 2

        # Construir el binario (invirtiendo la lista)
        if binario:
            resultado = ''.join(reversed(binario))  # Invertir y unir la lista
        else:
            resultado = '0'  # Caso especial para 0


    else:
        print("Opción no válida. Intente nuevamente.")
        continue

    # Mostrar el resultado
    print()
    print(f"El resultado de la conversión es: {resultado}")
    print(f"IU Digital de Antioquia - 2024-2")
    print(f"Powered by Python 🐍")
    print(f"By: @JPDZSoftware")
