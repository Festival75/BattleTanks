# -*- coding: utf-8 -*-
from Constants import *
import pygame
import logging

class Player:
    def __init__(self, screen, name, color, barrel_type, speed):
        """Инициализация переменных и выполнение необходимых преобразований"""
        logging.basicConfig(filename='Game.log', format='%(asctime)s - %(levelname)s : %(message)s', level=logging.INFO)
        logging.info('Initialize Player class')
        self.body_image_pack = []  # список с картинками корпуса на 4 направления
        self.barrel_image_pack = []  # список с картинками пушки на 4 направления
        self.screen = screen
        self.current_direction = NORTH
        self.direction = NORTH
        self.position_x = START_X
        self.position_y = START_Y
        self.moving = [0, 0, 0, 0, 0, 0, 0, 0]
        self.color = color
        self.barrel_type = barrel_type
        self.name = name
        self.image_pack = {"BLUE": {"BODY": "data/tank/tankBody_blue.png",
                                    "BARREL_TYPE1": "data/tank/tankBlue_barrel1_outline.png",
                                    "BARREL_TYPE2": "data/tank/tankBlue_barrel2_outline.png",
                                    "BARREL_TYPE3": "data/tank/tankBlue_barrel3_outline.png"},
                           "DARK": {"BODY": "data/tank/tankBody_dark.png",
                                    "BARREL_TYPE1": "data/tank/tankDark_barrel1_outline.png",
                                    "BARREL_TYPE2": "data/tank/tankDark_barrel2_outline.png",
                                    "BARREL_TYPE3": "data/tank/tankDark_barrel3_outline.png"},
                           "GREEN": {"BODY": "data/tank/tankBody_green.png",
                                     "BARREL_TYPE1": "data/tank/tankGreen_barrel1_outline.png",
                                     "BARREL_TYPE2": "data/tank/tankGreen_barrel2_outline.png",
                                     "BARREL_TYPE3": "data/tank/tankGreen_barrel3_outline.png"},
                           "RED": {"BODY": "data/tank/tankBody_red.png",
                                   "BARREL_TYPE1": "data/tank/tankRed_barrel1_outline.png",
                                   "BARREL_TYPE2": "data/tank/tankRed_barrel2_outline.png",
                                   "BARREL_TYPE3": "data/tank/tankRed_barrel3_outline.png"},
                           "SAND": {"BODY": "data/tank/tankBody_sand.png",
                                    "BARREL_TYPE1": "data/tank/tankSand_barrel1_outline.png",
                                    "BARREL_TYPE2": "data/tank/tankSand_barrel2_outline.png",
                                    "BARREL_TYPE3": "data/tank/tankSand_barrel3_outline.png"}
                           }
        self.barrel = None
        self.tank = None
        self.image_pack_generator()
        self.speed = speed

    def image_pack_generator(self):
        """Генерирует по 8 изображений корпуса и пушки, на 8 основных направлений"""
        for direction in DIRECTIONS:
            body = pygame.image.load(self.image_pack[self.color]['BODY']).convert_alpha()
            body = pygame.transform.rotate(body, direction)
            barrel = pygame.image.load(self.image_pack[self.color][self.barrel_type]).convert_alpha()
            barrel = pygame.transform.rotate(barrel, direction)
            self.body_image_pack.append(body)
            self.barrel_image_pack.append(barrel)
        # костыль изза косяка в расположении моделек
        barrel_temp = self.barrel_image_pack[0]
        self.barrel_image_pack[0] = self.barrel_image_pack[4]
        self.barrel_image_pack[4] = barrel_temp
        body_temp = self.body_image_pack[2]
        self.body_image_pack[2] = self.body_image_pack[6]
        self.body_image_pack[6] = body_temp
        # конец костыля

    def move(self):
        """Изменяет координаты танка в завимости от значения списка moving"""
        if self.moving[EAST] == 1: self.position_x += self.speed
        if self.moving[SOUTH] == 1: self.position_y += self.speed
        if self.moving[WEST] == 1: self.position_x -= self.speed
        if self.moving[NORTH] == 1: self.position_y -= self.speed

        # танк не выезжает за границы экрана
        if self.position_x <= 0: self.position_x = 0
        if self.position_y <= 0: self.position_y = 0
        if self.position_x >= SCREEN_WIDTH - 38: self.position_x = SCREEN_WIDTH - 38
        if self.position_y >= SCREEN_HEIGHT - 38: self.position_y = SCREEN_HEIGHT - 38

    def barrel_position(self) -> tuple:
        """Управляет положением пушки относительно модели танка"""
        if self.direction == NORTH:
            barrel_x = self.position_x + (self.tank.get_rect().center[0] - self.barrel.get_rect().center[0])
            barrel_y = self.position_y + (self.tank.get_rect().center[1] - 2*self.barrel.get_rect().center[1])
        elif self.direction == EAST:
            barrel_x = self.position_x + self.tank.get_rect().center[0]
            barrel_y = self.position_y + (self.tank.get_rect().center[1] - self.barrel.get_rect().center[1])
        elif self.direction == WEST:
            barrel_x = self.position_x - (self.tank.get_rect().center[0] - self.barrel.get_rect().center[0]//2)
            barrel_y = self.position_y + (self.tank.get_rect().center[1] - self.barrel.get_rect().center[1])
        elif self.direction == SOUTH:
            barrel_x = self.position_x + (self.tank.get_rect().center[0] - self.barrel.get_rect().center[0])
            barrel_y = self.position_y - (self.tank.get_rect().center[1] - self.barrel.get_rect().center[1]*2 - 4)
        barrel_position = (barrel_x, barrel_y)
        return barrel_position

    def object_rotation(self):
        pass

    def tile_effect(self, bf_map):
        row = self.position_y // 64
        col = self.position_x // 64
        current_tile = bf_map[row][col]
        if current_tile == TILE_SAND_TYPE1 or current_tile == TILE_SAND_TYPE2:
            self.speed = PLAYER_SPEED - 1
        elif current_tile == TILE_GRASS_TYPE1 or current_tile == TILE_GRASS_TYPE2:
            self.speed = PLAYER_SPEED

    def render(self):
        """Отрисовка модели танка на текущей позиции (x,y)"""
        direction = self.direction

        self.tank = self.body_image_pack[direction]
        self.screen.blit(self.tank, (self.position_x, self.position_y))

        self.barrel = self.barrel_image_pack[direction]
        self.screen.blit(self.barrel, self.barrel_position())

    def render_ui(self):
        pass
