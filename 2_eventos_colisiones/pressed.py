#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pygame 


pygame.init()

width, height = 400, 500

surface = pygame.display.set_mode( (width, height) )
pygame.display.set_caption('Key events')

# Colors
red = pygame.Color(115, 38, 80)
white = pygame.Color(255, 255, 255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_w] or pressed[pygame.K_UP]:
            print('arriba')
        if pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
            print('abajo')
        if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
            print('izquierda')
        if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
            print('derecha')

    surface.fill(white)
    pygame.display.update()