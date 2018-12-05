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

rect = pygame.Rect(100, 150, 120, 60)  
rect.center = ( width//2, height//2 )

# También se pueden definir rectangulos por medio de una tupla
rect2 = (100, 100, 80, 40)  

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(white)
    pygame.draw.rect(surface, red, rect)
    pygame.draw.rect(surface, green, rect2)
    pygame.display.update()