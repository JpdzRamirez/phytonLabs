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
    {"Índice": 9, "Conversión": "Minuto luz a kilómetro", "Factor": 17987539.67},
]

# Funciones
# 1. Kilómetro a metro
def kilometro_metro(kilometros):
    metros = (kilometros * conversions[0]['Factor'])
    return metros

# 2. Centímetro a metro
def centimetro_metro(centimetros):
    metros = (centimetros * conversions[1]['Factor'])
    return metros

# 3. Kilómetro por hora a millas por hora
def kilometroHora_millasHora(kmH):
    miH = (kmH * conversions[2]['Factor'])
    return miH

# 4. Nota en Educatic a nota en Canvas
def notaEducatic_notaCanvas(notaEducatic):
    notaCanvas = (notaEducatic * conversions[3]['Factor'])
    return notaCanvas

# 5. Nota en Canvas a nota en Educatic
def notaCanvas_notaEducatic(notaCanvas):
    notaEducatic = (notaCanvas * conversions[4]['Factor'])
    return notaEducatic

# 6. Mililitro a centímetro cúbico
def mililitro_centimetroCubico(mililitro):
    cmcubico = (mililitro * conversions[5]['Factor'])
    return cmcubico

# 7. Dólar (USA) a peso colombiano
def dolar_peso(dolar):
    peso = (dolar * conversions[6]['Factor'])
    return peso

# 8. Peso colombiano a dólar (USA)
def peso_dolar(peso):
    dolar = (peso * conversions[7]['Factor'])
    return dolar

# 9. Libra a kilogramo
def libra_kilogramo(libra):
    kilogramo = (libra * conversions[8]['Factor'])
    return kilogramo

# 10. Minuto luz a kilómetro
def minutosLuz_kilometro(minutrosLuz):
    km = (minutrosLuz * conversions[9]['Factor'])
    return km

# MENÚ
def menu(value):
    match value:
        case 1:
            kilometros = float(input("Ingresa los Kilómetros: "))            
            resultado = kilometro_metro(kilometros)
            response = f"{kilometros} km son {resultado:.2f} mts."      
            return response  
        case 2:
            centimetros = float(input("Ingresa los Centímetros: "))            
            resultado = centimetro_metro(centimetros)
            response = f"{centimetros} cm son {resultado:.2f} mts."  
            return response
        case 3:
            kmH = float(input("Ingresa los KmH: "))            
            resultado = kilometroHora_millasHora(kmH)
            response = f"{kmH} KmH son {resultado:.2f} Millas/Hora."  
            return response 
        case 4:
            notaEducatic = float(input("Ingresa la nota Educatic: "))            
            resultado = notaEducatic_notaCanvas(notaEducatic)
            response = f"Nota Educatic: {notaEducatic}, Nota Canvas: {resultado:.2f}."  
            return response   
        case 5:
            notaCanvas = float(input("Ingresa la nota Canvas: "))            
            resultado = notaCanvas_notaEducatic(notaCanvas)
            response = f"Nota Canvas: {notaCanvas}, Nota Educatic: {resultado:.2f}."  
            return response   
        case 6:
            mililitro = float(input("Ingresa el mililitro: "))            
            resultado = mililitro_centimetroCubico(mililitro)
            response = f"{mililitro} ml son {resultado:.2f} cm³."  
            return response   
        case 7:
            dolar = float(input("Ingresa el valor en dólares: "))            
            resultado = dolar_peso(dolar)
            response = f"{dolar:.2f} USD son {resultado:.2f} COP."  
            return response   
        case 8:
            pesos = float(input("Ingresa el valor en pesos colombianos: "))            
            resultado = peso_dolar(pesos)
            response = f"{pesos} COP son {resultado:.2f} USD."  
            return response   
        case 9:
            libras = float(input("Ingresa las libras: "))            
            resultado = libra_kilogramo(libras)
            response = f"{libras} lb son {resultado:.2f} kg."  
            return response   
        case 10:
            minutrosLuz = float(input("Ingresa los minutos luz: "))            
            resultado = minutosLuz_kilometro(minutrosLuz)
            response = f"{minutrosLuz} minLuz son {resultado:.2f} km."  
            return response              
        case _:
            return "Opción no válida"
        
# Print Area
print("Bienvenido al ejercicio 1 de conversiones")
index = 1
for conversion in conversions:
    print(f"{index}. Conversión {conversion['Conversión']}")
    index += 1

seleccion = int(input("Ingrese por favor una opción, solo el número:"))
consulta = menu(seleccion)
print(f"El resultado de su petición es: {consulta}")
print("¡Muchas gracias! <3")
