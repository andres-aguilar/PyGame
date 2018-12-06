#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math
import pygame 


pygame.init()

width, height = 400, 500

surface = pygame.display.set_mode( (width, height) )
pygame.display.set_caption('Circle collition')

# Colors
red = pygame.Color(115, 38, 80)
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 200, 0)
blue = pygame.Color(0, 0, 200)

# Image
image = pygame.image.load("../1_introduction/images/medium_circle.png")
rect = image.get_rect()
rect.center = (width//2, height//2)

image1 = pygame.image.load('../1_introduction/images/medium_circle.png')
rect1 = image1.get_rect()
rect1.center = (width//2, height//2)

surface2 = pygame.Surface( (rect1.width, rect1.height), pygame.SRCALPHA )
surface2.fill( (0, 0, 0, 50) )
rect2 = surface2.get_rect()
rect2.center = rect1.center

# Mensaje
font = pygame.font.Font("freesansbold.ttf", 32)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(white)
    rect.center = pygame.mouse.get_pos()

    surface.blit(image1, rect1)
    surface.blit(surface2, rect2)
    surface.blit(image, rect)

    dist = math.hypot(rect.x - rect1.x, rect.y - rect1.y)
    r = 64  # Radio del círculo en la imágen
    message = str(dist)

    pygame.draw.line(surface, (0, 0, 0), rect.center, rect1.center, 4)

    if dist < (r+r):
        message = "colision"

    text = font.render(message, True, blue)
    rect3 = text.get_rect()
    rect3.midtop = (width//2, 50)

    surface.blit(text, rect3)

    pygame.display.update()