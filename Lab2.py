#Librerías
import math
#Función
def distancia(x1,y1,x2,y2):
    distancia = math.sqrt(pow((x2-x1),2)+pow((y2-y1),2))
    return distancia
#Menu
def menu(value):
    match value:
        case 1:
            x1 = float(input("Ingresa la coordenada X1: "))            
            y1 = float(input("Ingresa la coordenada Y1: "))
            x2 = float(input("Ingresa la coordenada X2: "))
            y2 = float(input("Ingresa la coordenada Y2: "))            
            resultado = distancia(x1,y1,x2,y2)
            response = f"Distancia entre las P1:({int(x1)},{int(y1)}) y P2({int(x2)},{int(y2)}) es: {resultado:,.2f}."      
            return response 
        case _:
            return "Opción no válida"
        
# Print Area
print("Bienvenido al ejercicio 2 de calculos ")
print("1. Calcular Distancia entre dos puntos")
seleccion = int(input("Ingrese por favor una opción, solo el número: "))
consulta = menu(seleccion)
print(f"El resultado de su petición es: {consulta}")
print("¡Muchas gracias! <3")