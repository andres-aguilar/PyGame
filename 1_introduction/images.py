#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pygame 


pygame.init()

width = 500
height = 600

surface = pygame.display.set_mode( (width, height) )
pygame.display.set_caption('Images')

# Colors
white = pygame.Color(255, 255, 255)

image = pygame.image.load('images/codi.png')
rect = image.get_rect()
rect.center = (width//2, height//2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(white)

    surface.blit(image, rect)

    pygame.display.update()