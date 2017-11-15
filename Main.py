# -*- coding: utf-8 -*-
from Battlefield import *
from Player import *
import pygame
import logging


class Main:

    def __init__(self, screen):
        """Инициализация переменных и создание экземпляров классов"""
        logging.info('Initialize Main class')
        self.player = Player(screen, 'Test', 'SAND', 'BARREL_TYPE2', PLAYER_SPEED)
        self.battlefield = Battlefield(screen)
        self.screen = screen
        self.running = True
        self.main_loop()

    def render(self):
        """Отрисовка игровых классов"""

        self.battlefield.render_battlefield()
        self.player.render()
        pygame.display.flip()

    def handle_events(self):
        """Логика реакций игры на нажатия клавиш"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.player.direction = EAST
                    self.player.moving = [0, 0, 1, 0, 0, 0, 0, 0]
                if event.key == pygame.K_DOWN:
                    self.player.direction = SOUTH
                    self.player.moving = [0, 0, 0, 0, 1, 0, 0, 0]
                if event.key == pygame.K_LEFT:
                    self.player.direction = WEST
                    self.player.moving = [0, 0, 0, 0, 0, 0, 1, 0]
                if event.key == pygame.K_UP:
                    self.player.direction = NORTH
                    self.player.moving = [1, 0, 0, 0, 0, 0, 0, 0]
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.player.direction = EAST
                    self.player.moving[EAST] = 0
                if event.key == pygame.K_DOWN:
                    self.player.direction = SOUTH
                    self.player.moving[SOUTH] = 0
                if event.key == pygame.K_LEFT:
                    self.player.direction = WEST
                    self.player.moving[WEST] = 0
                if event.key == pygame.K_UP:
                    self.player.direction = NORTH
                    self.player.moving[NORTH] = 0



    def main_loop(self):
        """Основной цикл программы"""
        logging.info('Starting main_loop')
        while self.running:
            self.battlefield.build_field()
            self.player.move()
            self.render()
            self.handle_events()
            self.player.tile_effect(self.battlefield.build_field())
        logging.info('Main_loop stop')

if __name__ == '__main__':
    with open('Game.log', 'w'):
        pass
    logging.basicConfig(filename='Game.log', format='%(asctime)s - %(levelname)s : %(message)s', level=logging.INFO)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Main(screen)
