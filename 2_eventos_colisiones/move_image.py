#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pygame 


pygame.init()

width, height = 400, 500

surface = pygame.display.set_mode( (width, height) )
pygame.display.set_caption('Move image')

# Colors
red = pygame.Color(115, 38, 80)
white = pygame.Color(255, 255, 255)

# image
image = pygame.image.load("../1_introduction/images/medium_circle.png")
rect = image.get_rect()
rect.center = (width//2, height//2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_w] or pressed[pygame.K_UP]:
        rect.y -= 1
    if pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
        rect.y += 1
    if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
        rect.x -= 1
    if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
        rect.x += 1

    if rect.left < 0:
        rect.left = 0
    if rect.right > width:
        rect.right = width
    if rect.top < 0:
        rect.top = 0
    if rect.bottom > height:
        rect.bottom = height

    surface.fill(white)
    surface.blit(image, rect)
    pygame.display.update()