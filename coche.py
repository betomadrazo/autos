import pygame
import sys

pygame.init()

#                   RED  GREEN  BLUE
DARK_GRAY =         (130,   130,  0)
RED =               (255, 128,   0)
GREEN =             (128,   0, 128)
LINE_COLOR =        (255, 180,   0)
ACOTAMIENTO_COLOR = (50,   40,  30)
BGCOLOR = DARK_GRAY

# Set up the window
WINDOW_WIDTH = 600
WINDOW_HEIGHT =800

ACOTAMIENTO_WIDTH = 50
CAR_WIDTH = 100
CAR_HEIGHT = 180

# La velocidad del carro
SPEED = 7

RIGHT = 'right'
LEFT = 'left'
CENTER = 'center'

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Car Racing')

car_image = pygame.image.load('car.png')
car_image = pygame.transform.scale(car_image,(CAR_WIDTH, CAR_HEIGHT))
#car_image = pygame.transform.rotate(car_image, 10)

# Set up the car position and speed
car_x = (WINDOW_WIDTH // 2) - (CAR_WIDTH // 2) - 10
car_y = (WINDOW_HEIGHT) - CAR_HEIGHT - 50
car_speed = 0
limite_izquierdo = ACOTAMIENTO_WIDTH
limite_derecho = WINDOW_WIDTH - CAR_WIDTH - 50
top_line = 0
INTERVALO = 80

DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
DISPLAYSURF.fill(BGCOLOR)

window.blit(car_image, (car_x, car_y))

def drawLine(top_of_line):
    #                          LEFT                  TOP         WIDTH          HEIGHT
    carril1 = pygame.Rect((WINDOW_WIDTH / 2) - 20, top_of_line - INTERVALO * 2, 10, INTERVALO)
    carril2 = pygame.Rect((WINDOW_WIDTH / 2) - 20, top_of_line                , 10, INTERVALO)
    carril3 = pygame.Rect((WINDOW_WIDTH / 2) - 20, top_of_line + INTERVALO * 2, 10, INTERVALO)
    carril4 = pygame.Rect((WINDOW_WIDTH / 2) - 20, top_of_line + INTERVALO * 4, 10, INTERVALO)
    carril5 = pygame.Rect((WINDOW_WIDTH / 2) - 20, top_of_line + INTERVALO * 6, 10, INTERVALO)
    carril6 = pygame.Rect((WINDOW_WIDTH / 2) - 20, top_of_line + INTERVALO * 8, 10, INTERVALO)

    pygame.draw.rect(DISPLAYSURF, LINE_COLOR, carril1)
    pygame.draw.rect(DISPLAYSURF, LINE_COLOR, carril2)
    pygame.draw.rect(DISPLAYSURF, LINE_COLOR, carril3)
    pygame.draw.rect(DISPLAYSURF, LINE_COLOR, carril4)
    pygame.draw.rect(DISPLAYSURF, LINE_COLOR, carril5)
    pygame.draw.rect(DISPLAYSURF, LINE_COLOR, carril6)

def rotate_car(car, direction):
    if direction == RIGHT:
        return pygame.transform.rotate(car, 10)
    if direction == LEFT:
        return pygame.transform.rotate(car, -10)
    
    # return pygame.transform.rotate(car, 0)


move = top_line
# Run the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                move += 3
            if event.key == pygame.K_LEFT:
                car_speed = -SPEED
                car_image = rotate_car(car_image, LEFT)
            elif event.key == pygame.K_RIGHT:
                car_speed = SPEED
                car_image = rotate_car(car_image, RIGHT)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                move = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                car_speed = 0
                car_image = rotate_car(car_image, CENTER)

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_SPACE]:
            #print("XXXXXXXXXXXX")
            if move < 15:
                move += 1

    # Move the car

    car_x += car_speed
    top_line += move

    if car_x < limite_izquierdo:
        car_x -= car_speed
    if car_x > limite_derecho:
        car_x -= car_speed

    if top_line > INTERVALO * 2:
        top_line = 0

    # Crear unos rectángulos(Rect) que representan el carril y las orillas
    # Primero se crean las medidas, y luego se dibujan
    #                                   LEFT                              TOP   WIDTH              HEIGHT
    raya =                  pygame.Rect((WINDOW_WIDTH / 2) - 20,          0,                   10, WINDOW_HEIGHT)


    acotamiento_izquierdo = pygame.Rect(0,                                0,    ACOTAMIENTO_WIDTH, WINDOW_HEIGHT)
    acotamiento_derecho =   pygame.Rect(WINDOW_WIDTH - ACOTAMIENTO_WIDTH, 0,    ACOTAMIENTO_WIDTH, WINDOW_HEIGHT)

    # Redibujar fondo
    DISPLAYSURF.fill(BGCOLOR)
    # Redibujar carril
    # pygame.draw.rect(DISPLAYSURF, BGCOLOR, raya)

    drawLine(top_line)
    # top_line = top_line + 2

    # Redibujar orillas
    pygame.draw.rect(DISPLAYSURF, ACOTAMIENTO_COLOR, acotamiento_izquierdo)
    pygame.draw.rect(DISPLAYSURF, ACOTAMIENTO_COLOR, acotamiento_derecho)
    # Redibujar el auto
    window.blit(car_image, (car_x, car_y))

    # Update the window
    pygame.display.update()
