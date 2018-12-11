import sys, pygame, random
from pygame.locals import *
import pygame.event

pygame.init()

screen_width = 720
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake')


class snake:
    image = pygame.image.load('img/red.png')
    snake_body = 1
    snake_is_in_live = True
    snake_x, snake_y = 0, 0
    score = 0

    def __init__(self):
        self.snake_x = random.randint(0, screen_width / 16)
        self.snake_y = random.randint(0, screen_height / 16)

    def draw_snake(self):
        screen.blit(snake.image, (self.snake_x * 16, self.snake_y * 16))


def draw_background(screen):
    background_img = pygame.image.load('img/white.png')
    for i in range(0, 40):
        for j in range(0, 45):
            screen.blit(background_img, (j * 16, i * 16))


'''    
16*30 = 480
16*40 = 640
16*45 = 720
'''


class point:
    x, y = 0, 0
    img = pygame.image.load('img/green.png')

    def __init__(self):
        self.x = random.randint(0, screen_width / 16)
        self.y = random.randint(0, screen_height / 16)

    def get_random(self):
        self.x = random.randint(0, screen_width / 16)
        self.y = random.randint(0, screen_height / 16)

    def draw_image(self):
        screen.blit(self.img, (self.x * 16, self.y * 16))


snk = snake()
pnt = point()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                snk.snake_y += 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snk.snake_y -= 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snk.snake_x -= 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snk.snake_x += 1

    draw_background(screen)
    pnt.draw_image()
    snk.draw_snake()
    if snk.snake_x == pnt.x and snk.snake_y == pnt.y:
        snk.score += 1
        pnt.get_random()
        print('Score is: ', snk.score)
    pygame.display.update()