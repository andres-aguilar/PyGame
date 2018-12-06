#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pygame 


pygame.init()

width, height = 400, 500

surface = pygame.display.set_mode( (width, height) )
pygame.display.set_caption('Sounds')

# Colors
red = pygame.Color(115, 38, 80)
white = pygame.Color(255, 255, 255)

# Music
pygame.mixer.music.load('sounds/Haggstrom.mp3')
pygame.mixer.music.set_volume(1.0)  # from 0 to 1.0
# Camtidad de repeticiones (-1 para infinito), minuto de inicio de la canción
pygame.mixer.music.play(-1, 0) 


# Funciones para modificar el comportamiento de la música
# rewind  -> reiniciar
# pause   -> pausar
# stop    -> detener
# fadeout -> Bajar el volumen al para finalizar suavemente

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(white)
    pygame.display.update()