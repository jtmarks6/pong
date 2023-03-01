import pygame, sys

pygame.init()

playing = True
score = 0

screen_size = width, height = 800, 500
black = 0, 0, 0
green = 0, 255, 0
white = 255, 255, 255

ball_speed = [10, 10]
ball_size = ball_width, ball_height = 20, 20
ball_pos = ballX, ballY = width / 2, height / 2

paddle_speed = 20
paddle_size = paddle_width, paddle_height = 30, 150
paddle_pos = paddleX, paddleY = 0, 0

pygame.display.set_caption("Pong")
surface = pygame.display.set_mode(screen_size, flags=pygame.SCALED, vsync=1)
font = pygame.font.Font('freesansbold.ttf', 32)

ball = pygame.Rect(ballX, ballY, ball_width, ball_height)
paddle = pygame.Rect(paddleX, paddleY, paddle_width, paddle_height)
text = font.render(str(score), True, green)
textRect = text.get_rect()
textRect.centerx = (width // 2)

def move_paddle(paddle_rect):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and paddle_rect.top > 0:
        paddle_rect.move_ip(0, -paddle_speed)
    elif keys[pygame.K_DOWN] and paddle.bottom < height:
        paddle_rect.move_ip(0, paddle_speed)


def move_ball(ball_rect, paddle_rect):
    ball_rect.move_ip(ball_speed)
    
    if ball_rect.left < 0:
        global playing
        playing = False

    if ball_rect.right > width:
        ball_speed[0] = -ball_speed[0]
    elif ball_rect.left == paddle_rect.right and paddle_rect.bottom >= ball_rect.centery and ball_rect.centery >= paddle_rect.top:
        global score
        score += 1
        ball_speed[0] = -ball_speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > height:
        ball_speed[1] = -ball_speed[1]


while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    move_ball(ball, paddle)
    move_paddle(paddle)
    text = font.render(str(score), True, green)

    surface.fill(black)
    pygame.draw.rect(surface, green, ball)
    pygame.draw.rect(surface, white, paddle)
    surface.blit(text, textRect)
    
    pygame.display.update()