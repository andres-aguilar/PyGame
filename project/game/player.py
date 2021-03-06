#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from .config import *

class Player(pygame.sprite.Sprite):
    """ Class Player """

    def __init__(self, left, bottom):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((40, 40))
        self.image.fill(BLUE)
        
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom

        self.pos_y = self.rect.bottom
        self.vel_y = 0

        self.can_jump = False

    def update_pos(self):
        self.vel_y += GRAVITY
        self.pos_y += self.vel_y + 0.1 * GRAVITY

    def update(self):
        self.update_pos()
        self.rect.bottom  = self.pos_y

    def validate_platform(self, platform):
        result = pygame.sprite.collide_rect( self, platform )

        if result:
            self.vel_y = 0
            self.pos_y = platform.rect.top
            self.can_jump = True

    def jump(self):
        if self.can_jump:
            self.vel_y = JUMP_LENGTH
            self.can_jump = False