#imports
import pygame
import sys
import view
import ball_model
import random
import time

## init
SCREEN_SIZE = SCREEN_WIDTH, SCREENHEIGHT = 1000, 500

screen_color = (150, 150, 150)
pygame.init()

pygame.display.set_caption("My Game")
surface = pygame.display.set_mode(SCREEN_SIZE)

x_loc = 400
y_loc = 200
radius = 20


ball = ball_model.Ball(x_loc, y_loc, radius, surface)

count = 0

last_time = time.time() * 1000
print(last_time)
while True:

    game_time  = time.time() * 1000
    if(game_time - last_time < 1000/60):
        continue
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if count % 10 == 0:
        ball.set_velocity([random.randint(-5, 5), random.randint(-5, 5)])
    ball.move_frame()
        
    surface.fill(screen_color)
    view.draw_ball(ball)
    count += 1
    last_time = game_time

"""
    Paddle:
        x_loc
        y_loc
        x_size
        y_size
        movement_vector

        move_frame

        get_x
        get_y

        set_x
        set_y
        set_vector



    Ball:
        x_loc
        y_loc
        radius
        movement_vector

        move_frame

        get_x
        get_y

        set_x
        set_y
        set_vector

    Controller:
        collision handeler

    
"""