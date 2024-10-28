import pandas as pd
from PIL import Image, ImageDraw, ImageFont

# Paso 1: Leer el archivo Excel
# Asegúrate de que el archivo Excel esté en el mismo directorio o proporciona la ruta correcta
excel_file = 'C:\\Users\\rocio\\Documents\\Otros programas\\programa_cocina\\Programa_cocina\\planilla.xlsx'
df = pd.read_excel(excel_file)

# Paso 2: Procesar los datos
# Supongamos que quieres extraer los valores de la primera fila
# Puedes ajustar esto según tus necesidades
datos_a_colocar = df.iloc[0]  # Extraer la primera fila

# Paso 3: Cargar la imagen prediseñada
imagen_base = 'C:\\Users\\rocio\\Documents\\Otros programas\\programa_cocina\\Programa_cocina\\menu.png'
img = Image.open(imagen_base)

# Configuración para el texto
draw = ImageDraw.Draw(img)
font_size = 30  # Ajusta el tamaño de la fuente según sea necesario
fuente = ImageFont.truetype('C:\\Users\\rocio\\Documents\\Otros programas\\programa_cocina\\Programa_cocina\\fuente.ttf', size=font_size)

# Coordenadas donde colocar el texto (ajusta según tu imagen)
x = 50
y = 50

# Paso 4: Añadir texto a la imagen
for i, valor in enumerate(datos_a_colocar):
    draw.text((x, y + (i * (font_size + 10))), str(valor), fill="black", font=fuente)

# Paso 5: Guardar el resultado
nueva_imagen = 'menu_editado.png'
img.save(nueva_imagen)

print(f"Imagen guardada como {nueva_imagen}")
