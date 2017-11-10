# -*- coding: utf-8 -*-
from Constants import *
import pygame
import random


class Battlefield:
    def __init__(self, screen):
        self.battlefield_ready = False
        self.rows = SCREEN_WIDTH // 64
        self.cols = SCREEN_HEIGHT // 64
        self.blocks = self.rows * self.cols
        self.block_x = 0
        self.block_y = 0
        self.screen = screen
        self.sand_block_type1 = pygame.image.load('data/landscape/tileSand1.png')
        self.sand_block_type2 = pygame.image.load('data/landscape/tileSand2.png')
        self.grass_block_type1 = pygame.image.load('data/landscape/tileGrass1.png')
        self.grass_block_type2 = pygame.image.load('data/landscape/tileGrass2.png')

    def random_block(self):
        num = random.randint(1, 4)
        if num == 1:
            block = self.sand_block_type1
        elif num == 2:
            block = self.sand_block_type2
        elif num == 3:
            block = self.grass_block_type1
        else:
            block = self.grass_block_type2
        return block

    def render_battlefield(self):
        while not self.battlefield_ready:
            col = 0
            while col <= self.cols:
                row = 0
                while row <= self.rows:
                    self.screen.blit(self.random_block(), (self.block_x + (64 * col), self.block_y + (64 * row)))
                    row += 1
                col += 1
            self.battlefield_ready = True
