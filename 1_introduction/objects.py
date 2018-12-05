#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pygame 


pygame.init()

width = 400
height = 500

surface = pygame.display.set_mode( (width, height) )
pygame.display.set_caption('Colors')

# RBG
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

    pygame.draw.rect(surface, red, (100, 100, 80, 40))
    # lienzo, color, (x, y), radio (px)
    pygame.draw.circle(surface, green, (200, 300), 100)
    # lienzo, color, inicio(x, y), fin(x, y), grosor (px)
    pygame.draw.line(surface, blue, (100, 100), (200, 300), 2)

    pygame.display.update()