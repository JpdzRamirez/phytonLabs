# Creando variables de texto
texto1 = "Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500."
texto2 = "Es un hecho establecido hace demasiado tiempo que un lector se distraerá con el contenido del texto de un sitio mientras que mira su diseño."
texto3 = "Lorem Ipsum va a dar por resultado muchos sitios web que usan este texto si se encuentran en estado de desarrollo"

# Slicing Ascendente
slicing_ascendente_1 = texto1[0:10]  
slicing_ascendente_2 = texto2[11:23]  
slicing_ascendente_3 = texto3[0:25]   
slicing_ascendente_4 = texto1[20:40] 
slicing_ascendente_5 = texto2[0:6]  

# Slicing Descendente
slicing_descendente_1 = texto1[-11:]       
slicing_descendente_2 = texto2[-25:-15]    
slicing_descendente_3 = texto3[-25:]       
slicing_descendente_4 = texto1[-40:-20]    
slicing_descendente_5 = texto2[::-1]       

# Imprimir resultados
print("Slicing Ascendente:")
print(slicing_ascendente_1)
print(slicing_ascendente_2)
print(slicing_ascendente_3)
print(slicing_ascendente_4)
print(slicing_ascendente_5)

print("\nSlicing Descendente:")
print(slicing_descendente_1)
print(slicing_descendente_2)
print(slicing_descendente_3)
print(slicing_descendente_4)
print(slicing_descendente_5)