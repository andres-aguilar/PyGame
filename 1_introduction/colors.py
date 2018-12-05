#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pygame 


pygame.init()

width = 400
height = 500

sourface = pygame.display.set_mode( (width, height) )
pygame.display.set_caption('Colors')

# RBG
red = pygame.Color(255, 0, 0)  # también se pueden definir colores mediante tuplas


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    sourface.fill(red)
    pygame.display.update()