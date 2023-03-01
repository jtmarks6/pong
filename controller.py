import pygame
import sys
import time
from model import *
from view import *

pygame.init()
pygame.display.set_caption("Pong")
screen_size = width, height = 800, 500

surface = pygame.display.set_mode(screen_size, flags=pygame.SCALED, vsync=1)
ball = Ball(surface)
paddle1 = Paddle(surface, pygame.K_w, pygame.K_s)
paddle2 = Paddle(surface, pygame.K_UP, pygame.K_DOWN, False)
objects = [ball, paddle1, paddle2]
bouncing = False
last_time = time.time() * 1000

while True:
    game_time  = time.time() * 1000
    if(game_time - last_time < 1000/60):
        continue

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    keys = pygame.key.get_pressed()
    delta_time = game_time - last_time
    for i, obj in enumerate(objects):
        obj.move(delta_time, keys)

    if ball.left < 0 or ball.right > width:
        sys.exit()

    if ball.left <= paddle1.paddle.right and paddle1.paddle.bottom >= ball.centery and ball.centery >= paddle1.paddle.top:
        if not bouncing:
            bouncing = True
            ball.bounce(x=True)
    elif ball.right >= paddle2.paddle.left and paddle2.paddle.bottom >= ball.centery and ball.centery >= paddle2.paddle.top:
        if not bouncing:
            bouncing = True
            ball.bounce(x=True)
    elif ball.top < 0 or ball.bottom > height:
            ball.bounce(y=True)
    else:
        bouncing = False

    update_display(surface, objects)
    last_time = game_time


pygame.display.set_caption("Pong")
surface = pygame.display.set_mode(screen_size, flags=pygame.SCALED, vsync=1)
font = pygame.font.Font('freesansbold.ttf', 32)

text = font.render(str(score), True, green)
textRect = text.get_rect()
textRect.centerx = (width // 2)