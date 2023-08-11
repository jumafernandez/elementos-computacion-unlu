import matplotlib.pyplot as plt
import matplotlib.patches as patches

def plot_rect_and_point(x1, y1, x2, y2, x_punto, y_punto):
    fig, ax = plt.subplots()

    # Dibuja el rectángulo
    rect = patches.Rectangle((x1, y1), x2 - x1, y2 - y1, linewidth=1, edgecolor='blue', facecolor='none')
    ax.add_patch(rect)

    # Dibuja el punto en rojo
    ax.plot(x_punto, y_punto, 'ro')

    # Configuración del gráfico
    ax.set_xlim(min(x1, x2, x_punto) - 1, max(x1, x2, x_punto) + 1)
    ax.set_ylim(min(y1, y2, y_punto) - 1, max(y1, y2, y_punto) + 1)
    ax.set_aspect('equal', 'box')
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.spines['right'].set_visible(False)  # Oculta el eje derecho
    ax.spines['top'].set_visible(False)    # Oculta el eje superior
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    
    ax.set_title('Rectángulo y Punto')

    plt.show()



x1 = float(input("Ingrese la coordenada x del vértice 1: "))
y1 = float(input("Ingrese la coordenada y del vértice 1: "))
x2 = float(input("Ingrese la coordenada x del vértice 2: "))
y2 = float(input("Ingrese la coordenada y del vértice 2: "))
x_punto = float(input("Ingrese la coordenada x del punto: "))
y_punto = float(input("Ingrese la coordenada y del punto: "))

plot_rect_and_point(x1, y1, x2, y2, x_punto, y_punto)
