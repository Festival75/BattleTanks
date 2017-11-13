# -*- coding: utf-8 -*-
from Constants import *
import pygame
import logging
import traceback
import sys


class Battlefield:

    def __init__(self, screen):
        """Инициализация переменных"""
        logging.basicConfig(filename='Game.log', format='%(asctime)s - %(levelname)s : %(message)s', level=logging.INFO)
        logging.info('Initialize Battlefield class')
        self.battlefield_map = {}
        self.battlefield_ready = False
        self.rows = SCREEN_WIDTH // 64
        self.cols = SCREEN_HEIGHT // 64
        self.blocks = self.rows * self.cols
        self.block_x = 0
        self.block_y = 0
        self.screen = screen
        try:
            self.sand_block_type1 = pygame.image.load('data/landscape/tileSand1.png').convert_alpha()
            self.sand_block_type2 = pygame.image.load('data/landscape/tileSand2.png').convert_alpha()
            self.grass_block_type1 = pygame.image.load('data/landscape/tileGrass1.png').convert_alpha()
            self.grass_block_type2 = pygame.image.load('data/landscape/tileGrass2.png').convert_alpha()
        except FileNotFoundError as e:
            logging.error('Error in class Battlefield, module __init__. {0}'.format(
                traceback.print_exc(limit=2, file=sys.stdout)))

    def build_field(self):
        """Сформировать карту игрового поля, на основании настроек"""
        row = 0
        count = 0
        while row <= self.rows:
            row_map = []
            col = 0
            while col < self.cols:
                try:
                    row_map.append(MAP[count])
                except IndexError:
                    break
                count += 1
                col += 1
            self.battlefield_map[row] = row_map
            print(self.battlefield_map)
            row += 1

    def render_battlefield(self):
        """Отрисовать поле на основе полученной карты"""
        row = 0
        while row <= self.rows:
            col = 0
            count = 0
            while col < self.cols:
                try:
                    if self.battlefield_map[row][count] == TILE_GRASS_TYPE1:
                        self.screen.blit(self.grass_block_type1, (self.block_x + (64 * col), self.block_y + (64 * row)))
                    elif self.battlefield_map[row][count] == TILE_GRASS_TYPE2:
                        self.screen.blit(self.grass_block_type2, (self.block_x + (64 * col), self.block_y + (64 * row)))
                    elif self.battlefield_map[row][count] == TILE_SAND_TYPE1:
                        self.screen.blit(self.sand_block_type1, (self.block_x + (64 * col), self.block_y + (64 * row)))
                    else:
                        self.screen.blit(self.sand_block_type2, (self.block_x + (64 * col), self.block_y + (64 * row)))
                    col += 1
                    count += 1
                except IndexError:
                    break
            row += 1
