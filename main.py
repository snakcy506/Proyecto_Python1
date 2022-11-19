#!/usr/bin/python3
# Gabriel Baltodano Dormond C00906
# Enrique Munoz Vieto C15396
# Se importa la biblioteca pygame para realizar el pictionary y sys para cerrar
# la aplicaion
# Documentacion https://www.pygame.org/docs/
import pygame
import sys


pygame.init()

ancho = 1200
largo = 1000
fps = 350
fpsReloj = pygame.time.Clock()
pantalla = pygame.display.set_mode([ancho, largo], pygame.RESIZABLE)
pygame.display.set_caption('Menu')
main_menu = False
font = pygame.font.Font('freesansbold.ttf', 24)
bg = pygame.transform.scale(pygame.image.load('Logo.png'), (700, 700))
menu_commando = 0  # Cuenta si se presiona un boton en la interfaz
# color de inicio
inicioColor = [0, 0, 0]
# tamano del lapiz
tamanolapiz = 10
# Area para dibujar
AreaDibujo = [800, 800]
AreaChat = [200, 1000]


# clase para botones del juego
class botones:
    # Se nombran las caracteristicas del objeto
    def __init__(self, txt, pos):
        self.text = txt
        self.pos = pos
        self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), (260, 40))

    # Dibuja el boton el la interfaz
    def draw(self):
        pygame.draw.rect(pantalla, 'light gray', self.button, 0, 5)
        pygame.draw.rect(pantalla, 'dark gray', [self.pos[0], self.pos[1], 260, 40], 5, 5)
        text2 = font.render(self.text, True, 'black')
        pantalla.blit(text2, (self.pos[0] + 15, self.pos[1] + 7))

    # Revisa si se presiona el boton
    def revisionClick(self):
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False


# Definiendo el area asignada de dibujo
espacio = pygame.Surface(AreaDibujo)
espacio.fill((255, 255, 255))  # se llena el espacio con color blanco

# Definiendo espacio de chat
espacio_Chat = pygame.Surface(AreaChat)
espacio_Chat.fill((83, 134, 139))


# Funcion que define como se juega el juego
def juego():

    pygame.display.set_caption('DIBUJA2!')

    # bucle de juego
    while True:
        pantalla.fill((30, 30, 30))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # ahora se centra el espacio de dibujo

        x, y = pantalla.get_size()
        pantalla.blit(espacio, [x/2 - AreaDibujo[0]/2, y/2 - AreaDibujo[1]/2])

        # Se determina si el usurario dibuja
        if pygame.mouse.get_pressed()[0]:
            mx, my = pygame.mouse.get_pos()
            # se encuentra posicion en el AreaDibujo al presionar el mouse
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
        fpsReloj.tick(fps)


# Funcion para menu de incicio
def draw_menu():
    pantalla.blit(bg, (500, 175))
    titulo = font.render('DIBUJA 2!', True, 'blue')
    pantalla.blit(titulo, (850, 100))
    menu_btn = botones('INICIAR', (800, 450))
    menu_btn.draw()
    menu = menu_btn.revisionClick()

    return menu


# Secuencia del juego
run = True
while run:
    pantalla.fill('light yellow')
    fpsReloj.tick(fps)
    if main_menu:
        menu_commando = juego()
        if menu_commando != -1:
            main_menu = False
    else:
        main_menu = draw_menu()
        

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
