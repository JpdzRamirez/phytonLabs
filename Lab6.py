# Define el vector de opciones
conversions = [
    {"Índice": 0, "Funcion": "¿Es Triangolo?"},
]

# Funciones
# 1. Numero a Hexadecimal
def es_triangulo():
        
        #Todo es triangulo hasta que se demuestre lo contrario
        esTriangulo_lados=True
        esTriangulo_angulos=True

        print("A continuación ingresa por favor 3 lados del angulo en cm")

        lado_1 = int(input("Ingrese el lado 1: "))
        lado_2 = int(input("Ingrese el lado 2: "))
        lado_3 = int(input("Ingrese el lado 3: "))


        if lado_1 + lado_2 <= lado_3 or lado_1 + lado_3 <= lado_2 or lado_2 + lado_3 <= lado_1:
            esTriangulo_lados=False

        print("A continuación ingresa por favor 3 lados del angulo")

        angulo_1 = float(input("Ingrese el ángulo 1: "))
        angulo_2 = float(input("Ingrese el ángulo 2: "))
        angulo_3 = float(input("Ingrese el ángulo 3: "))


        if angulo_1 <= 0 or angulo_2 <= 0 or angulo_3 <= 0 or (angulo_1 + angulo_2 + angulo_3 != 180):
            esTriangulo_angulos=False

        if esTriangulo_lados and esTriangulo_angulos:
            return "Es triangulo -> ¡Dibujalo mano!" 
        else:
            return "Error: No es triangulo"     

# MENÚ
def menu(value):

    if value == 1:
        resultado = es_triangulo()
        response = f"El Triangulo es {resultado}."      
        return response  
    
    else:
        return "Opción no válida"
        
# Print Area
print("Bienvenido al ejercicio 3 de Estructuras de control")
print("Propiedades de los triángulos:\n")
print("- Si tenemos tres segmentos de cualquier longitud, no siempre se puede construir un triángulo con ellos. En cualquier triángulo, la suma de dos de sus lados siempre es mayor que el tercer lado.")
print("- La suma de los ángulos de un triángulo es igual a 180°.")

index = 1

for conversion in conversions:
    print(f"{index}. Conversión {conversion['Funcion']}")
    index += 1

seleccion = int(input("Ingrese por favor una opción, solo el número:"))
consulta = menu(seleccion)
print(f"El resultado de su petición es: {consulta}")
print("¡Muchas gracias! <3")
