# Datos de la tabla
datos = [
    [1967, 54, 25.5, 128, 156.1, 207.1, 314.5, 217.5, 240.1, 109.1, 77.5, 280.2, 51.1],
    [1977, 0, 35, 85, 107, 82.1, 224, 430.5, 144, 339.5, 192, 401.5, 88],
    [1987, 27, 55, 71.9, 77.4, 139.1, 81.7, 82.6, 130.5, 78.8, 102.6, 57.4, 63.1],
    [1997, 79.6, 59.7, 38.8, 81, 111.4, 83.9, 201.8, 108.1, 57.9, 73, 77.5, 5],
    [2007, 0, 32.7, 95.4, 128.2, 88.3, 223.7, 57.9, 128.2, 58.5, 147.8, 77.3, 127.2],
    [2017, 119.1, 57.8, 210.7, 66.6, 170.8, 189.5, 190, 132.8, 52.2, 140.4, 92.7, 102.5],
]

# Inicialización
menor_precip = float('inf')
mayor_precip = float('-inf')
años_menor = []  # Lista para guardar (año, mes) con menor precipitación
años_mayor = []  # Lista para guardar (año, mes) con mayor precipitación
precip_anual = []  # Promedio anual por año
meses_prom = [0] * 12  # Suma de precipitación por mes
contador_meses = [0] * 12  # Contador de meses para calcular promedio mensual

# Procesamiento
for fila in datos:
    año = fila[0]
    precipitaciones = fila[1:]
    suma_anual = sum(precipitaciones)
    precip_anual.append((año, suma_anual))
    
    # Comparar precipitaciones mes a mes
    for mes, precip in enumerate(precipitaciones):
        meses_prom[mes] += precip
        contador_meses[mes] += 1

        #Aprovechamos el ciclo para determinar el mes con mayor y menor precipitación
        # Menor precipitación
        if precip < menor_precip:
            menor_precip = precip
            años_menor = [(año, mes + 1)]  # Reiniciar la lista
        elif precip == menor_precip:
            años_menor.append((año, mes + 1))  # Agregar si es igual
        
        # Mayor precipitación
        if precip > mayor_precip:
            mayor_precip = precip
            años_mayor = [(año, mes + 1)]  # Reiniciar la lista
        elif precip == mayor_precip:
            años_mayor.append((año, mes + 1))  # Agregar si es igual

# Calcular promedios mensuales
promedios_mensuales = [suma / contador for suma, contador in zip(meses_prom, contador_meses)]

# Determinar el año más lluvioso
max_anual = max(precip_anual, key=lambda x: x[1])[1]  # Mayor precipitación anual
años_lluviosos = [año for año, total in precip_anual if total == max_anual]

# Imprimir los resultados en el orden solicitado:

# 1. Promedio anual de precipitación
print("El promedio anual de precipitación en el Lago para cada año presentado en la tabla:")
for año, total in precip_anual:
    print(f"Año {año}: {total:.2f} mm")

# 2. Promedio mensual de precipitación
print("\nEl promedio mensual de precipitación en el Lago para cada mes presentado en la tabla:")
for i, promedio in enumerate(promedios_mensuales):
    print(f"Mes {i+1}: {promedio:.2f} mm")

# 3. El mes y año que registra menor precipitación
print("\nEl mes y año que registra menor precipitación:")
print(f"Menor precipitación: {menor_precip} mm en los siguientes meses/años:")
for año, mes in años_menor:
    print(f"Año {año}, Mes {mes}")

# 4. El año más lluvioso
print("\nEl año más lluvioso:")
print(f"Año(s) con mayor precipitación anual: {años_lluviosos}")

# 5. El mes más lluvioso
print("\nEl mes más lluvioso:")
print(f"Mayor precipitación: {mayor_precip} mm en los siguientes meses/años:")
for año, mes in años_mayor:
    print(f"Año {año}, Mes {mes}")
