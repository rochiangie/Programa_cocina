import pandas as pd
from PIL import Image, ImageDraw, ImageFont

# Paso 1: Leer el archivo Excel
excel_file = 'Programa_cocina\\planilla.xlsx'
df = pd.read_excel(excel_file)

# Paso 2: Especificar las filas y columnas que quieres extraer
# Ejemplo: Extraer datos de la fila 0 y de las columnas "A" y "B"
filas_a_extraer = [0, 1]  # Lista de filas que quieres extraer
columnas_a_extraer = ["A", "B"]  # Lista de columnas que quieres extraer
datos_a_colocar = df.loc[filas_a_extraer, columnas_a_extraer]

# Paso 3: Cargar la imagen prediseñada
imagen_base = 'Programa_cocina\\menu.png'
img = Image.open(imagen_base)

# Configuración para el texto
draw = ImageDraw.Draw(img)
font_size = 50
fuente = ImageFont.truetype('Programa_cocina\\fuente.ttf', size=font_size)

# Paso 4: Posicionar los textos en la imagen
# Especifica las coordenadas para cada elemento en una lista
coordenadas = [
    (50, 50),   # Posición del primer dato
    (50, 120),  # Posición del segundo dato
    # Agrega más posiciones según lo que necesites
]

# Iterar sobre los datos y posiciones para colocar cada valor en la imagen
for i, (indice, fila) in enumerate(datos_a_colocar.iterrows()):
    for j, valor in enumerate(fila):
        x, y = coordenadas[i * len(fila) + j]  # Calcula la posición según el índice
        draw.text((x, y), str(valor), fill="black", font=fuente)

# Paso 5: Guardar el resultado
nueva_imagen = 'nueva_imagen.png'
img.save(nueva_imagen)

print(f"Imagen guardada como {nueva_imagen}")
