#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pygame 


pygame.init()

width, height = 400, 500

surface = pygame.display.set_mode( (width, height) )
pygame.display.set_caption('Text')

# Colors
red = pygame.Color(115, 38, 80)
white = pygame.Color(255, 255, 255)

# font = pygame.font.Font('freesansbold.ttf', 36)
font = pygame.font.Font('roboto/Roboto-Thin.ttf', 36)
text_surface = font.render('Hola mundo', True, red)

rect = text_surface.get_rect()
rect.center = (width//2, height//2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(white)

    surface.blit(text_surface, rect)

    pygame.display.update()