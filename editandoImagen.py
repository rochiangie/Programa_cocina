import cv2

# Cargar la imagen
image = cv2.imread('menu.png')

# Mostrar la imagen
cv2.imshow('Imagen', image)

# Inicializar la lista de puntos
points = []

# Función para capturar los puntos del rectángulo
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        cv2.circle(image, (x, y), 5, (0, 255, 0), -1)
        cv2.imshow('Imagen', image)

        # Si se han seleccionado dos puntos, dibujar el rectángulo
        if len(points) == 2:
            cv2.rectangle(image, points[0], points[1], (255, 0, 0), 2)
            cv2.imshow('Imagen', image)
            print(f'Coordenadas del rectángulo: {points[0]} y {points[1]}')

# Configurar el evento de clic
cv2.setMouseCallback('Imagen', click_event)

# Esperar hasta que se presione una tecla
cv2.waitKey(0)
cv2.destroyAllWindows()