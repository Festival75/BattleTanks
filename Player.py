# -*- coding: utf-8 -*-
from Constants import *
import pygame
import logging


class Player:

    def __init__(self, screen, name, color, barrel_type):
        """Инициализация переменных и выполнение необходимых преобразований"""
        logging.basicConfig(filename='Game.log', format='%(asctime)s - %(levelname)s : %(message)s', level=logging.INFO)
        logging.info('Initialize Player class')
        self.tank = []                  # список представляющий собой танк (корпус+пушка)
        self.body_image_pack = []       # список с картинками корпуса на 4 направления
        self.barrel_image_pack = []     # список с картинками пушки на 4 направления
        self.screen = screen
        self.direction = RIGHT
        self.position_x = START_X
        self.position_y = START_Y
        self.moving = [0, 0, 0, 0]
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
        self.rotate()
        self.select_tank_type()

    def select_tank_type(self):
        """Формирует модель танка, выбирая изображения корпуса и пушки"""

        if self.color in self.image_pack.keys():
            body = self.body_image_pack[self.direction]
            self.tank.append(body)
        else:
            exit()
        if self.barrel_type in self.image_pack[self.color].keys():
            barrel = self.barrel_image_pack[self.direction]
            self.tank.append(barrel)
        else:
            exit()

    def rotate(self):
        """Генерирует по 4 изображения корпуса и пушки, на 4 основных направления"""
        self.body_image_pack.append(
            pygame.transform.rotate(pygame.image.load(self.image_pack[self.color]['BODY']).convert_alpha(), 90))
        self.body_image_pack.append(pygame.image.load(self.image_pack[self.color]['BODY']).convert_alpha())
        self.body_image_pack.append(
            pygame.transform.rotate(pygame.image.load(self.image_pack[self.color]['BODY']).convert_alpha(), 270))
        self.body_image_pack.append(
            pygame.transform.rotate(pygame.image.load(self.image_pack[self.color]['BODY']).convert_alpha(), 180))
        self.barrel_image_pack.append(
            pygame.transform.rotate(pygame.image.load(self.image_pack[self.color][self.barrel_type]).convert_alpha(),
                                    90))
        self.barrel_image_pack.append(pygame.image.load(self.image_pack[self.color][self.barrel_type]).convert_alpha())
        self.barrel_image_pack.append(
            pygame.transform.rotate(pygame.image.load(self.image_pack[self.color][self.barrel_type]).convert_alpha(),
                                    270))
        self.barrel_image_pack.append(
            pygame.transform.rotate(pygame.image.load(self.image_pack[self.color][self.barrel_type]).convert_alpha(),
                                    180))

    def move(self):
        """Изменяет координаты танка в завимости от значения списка moving"""
        if self.moving[RIGHT] == 1: self.position_x += PLAYER_SPEED
        if self.moving[DOWN] == 1: self.position_y += PLAYER_SPEED
        if self.moving[LEFT] == 1: self.position_x -= PLAYER_SPEED
        if self.moving[UP] == 1: self.position_y -= PLAYER_SPEED

        # танк не выезжает за границы экрана
        if self.position_x <= 0: self.position_x = 0
        if self.position_y <= 0: self.position_y = 0
        if self.position_x >= SCREEN_WIDTH - 38: self.position_x = SCREEN_WIDTH - 38
        if self.position_y >= SCREEN_HEIGHT - 38: self.position_y = SCREEN_HEIGHT - 38

    def barrel_position(self) -> tuple:
        """Управляет положением пушки относительно модели танка"""
        if self.direction == DOWN:
            barrel_x = self.position_x + (self.tank[0].get_rect().center[0] - self.tank[1].get_rect().center[0])
            barrel_y = self.position_y + self.tank[0].get_rect().center[1]
        elif self.direction == RIGHT:
            barrel_x = self.position_x + (self.tank[0].get_rect().midright[0] - self.tank[0].get_rect().center[0])
            barrel_y = self.position_y + (self.tank[0].get_rect().center[1] - self.tank[1].get_rect().center[1])
        elif self.direction == LEFT:
            barrel_x = (self.position_x + 7) - (self.tank[0].get_rect().midright[0] - self.tank[0].get_rect().center[0])
            barrel_y = self.position_y + (self.tank[0].get_rect().center[1] - self.tank[1].get_rect().center[1])
        else:
            barrel_x = self.position_x + (self.tank[0].get_rect().center[0] - self.tank[1].get_rect().center[0])
            barrel_y = (self.position_y + 6) - self.tank[0].get_rect().center[1]
        barrel_position = (barrel_x, barrel_y)
        return barrel_position

    def render(self):
        """Отрисовка модели танка на текущей позиции (x,y)"""
        self.tank = [self.body_image_pack[self.direction], self.barrel_image_pack[self.direction]]
        self.screen.blit(self.tank[0], (self.position_x, self.position_y))
        self.screen.blit(self.tank[1], self.barrel_position())

    def render_ui(self):
        pass
