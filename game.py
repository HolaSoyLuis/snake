import sys, pygame, random
from pygame.locals import *
import pygame.event

pygame.init()

square_size = 16
square_x = 45
square_y = 40
screen_width = square_x * square_size
screen_height = square_y * square_size
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake')

# background
pygame.mixer.music.load('sound/dk.mp3')
pygame.mixer.music.play()
grow = pygame.mixer.Sound('sound/grow.wav')

def draw_background():
    background_img = pygame.image.load('img/white.png')
    for i in range(0, square_y):
        for j in range(0, square_x):
            screen.blit(background_img, (j * square_size, i * square_size))

# Game resolutions per square size
# 16*30 = 480
# 16*40 = 640
# 16*45 = 720
# end background

# snake and point
class snake_point:
    x, y = 0, 0
    img = pygame.image.load('img/red.png')

    def __init__(self, x_, y_):
        self.x = x_
        self.y = y_

    def draw_image(self):
        screen.blit(self.img, (self.x * square_size, self.y * square_size))


class snake:
    image = pygame.image.load('img/red.png')
    snake_body = []
    snake_is_in_live = True
    score = 0

    # start point
    snake_x, snake_y = 0, 0
    aux = snake_point(0, 0)

    def __init__(self):
        self.snake_x = random.randint(0, screen_width / square_size)
        self.snake_y = random.randint(0, screen_height / square_size)
        self.snake_body.append(snake_point(self.snake_x, self.snake_y))

    def add_point(self, x_, y_):
        self.snake_body.append(snake_point(x_, y_))

    def draw_points(self):
        for i in range(len(self.snake_body)):
            # print(len(self.snake_body))
            self.snake_body[i].draw_image()


class point:
    x, y = 0, 0
    img = pygame.image.load('img/green.png')

    def __init__(self):
        self.x = random.randint(0, screen_width / square_size)
        self.y = random.randint(0, screen_height / square_size)

    def get_random(self):
        self.x = random.randint(0, screen_width / square_size)
        self.y = random.randint(0, screen_height / square_size)

    def draw_image(self):
        screen.blit(self.img, (self.x * square_size, self.y * square_size))
# end snake and point

snk = snake()
pnt = point()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                # snk.snake_y += 1
                snk.snake_body[0].y += 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # snk.snake_y -= 1
                snk.snake_body[0].y -= 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # snk.snake_x -= 1
                snk.snake_body[0].x -= 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # snk.snake_x += 1
                snk.snake_body[0].x += 1

    draw_background()
    pnt.draw_image()
    snk.draw_points()
    # print(len(snk.snake_body))
    '''
    for i in range(len(snk.snake_body)):
        if snk.snake_body[i].x == pnt.x and snk.snake_body[i].y == pnt.y:
            snk.score += 1
            grow.play()
            pnt.get_random()
            print('Score is: ', snk.score)
    '''
    # if snk.snake_x == pnt.x and snk.snake_y == pnt.y:
    if snk.snake_body[0].x == pnt.x and snk.snake_body[0].y == pnt.y:
        snk.score += 1
        grow.play()
        
        snk.add_point(snk.snake_body[0].x, snk.snake_body[0].y)
        pnt.get_random()
        print('Score is: ', snk.score)
        print(len(snk.snake_body))
    
    pygame.display.update()


'''
la serpiente tiene un punto inicial que se mueve
pero no debe ser asi, la serpiente debe de tener una dimension
inicial la cual marque su punto inicial y actualize tanto a este como al resto
para la actualizacion debo de crear un punto auxiliar el cual contenga la posicion
del punto inicial y se vaya cambiando en valor de posicion y cada uno de los n puntos
de la serpiente, asi el punto auxiliar sera actualizado en cada iteracion dando asi
la posicion al siguiente punto
'''