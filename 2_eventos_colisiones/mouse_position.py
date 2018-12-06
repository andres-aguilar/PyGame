#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pygame 


pygame.init()

width, height = 400, 500

surface = pygame.display.set_mode( (width, height) )
pygame.display.set_caption('Mouse position')

# Colors
red = pygame.Color(115, 38, 80)
white = pygame.Color(255, 255, 255)

font = pygame.font.Font("freesansbold.ttf", 32)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    x, y = pygame.mouse.get_pos()
    message = "mouse position: {},{}".format(x, y)

    text = font.render(message, True, red)
    rect = text.get_rect()
    rect.center = (width//2, height//2)

    surface.fill(white)

    surface.blit(text, rect)

    pygame.display.update()