import pandas as pd
from PIL import Image, ImageDraw, ImageFont

# Paso 1: Leer el archivo Excel
excel_file = 'planilla.xlsx'
df = pd.read_excel(excel_file)

# Selección de filas y columnas específicas
filas_a_extraer = [3, 9, 15, 21]  # Lista de filas que quieres extraer
columnas_a_extraer = [1, 2, 3, 4]  # Lista de columnas que quieres extraer
datos_a_colocar = df.iloc[filas_a_extraer, columnas_a_extraer]

# Paso 2: Configuración inicial de la imagen
imagen_base = 'menu.png'
img = Image.open(imagen_base)
draw = ImageDraw.Draw(img)
font_size = 15  # Ajusta el tamaño de la fuente a un valor más pequeño
fuente = ImageFont.truetype('fuente.ttf', size=font_size)

# Coordenadas del rectángulo
x1, y1 = 332, 566
x2, y2 = 1040, 883

# Calcular el área disponible para el texto
ancho_area = x2 - x1
alto_area = y2 - y1

# Posiciones iniciales y espaciado automático
espacio_vertical = font_size + 5  # Espacio entre filas
espacio_horizontal = ancho_area // len(columnas_a_extraer)  # Espacio entre columnas

# Generar y dibujar texto automáticamente
for i, fila in enumerate(datos_a_colocar.itertuples(index=False)):
    for j, valor in enumerate(fila):
        # Calcular posiciones basadas en `i` y `j`
        x = x1 + j * espacio_horizontal
        y = y1 + (i * espacio_vertical)
        if y < y2:  # Asegurarse de que el texto no se salga del área
            draw.text((x, y), str(valor), fill="black", font=fuente)

# Guardar la imagen final
nueva_imagen = 'nueva_imagen.png'
img.save(nueva_imagen)

print(f"Imagen guardada como {nueva_imagen}")



