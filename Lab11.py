# Arreglo 
conversions = [
    {"Índice": 0, "Conversión": "Kilómetro a metro", "Factor": 1000},
    {"Índice": 1, "Conversión": "Centímetro a metro", "Factor": 0.01},
    {"Índice": 2, "Conversión": "Kilómetro por hora a millas por hora", "Factor": 0.62},
    {"Índice": 3, "Conversión": "Nota en Educatic a nota en Canvas", "Factor": 20},
    {"Índice": 4, "Conversión": "Nota en Canvas a nota en Educatic", "Factor": 0.05},
    {"Índice": 5, "Conversión": "Mililitro a centímetro cúbico", "Factor": 1},
    {"Índice": 6, "Conversión": "Dólar (USA) a peso colombiano", "Factor": 4.418},
    {"Índice": 7, "Conversión": "Peso colombiano a dólar (USA)", "Factor": 0.00023},
    {"Índice": 8, "Conversión": "Libra a kilogramo", "Factor": 0.45},
    {"Índice": 9, "Conversión": "Minuto luz a kilómetro", "Factor": 17987539.67}
]

# Funciones
def kilometro_metro(kilometros):
    return kilometros * conversions[0]['Factor']

def centimetro_metro(centimetros):
    return centimetros * conversions[1]['Factor']

def kilometroHora_millasHora(kmH):
    return kmH * conversions[2]['Factor']

def notaEducatic_notaCanvas(notaEducatic):
    return notaEducatic * conversions[3]['Factor']

def notaCanvas_notaEducatic(notaCanvas):
    return notaCanvas * conversions[4]['Factor']

def mililitro_centimetroCubico(mililitro):
    return mililitro * conversions[5]['Factor']

def dolar_peso(dolar):
    return dolar * conversions[6]['Factor']

def peso_dolar(peso):
    return peso * conversions[7]['Factor']

def libra_kilogramo(libra):
    return libra * conversions[8]['Factor']

def minutosLuz_kilometro(minutrosLuz):
    return minutrosLuz * conversions[9]['Factor']

# MENÚ
def menu(value):
    if value == 1:
        kilometros = float(input("Ingresa los Kilómetros: "))            
        return f"{kilometros} km son {kilometro_metro(kilometros):.2f} mts."
    elif value == 2:
        centimetros = float(input("Ingresa los Centímetros: "))            
        return f"{centimetros} cm son {centimetro_metro(centimetros):.2f} mts."
    elif value == 3:
        kmH = float(input("Ingresa los KmH: "))            
        return f"{kmH} KmH son {kilometroHora_millasHora(kmH):.2f} Millas/Hora."
    elif value == 4:
        notaEducatic = float(input("Ingresa la nota Educatic: "))            
        return f"Nota Educatic: {notaEducatic}, Nota Canvas: {notaEducatic_notaCanvas(notaEducatic):.2f}."
    elif value == 5:
        notaCanvas = float(input("Ingresa la nota Canvas: "))            
        return f"Nota Canvas: {notaCanvas}, Nota Educatic: {notaCanvas_notaEducatic(notaCanvas):.2f}."
    elif value == 6:
        mililitro = float(input("Ingresa el mililitro: "))            
        return f"{mililitro} ml son {mililitro_centimetroCubico(mililitro):.2f} cm³."
    elif value == 7:
        dolar = float(input("Ingresa el valor en dólares: "))            
        return f"{dolar:.2f} USD son {dolar_peso(dolar):.2f} COP."
    elif value == 8:
        pesos = float(input("Ingresa el valor en pesos colombianos: "))            
        return f"{pesos} COP son {peso_dolar(pesos):.2f} USD."
    elif value == 9:
        libras = float(input("Ingresa las libras: "))            
        return f"{libras} lb son {libra_kilogramo(libras):.2f} kg."
    elif value == 10:
        minutrosLuz = float(input("Ingresa los minutos luz: "))            
        return f"{minutrosLuz} minLuz son {minutosLuz_kilometro(minutrosLuz):.2f} km."
    else:
        return "Opción no válida"

# Ciclo principal
salir = False
while not salir:
    print("\nBienvenido al ejercicio de conversiones")
    for idx, conversion in enumerate(conversions, start=1):
        print(f"{idx}. {conversion['Conversión']}")
    print("11. Salir")
    
    seleccion = input("Ingrese por favor una opción, solo el número: ")
    if seleccion.isdigit():  # Validar si es un número
        seleccion = int(seleccion)
        if seleccion == 11:
            print("¡Gracias por usar el programa! ¡Hasta pronto!")
            print(f"IU Digital de Antioquia - 2024-2")
            print(f"Powered by Python 🐍")
            print(f"By: @JPDZSoftware")
            salir = True
        elif 1 <= seleccion <= 10:
            print(menu(seleccion))
        else:
            print("Opción no válida. Inténtalo de nuevo.")
    else:
        print("Por favor, ingrese un número válido.")
