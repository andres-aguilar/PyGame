#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pygame 

pygame.init()

width, height = 400, 500
center = (width//2, height//2)

surface = pygame.display.set_mode( (width, height) )
pygame.display.set_caption('Masks')

# Colors
red = pygame.Color(115, 38, 80)
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 200, 0)
blue = pygame.Color(0, 0, 200)

# Images
circle = pygame.image.load('../1_introduction/images/medium_circle.png')
circle_rect = circle.get_rect()
circle_rect.center = center
cicle_mask = pygame.mask.from_surface(circle)

rectangle = pygame.image.load('../1_introduction/images/small_rectangle.png')
rectangle_rect = rectangle.get_rect()
rectangle_mask = pygame.mask.from_surface(rectangle)

# Fonts
font = pygame.font.Font('freesansbold.ttf', 32)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(white)

    rectangle_rect.center = pygame.mouse.get_pos()

    surface.blit(circle, circle_rect)
    surface.blit(rectangle, rectangle_rect)

    message = 'Hola'

    offset = (rectangle_rect.x - circle_rect.x, rectangle_rect.y - circle_rect.y)
    if cicle_mask.overlap(rectangle_mask, offset):
        message = 'Colision'

    text = font.render(message, True, blue)
    text_rect = text.get_rect()
    text_rect.midtop = (width//2, 50)

    surface.blit(text, text_rect)

    pygame.display.update()