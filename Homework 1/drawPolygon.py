import pygame
import numpy as np

width = 800
height = 600
pygame.init()
screen = pygame.display.set_mode((width, height), 0, 32)

background_image_filename = 'image/curve_pattern.png'
background = pygame.image.load(background_image_filename).convert()
width, height = background.get_size()
screen = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption("ImagePolylineMouseButton")

BLACK = (0, 0, 0)
GREY = (128, 128, 128)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
SKY_BLUE = (135, 206, 235)
RED = (255, 0, 0)
PINK = (255, 192, 203)
ORANGE = (255, 165, 0)

old_pt = np.array([0, 0])
cur_pt = np.array([0, 0])

screen.fill(WHITE)

clock = pygame.time.Clock()

done = False
pressed = -1
margin = 6
npressed_button1, npressed_button2, npressed_button3 = 0, 0, 0
while not done:
    time_passed = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pressed = 1
        elif event.type == pygame.MOUSEMOTION:
            pressed = 0
        elif event.type == pygame.MOUSEBUTTONUP:
            pressed = 2
        elif event.type == pygame.QUIT:
            done = True
        else:
            pressed = -1

    button1, button2, button3 = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    cur_pt = np.array([x, y])
    if old_pt[0] != 0 and old_pt[1] != 0:
        pygame.draw.circle(screen, ORANGE, cur_pt, 2, 0)

    if pressed == 1:
        if button1 == 1:
            pygame.draw.rect(screen, BLUE, (cur_pt[0] - margin, cur_pt[1] - margin, 2 * margin, 2 * margin), 5)
            if npressed_button1 == 0:
                pygame.draw.lines(screen, SKY_BLUE, True, (cur_pt, cur_pt), 2)
            else:
                pygame.draw.lines(screen, SKY_BLUE, True, (old_pt_button1, cur_pt), 2)
            old_pt_button1 = cur_pt
            npressed_button1 += 1
        elif button3 == 1:
            pygame.draw.rect(screen, RED, (cur_pt[0] - margin, cur_pt[1] - margin, 2 * margin, 2 * margin), 5)
            if npressed_button3 == 0:
                pygame.draw.lines(screen, PINK, True, (cur_pt, cur_pt), 2)
            else:
                pygame.draw.lines(screen, PINK, True, (old_pt_button3, cur_pt), 2)
            old_pt_button3 = cur_pt
            npressed_button3 += 1
        elif button2 == 1:
            pygame.draw.rect(screen, BLACK, (cur_pt[0] - margin, cur_pt[1] - margin, 2 * margin, 2 * margin), 5)
            if npressed_button2 == 0:
                pygame.draw.lines(screen, GREY, True, (cur_pt, cur_pt), 2)
            else:
                pygame.draw.lines(screen, GREY, True, (old_pt_button2, cur_pt), 2)
            old_pt_button2 = cur_pt
            npressed_button2 += 1
    print("mouse x:" + repr(x) + " y:" + repr(y) + " button:" + repr(button1) + " " + repr(button2) + " " + repr(
        button3) + " pressed:" + repr(pressed))
    old_pt = cur_pt

    pygame.display.update()

pygame.quit()