# Librerias
from IPython.display import display
import ipywidgets as widgets

# Definir los widgets para las entradas de cada calificación
calificacion1 = widgets.FloatText(description="Tarea 01:", value=0.0)
calificacion2 = widgets.FloatText(description="Tarea 02:", value=0.0)
calificacion3 = widgets.FloatText(description="Tarea 03:", value=0.0)
calificacion4 = widgets.FloatText(description="Tarea 04:", value=0.0)

# Botón para calcular la calificación final
boton_calcular = widgets.Button(description="Calcular calificación final")

# Función para calcular la calificación final
def calcular_calificacion(b):
    # Definimos los pesos para cada actividad
    ponderacion = 0.25
    # Calculamos la calificación final
    calificacion_final = (
        calificacion1.value * ponderacion +
        calificacion2.value * ponderacion +
        calificacion3.value * ponderacion +
        calificacion4.value * ponderacion
    )
    # Mostrar el resultado
    print(f"\nLa calificación final del curso es: {calificacion_final:.2f}")

# Asignamos la función al evento de clic del botón
boton_calcular.on_click(calcular_calificacion)

# Mostrar los widgets y el botón en el formulario
display(calificacion1, calificacion2, calificacion3, calificacion4, boton_calcular)