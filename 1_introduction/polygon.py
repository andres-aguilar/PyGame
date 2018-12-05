#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pygame 


pygame.init()

width = 400
height = 500

surface = pygame.display.set_mode( (width, height) )
pygame.display.set_caption('Colors')

# Colors
red = pygame.Color(115, 38, 80)
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 200, 0)
blue = pygame.Color(0, 0, 200)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(white)

    # Triangulo - lienzo, color, tupla de tuplas con los puntos del triangulo
    pygame.draw.polygon(surface, green, ( (0, 450), (100, 300), (200, 450) ))
    # Pentagono - lienzo, color, tupla de tuplas con los puntos del pentagono
    pygame.draw.polygon(surface, red, ( (146, 0), (291, 106), (236, 277), (56, 277), (0, 106) ))

    pygame.display.update()