import pygame
from random import randint
import time

pygame.init()
pygame.font.init()
pygame.mixer.init()

dice_sound = pygame.mixer.Sound("dice.wav")

screen_height = 400
screen_width = 400
screen_size = (screen_width, screen_height)

WHITE = (255,255,255)
BLACK = (0,0,0)

screen = pygame.display.set_mode(screen_size)
myfont = pygame.font.SysFont("Calibri", 30)
myfont.set_bold(True)

def roll_button():
    btn_w = 100
    btn_h = 50
    btn_rect = pygame.draw.rect(screen, WHITE, ((int(screen_width/2)-int(btn_w/2)),50,btn_w,btn_h))
    return btn_rect

def draw_text():
    text = myfont.render("ROLL", False, BLACK)
    screen.blit(text, (165, 60))

def draw_cube():
    pygame.draw.rect(screen, WHITE, ((int(screen_width/2)-100),160,200,200))

def draw_circle(x, y):
    pygame.draw.circle(screen, BLACK, (x, y), 25)

def draw_points(number):
    n = int(number)
    if n == 1:
        draw_circle(int(screen_width/2), 265)
    elif n == 2:
        draw_circle(int(screen_width/2), 225)
        draw_circle(int(screen_width/2), 305)
    elif n == 3:
        draw_circle(155, 215)
        draw_circle(int(screen_width/2), 265)
        draw_circle(245, 315)
    elif n == 4:
        draw_circle(155, 215)
        draw_circle(155, 315)
        draw_circle(245, 215)
        draw_circle(245, 315)
    elif n == 5:
        draw_circle(155, 215)
        draw_circle(155, 315)
        draw_circle(245, 215)
        draw_circle(245, 315)
        draw_circle(int(screen_width/2), 265)
    elif n == 6:
        draw_circle(155, 210)
        draw_circle(155, 265)
        draw_circle(155, 320)
        draw_circle(245, 210)
        draw_circle(245, 265)
        draw_circle(245, 320)
    else:
        pass

FPS = 20
clock = pygame.time.Clock()
current_points = 0

run = True
while run:
    clock.tick(FPS)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONUP:
            current_points = randint(1,7)
            pygame.mixer.Sound.play(dice_sound)
           
    if keys[pygame.K_q]:
        run = False

    screen.fill(BLACK)
    draw_cube()
    roll_button()
    draw_text()
    draw_points(current_points)
    pygame.display.flip()
pygame.quit()