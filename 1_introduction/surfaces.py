#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pygame 


pygame.init()

width = 400
height = 500

surface = pygame.display.set_mode( (width, height) )
pygame.display.set_caption('Surfaces')

# Colors
red = pygame.Color(115, 38, 80)
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 200, 0)
blue = pygame.Color(0, 0, 200)

surface2 = pygame.Surface( (200, 200) )
surface2.fill(green)

rect = surface2.get_rect()
rect.center = ( width//2, height//2 )

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(white)

    surface.blit(surface2, rect )
    pygame.draw.rect( surface2, red, (100, 50, 80, 40) )

    pygame.display.update()