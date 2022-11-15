#!/usr/bin/python3
# Gabriel Baltodano Dormond C00906
# Enrique Munoz Vieto C15396
# Se importa la biblioteca pygame para realizar el pictionary y sys para cerrar
# la aplicaion
import sys
import pygame


# para hacer la linea mas fina


pygame.init()

# Se definen condiciones para el espacio de dibujo
ancho = 1000
largo = 1000
fps = 300  # Se utiliza para restingir la cantidad maxima de fps
fpsClock = pygame.time.Clock()
pantalla = pygame.display.set_mode((ancho, largo), pygame.RESIZABLE)


# Se crea una lista para guardar botones

lista = []
# colo de inicio
inicioColor = [0, 0, 0]
# tamano del lapiz
tamanolapiz = 10
# Area para dibujar
AreaDibujo = [800, 800]
# Se define una clase para los botones de la interfaz


class botones ():
    # Funcion para camniar de color
    def changeColor(color):
        global inicioColor
        inicioColor = color

    # Funcion para guardar archivo
    def guardar():
        pygame.image.save(AreaDibujo, 'dibujojuego.png')


# Definiendo el area asignada de dibujo
espacio = pygame.Surface(AreaDibujo)
espacio.fill((255, 255, 255))
# Bucle para juego
while True:
    pantalla.fill((30, 30, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for objeto in lista:
        objeto.process()

# ahora se centra el espacio de dibujo

    x, y = pantalla.get_size()
    pantalla.blit(espacio, [x/2 - AreaDibujo[0]/2, y/2 - AreaDibujo[1]/2])

    if pygame.mouse.get_pressed()[0]:
        mx, my = pygame.mouse.get_pos()
        # se encuentra posicion en el AreaDibujo
        dx = mx - x/2 + AreaDibujo[0]/2
        dy = my - y/2 + AreaDibujo[1]/2
        pygame.draw.circle(
            espacio,
            inicioColor,
            [dx, dy],
            tamanolapiz,

         )
    # guia para obsrvar adonde se esta dibujando

    pygame.draw.circle(
        pantalla,
        inicioColor,
        [100, 100],
        tamanolapiz,
    )
    pygame.display.flip()
    fpsClock.tick(fps)
