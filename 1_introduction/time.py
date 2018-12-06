#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pygame 


pygame.init()

width, height = 400, 500

surface = pygame.display.set_mode( (width, height) )
pygame.display.set_caption('Time')

# Colors
red = pygame.Color(115, 38, 80)
white = pygame.Color(255, 255, 255)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    time = pygame.time.get_ticks() // 1000 # return milsecs
    print(time)
    surface.fill(white)

    pygame.display.update()