import pandas as pd
from PIL import Image, ImageDraw, ImageFont

# Paso 1: Leer el archivo Excel
excel_file = 'planilla.xlsx'
df = pd.read_excel(excel_file)

# Selección de filas y columnas específicas
filas_a_extraer = [3, 9, 15, 21]  # Lista de filas que quieres extraer
columnas_a_extraer = [1, 2, 3, 4]  # Lista de columnas que quieres extraers
datos_a_colocar = df.iloc[filas_a_extraer, columnas_a_extraer]

# Paso 2: Configuración inicial de la imagen
imagen_base = 'menu.png'
img = Image.open(imagen_base)
draw = ImageDraw.Draw(img)
font_size = 30
fuente = ImageFont.truetype('fuente.ttf', size=font_size)

# Posiciones iniciales y espaciado automático
x_inicial, y_inicial = 400, 400
espacio_vertical = font_size + 10  # Espacio entre filas
espacio_horizontal = 200           # Espacio entre columnas

# Generar y dibujar texto automáticamente
for i, fila in enumerate(datos_a_colocar.itertuples(index=False)):
    for j, valor in enumerate(fila):
        # Calcular posiciones basadas en `i` y `j`
        x = x_inicial + j * espacio_horizontal
        y = y_inicial + i * espacio_vertical
        draw.text((x, y), str(valor), fill="black", font=fuente)

# Guardar la imagen final
nueva_imagen = 'nueva_imagen.png'
img.save(nueva_imagen)

print(f"Imagen guardada como {nueva_imagen}")
