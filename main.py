import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600

black = (0, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong Game')

paddle_width = 15
paddle_height = 90

ball_size = 15

player1_x = 50
player1_y = (screen_height // 2) - (paddle_height // 2)
player2_x = screen_width - 50 - paddle_width
player2_y = (screen_height // 2) - (paddle_height // 2)

ball_x = screen_width // 2
ball_y = screen_height // 2
ball_speed_x = 5
ball_speed_y = 5

paddle_speed = 5

clock = pygame.time.Clock()

def draw_objects():
    screen.fill(black)
    pygame.draw.rect(screen, white, (player1_x, player1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (player2_x, player2_y, paddle_width, paddle_height))
    pygame.draw.ellipse(screen, white, (ball_x, ball_y, ball_size, ball_size))
    pygame.draw.aaline(screen, white, (screen_width // 2, 0), (screen_width // 2, screen_height))
    pygame.display.flip()

def move_ball():
    global ball_x, ball_y, ball_speed_x, ball_speed_y

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_y <= 0 or ball_y >= screen_height - ball_size:
        ball_speed_y *= -1

    if (player1_x < ball_x < player1_x + paddle_width and player1_y < ball_y < player1_y + paddle_height) or \
       (player2_x < ball_x < player2_x + paddle_width and player2_y < ball_y < player2_y + paddle_height):
        ball_speed_x *= -1

def handle_input():
    global player1_y, player2_y

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= paddle_speed
    if keys[pygame.K_s] and player1_y < screen_height - paddle_height:
        player1_y += paddle_speed
    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= paddle_speed
    if keys[pygame.K_DOWN] and player2_y < screen_height - paddle_height:
        player2_y += paddle_speed

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    handle_input()
    move_ball()
    draw_objects()
    
    clock.tick(60)
