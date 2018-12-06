#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pygame 


pygame.init()

width, height = 400, 500

surface = pygame.display.set_mode( (width, height) )
pygame.display.set_caption('Collitions')

# Colors
red = pygame.Color(115, 38, 80)
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 200, 0)
blue = pygame.Color(0, 0, 200)

# Figures
rect1 = pygame.Rect(0, 0, 100, 80)
rect1.center = (width//2, height//2)

rect2 = pygame.Rect(0, 0, 100, 80)

# Mensaje
font = pygame.font.Font("freesansbold.ttf", 32)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(white)

    rect2.center = pygame.mouse.get_pos()

    pygame.draw.rect(surface, green, rect1)
    pygame.draw.rect(surface, red, rect2)

    message = ''

    if rect1.colliderect(rect2):
        message = "colision"

    text = font.render(message, True, blue)
    rect3 = text.get_rect()
    rect3.midtop = (width//2, 50)

    surface.blit(text, rect3)

    pygame.display.update()