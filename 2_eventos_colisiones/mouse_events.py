#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pygame 


pygame.init()

width, height = 400, 500

surface = pygame.display.set_mode( (width, height) )
pygame.display.set_caption('Mouse events')

# Colors
red = pygame.Color(115, 38, 80)
white = pygame.Color(255, 255, 255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Mouse events
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("clic izquierdo en ", event.pos)
            if event.button == 2:
                print("click central en ", event.pos)
            if event.button == 3:
                print("clic derecho en ", event.pos)
        # if event.type =0 pygame.MOUSEBUTTONUP

    surface.fill(white)
    pygame.display.update()