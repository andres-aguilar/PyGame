#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pygame 


pygame.init()

width, height = 400, 500

surface = pygame.display.set_mode( (width, height) )
pygame.display.set_caption('Circle collition')

# Colors
red = pygame.Color(115, 38, 80)
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 200, 0)
blue = pygame.Color(0, 0, 200)

# Image
image1 = pygame.image.load('../1_introduction/images/medium_circle.png')
rect1 = image1.get_rect()
rect1.center = (width//2, height//2)

surface2 = pygame.Surface( (rect1.width, rect1.height), pygame.SRCALPHA )
surface2.fill( (0, 0, 0, 50) )
rect2 = surface2.get_rect()
rect2.center = rect1.center

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(white)

    surface.blit(image1, rect1)
    surface.blit(surface2, rect2)

    pygame.display.update()