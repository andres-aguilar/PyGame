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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                print("izquierda")
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                print("derecha")
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                print("arriba")
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                print("abajo")
        #if event.type == pygame.KEYUP:


    surface.fill(white)
    pygame.display.update()