import ipywidgets as widgets
from IPython.display import display, clear_output

# Define el vector de conversiones
conversions = [
    {"Índice": 0, "Conversión": "Kilómetro a metro", "Factor": 1000},
    {"Índice": 1, "Conversión": "Centímetro a metro", "Factor": 0.01},
    {"Índice": 2, "Conversión": "Kilómetro por hora a millas por hora", "Factor": 0.62},
    {"Índice": 3, "Conversión": "Nota en Educatic a nota en Canvas", "Factor": 20},
    {"Índice": 4, "Conversión": "Nota en Canvas a nota en Educatic", "Factor": 0.05},
    {"Índice": 5, "Conversión": "Mililitro a centímetro cúbico", "Factor": 1},
    {"Índice": 8, "Conversión": "Libra a kilogramo", "Factor": 0.45},
    {"Índice": 9, "Conversión": "Minuto luz a kilómetro", "Factor": 17987539.67},
]

# Funciones de conversión
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

def libra_kilogramo(libra):
    return libra * conversions[6]['Factor']

def minutosLuz_kilometro(minutrosLuz):
    return minutrosLuz * conversions[7]['Factor']

# Función para manejar la selección y entrada de datos
# Aqui actualizamos los campos según sea el caso

def on_select(change):
    clear_output(wait=True)  # Limpia la salida anterior
    input_box.value = ""  # Limpia el campo de entrada
    output.value = ""  # Limpia el resultado
    #Opción por defecto
    if dropdown.value == "Seleccione una opción":
        # Si se selecciona "Seleccione una opción", no muestra input ni botón
        display(dropdown, output)
        return

    # Si se selecciona una opción válida, muestra input y botón
    conversion = dropdown.value
    input_label.value = f"Ingrese el valor para {conversion}:"
    display(dropdown, input_label, input_box, calculate_button, output)


#Funcion que usa las funciones de conversión según la selección
def on_calculate(button):
    # Restamos 1 porque "Seleccione una opción" es la primera posicion
    conversion_index = dropdown.options.index(dropdown.value) - 1  
    # Obtenemos el valor del input
    value = float(input_box.value)
    # Lógica estructuras condicionales
    if conversion_index == 0:
        result = kilometro_metro(value)
    elif conversion_index == 1:
        result = centimetro_metro(value)
    elif conversion_index == 2:
        result = kilometroHora_millasHora(value)
    elif conversion_index == 3:
        result = notaEducatic_notaCanvas(value)
    elif conversion_index == 4:
        result = notaCanvas_notaEducatic(value)
    elif conversion_index == 5:
        result = mililitro_centimetroCubico(value)
    elif conversion_index == 6:
        result = libra_kilogramo(value)
    elif conversion_index == 7:
        result = minutosLuz_kilometro(value)
    else:
        result = "Opción no disponible."

    # Seteamos el resultado en el Label y casteamos el numero de decimales a 2
    output.value = f"Resultado: {result:.2f}"

# Definimos los Widgets que podemos utilizar para mostrar en el display
dropdown = widgets.Dropdown(
    options=["Seleccione una opción"] + [c["Conversión"] for c in conversions],
    description="Conversión:",
    value="Seleccione una opción"
)

input_label = widgets.Label("")
input_box = widgets.Text(placeholder="Ingresa el valor aquí")
calculate_button = widgets.Button(description="Calcular")
output = widgets.Label("")

# Eventos
dropdown.observe(on_select, names='value')
calculate_button.on_click(on_calculate)

# Mostrar widgets iniciales
display(dropdown, output)